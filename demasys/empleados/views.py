#from twisted.internet.test._posixifaces import in_addr
from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import permission_required, login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from solicitudes.models import Solicitudes, conceptos, TIPO_STATUS, FORMAS_D_PAGO
##from solicitudes.forms import SolicitudForm, Sol_Edit_1_Form, Sol_Edit_2_Form,SearchForm, Sol_Edit_3_Form, Report_solForm, CAMPOS, Search_Form_Con, conceptos_form, reporteForm
#from empleados.forms import SearchForm, empleadoForm,empleadoSolicitudForm,DocumentacionForm,SalhabForm,FamiliaresForm,EscolaridadForm,ConocimientosForm,EmpleosForm, UploadForm, ReferenciasForm,GeneralesForm,EconomicoForm
from empleados.forms import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
from django.contrib.auth.models import Group
from django.db.models import Q
from django.core.mail import send_mail, EmailMessage

from django.db import connection, transaction
from django.http import QueryDict
####JC
import xlwt
from xlwt import Workbook,XFStyle,Borders, Pattern, Font, easyxf

from datetime import datetime
import time
import logging
import sys, os
import mimetypes
from django.conf import settings
from django.utils.encoding import smart_str
from django.core.servers.basehttp import FileWrapper

from decimal import Decimal
#from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from easy_pdf.views import PDFTemplateView
from django.forms.models import modelformset_factory, inlineformset_factory
from workflow.models import Workflow, WorkflowActivity, Participant, Role, Transition
from cuentas.models import Perfil
from django.contrib.auth.models import User
##from util import to_word

from empleados.models import *
#from empleados.models import empleado, Documentos
#from catalogos.models import Operador
#from beneficiarios.models import Benefi
#from viajes.models import CONCEPTO_GASTO, Gasto, Destino, Viaje
#from sepomex.models import Sepomex
#from contable.models import Area, Movimientos, Partidas
#from django.db.models import Sum
#from contable.views import saldoPartidaXArea
#from catalogos.models import Economico
#from inventario.models import Productos, Movimientos as Movimientos2

from django.contrib.formtools.wizard.views import SessionWizardView

#Ajuste para pdf
from django.template.loader import get_template
from django.template import Context
from django.views.generic import TemplateView
from xhtml2pdf import pisa
from PyPDF2 import PdfFileMerger
from django.template.defaulttags import register

def index (request):

    searchform = SearchForm (request.GET)

    filters = {}

    if ('pk' in request.GET) and request.GET['pk'].strip():
        filters['pk'] = request.GET['pk']
    if ('nombre' in request.GET) and request.GET['solicitante'].strip():
        filters['nombre'] = request.GET['solicitante']
    if ('apellidop' in request.GET) and request.GET['beneficiario'].strip():
        filters['apellidop'] = request.GET['beneficiario']
    if ('apellidom'in request.GET) and request.GET ['fecha'].strip():
        filters['apellidom']= request.GET['fecha']
    if ('sexo' in request.GET)and request.GET['sexo'].strip():
        filters['sexo']= request.GET['sexo']
    if ('estadocivil' in request.GET) and request.GET['estadocivil'].strip():
        filters['estadocivil']= request.GET['estadocivil']
    if ('hijos' in request.GET)and request.GET['hijos'].strip():
        filters['hijos']= request.GET['hijos']
    if ('tipo_lic' in request.GET)and request.GET['tipo_lic'].strip():
        filters['tipo_lic']= request.GET['tipo_lic']
    if ('escolaridad' in request.GET)and request.GET['escolaridad'].strip():
        filters['escolaridad']= request.GET['escolaridad']
    #if ('destino' in request.GET) and request.GET['destino'].strip():
    #        destinos = Destino.objects.filter(destino_clave_municipio=request.GET['destino']).values_list('viaje_id', flat=True)
     #       filters['workflowactivity__id__in'] = destinos
    ##filtes ['solicitante__id__in']=

    empleado_list = empleado.objects.filter(**filters)

    if not bool(filters):
        empleado_list= empleado_list.order_by('-pk')##.exclude(status = 3)

    paginator = Paginator(empleado_list, 80)
    page = request.GET.get('page')

    try:
        emp = paginator.page(page)
    except PageNotAnInteger:
        emp = paginator.page(1)
    except EmptyPage:
        emp = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'emp':emp,
    })

    return render_to_response ('empleados.html', context)


def operadores (request):

    empleado_list= empleado.objects.filter(puesto_id = 10).order_by('-pk')##.exclude(status = 3)
    paginator = Paginator(empleado_list, 80)
    page = request.GET.get('page')
    try:
        emp = paginator.page(page)
    except PageNotAnInteger:
        emp = paginator.page(1)
    except EmptyPage:
        emp = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'emp':emp,
    })

    return render_to_response ('empleados_operadores.html', context)

@csrf_exempt
@login_required
def agregar(request):
    user = request.user
    profile = user.get_profile()

    if request.method=='POST':

	form = empleadoForm(request.POST)

        if form.is_valid():

           form = form.save(commit = False)

           form.status = 1 ## se establece por default el valor 1 que es activo.

           ingreso = form.save()

           messages.success(request, 'Se ha guardado el empleado')
           return HttpResponseRedirect (reverse('empleados.views.index'))

        else:
           
           context = RequestContext (request, {
                 'form':form,
                 'action':'Agregar',})

           return render_to_response ('empleados_add.html', context)
           messages.error(request, 'Ha ocurrido algun error, favor de revisar los datos. ')


    else:
        form = empleadoForm()
    context = RequestContext (request, {
        'form':empleadoForm,
        'action':'Agregar',
    })
    return render_to_response ('empleados_add.html', context)

@login_required

def editar (request, empleado_id):  ### Este modulo es para editar los empleados.
    empleados = get_object_or_404(empleado, pk=empleado_id)
    current_user = request.user
    
    if request.method=='POST':
        form = empleadoForm(request.POST, instance = empleados)

        if form.is_valid():
                    
                form.save()
                messages.success(request, 'Se ha editado el empleado')
        	return HttpResponseRedirect (reverse('empleados.views.index'))
        else:
            messages.error(request,'Ha ocurrido algun error, favor de revisar los datos.')
    else:
        form = empleadoForm(instance=empleados)
    context = RequestContext (request,{
        'form':form,
        'action':'Editar',
	'action2':'Cancelar',
    })
    return render_to_response ('empleados_add.html',context)




@csrf_exempt
@login_required
def solempleados(request):
    user = request.user
    profile = user.get_profile()
    print 'SOLICITUD DE EMPLEADOS..'

    if request.method=='POST':
        form = empleadoSolicitudForm(request.POST)
        print form


        print 'valido_ ' + str(form.is_valid())
        if form.is_valid():
           solicitante = form.save()
           messages.success(request, 'Continue ingresando sus datos...')
           return HttpResponseRedirect (reverse('empleados.views.secDocumentacion',kwargs={'idSolicitante':solicitante.pk}))

        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        form = empleadoSolicitudForm()

    context = RequestContext (request, {
        'form':form,
        'action':'Continuar',
    })
    return render_to_response ('empleadosSolicitud.html', context)

def secDocumentacion(request, idSolicitante):
    print 'documentacion..' + str(idSolicitante)

    if request.method=='POST':

        formDocumentacion = DocumentacionForm(request.POST)
        print formDocumentacion

        print 'valido_ ' + str(formDocumentacion.is_valid())

        formDocumentacion.cleaned_data['idsolicitante'] = idSolicitante
        if formDocumentacion.is_valid():

            #formDocumentacion.cleaned_data['idsolicitante'] = idSolicitante
            formDocumentacion.save()
            messages.success(request, 'Continue ingresando sus datos...')
            return HttpResponseRedirect (reverse('empleados.views.secHabitos',kwargs={'idSolicitante':idSolicitante}))

        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formDocumentacion = DocumentacionForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formDocumentacion':formDocumentacion,
        'action':'Continuar',
    })
    return render_to_response ('secDocumentacion.html', context)

def secHabitos(request, idSolicitante):
    print 'habitos..'

    if request.method=='POST':
        formSalhabForm = SalhabForm(request.POST)
        print formSalhabForm
        formSalhabForm.cleaned_data['idsolicitante'] = idSolicitante
        print formSalhabForm
        print 'valido_ ' + str(formSalhabForm.is_valid())
        if formSalhabForm.is_valid():
           formSalhabForm.save()
           messages.success(request, 'Continue ingresando sus datos...')
           return HttpResponseRedirect (reverse('empleados.views.secFamiliares',kwargs={'idSolicitante':idSolicitante}))
        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formSalhabForm = SalhabForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formSalhabForm': formSalhabForm,
        'action':'Continuar',
    })
    return render_to_response ('secHabitos.html', context)

def secFamiliares(request, idSolicitante):
    print 'familiares..'

    if request.method=='POST':
        formFamiliaresForm = FamiliaresForm(request.POST)
        print formFamiliaresForm
        formFamiliaresForm.cleaned_data['idsolicitante'] = idSolicitante
        print 'valido_ ' + str(formFamiliaresForm.is_valid())
        if formFamiliaresForm.is_valid():
           formFamiliaresForm.save()
           messages.success(request, 'Continue ingresando sus datos...')
           return HttpResponseRedirect (reverse('empleados.views.secEscolaridad',kwargs={'idSolicitante':idSolicitante}))
        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formFamiliaresForm = FamiliaresForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formFamiliaresForm': formFamiliaresForm,
        'action':'Continuar',
    })
    return render_to_response ('secFamiliares.html', context)

def secEscolaridad(request, idSolicitante):
    print 'secEscolaridad..'

    if request.method=='POST':
        formEscolaridadForm = EscolaridadForm(request.POST)
        print formEscolaridadForm
        formEscolaridadForm.cleaned_data['idsolicitante'] = idSolicitante
        print 'valido_ ' + str(formEscolaridadForm.is_valid())
        if formEscolaridadForm.is_valid():
           formEscolaridadForm.save()
           messages.success(request, 'Continue ingresando sus datos...')
           return HttpResponseRedirect (reverse('empleados.views.secConocimientos',kwargs={'idSolicitante':idSolicitante}))
        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formEscolaridadForm = EscolaridadForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formEscolaridadForm': formEscolaridadForm,
        'action':'Continuar',
    })
    return render_to_response ('secEscolaridad.html', context)


def secConocimientos(request, idSolicitante):
    print 'secConocimientos..'

    if request.method=='POST':
        formConocimientosForm = ConocimientosForm(request.POST)
        print formConocimientosForm
        formConocimientosForm.cleaned_data['idsolicitante'] = idSolicitante
        print 'valido_ ' + str(formConocimientosForm.is_valid())
        if formConocimientosForm.is_valid():
           formConocimientosForm.save()
           messages.success(request, 'Continue ingresando sus datos...')
           return HttpResponseRedirect (reverse('empleados.views.secEmpleos',kwargs={'idSolicitante':idSolicitante}))
        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formConocimientosForm = ConocimientosForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formConocimientosForm': formConocimientosForm,
        'action':'Continuar',
    })
    return render_to_response ('secConocimientos.html', context)

def secEmpleos(request, idSolicitante):
    print 'secEmpleos..'

    if request.method=='POST':
        formEmpleosForm = EmpleosForm(request.POST)
        print formEmpleosForm
        formEmpleosForm.cleaned_data['idsolicitante'] = idSolicitante
        print 'valido_ ' + str(formEmpleosForm.is_valid())
        if formEmpleosForm.is_valid():
           formEmpleosForm.save()
           messages.success(request, 'Continue ingresando sus datos...')
           return HttpResponseRedirect (reverse('empleados.views.secReferencias',kwargs={'idSolicitante':idSolicitante}))
        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formEmpleosForm = EmpleosForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formEmpleossForm': formEmpleosForm,
        'action':'Continuar',
    })
    return render_to_response ('secEmpleos.html', context)

def secReferencias(request, idSolicitante):
    print 'secReferencias..'

    if request.method=='POST':
        formReferenciasForm = ReferenciasForm(request.POST)
        print formReferenciasForm
        formReferenciasForm.cleaned_data['idsolicitante'] = idSolicitante
        print 'valido_ ' + str(formReferenciasForm.is_valid())
        if formReferenciasForm.is_valid():
           formReferenciasForm.save()
           messages.success(request, 'Continue ingresando sus datos...')
           return HttpResponseRedirect (reverse('empleados.views.secGenerales',kwargs={'idSolicitante':idSolicitante}))
        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formReferenciasForm = ReferenciasForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formReferenciasForm': formReferenciasForm,
        'action':'Continuar',
    })
    return render_to_response ('secReferencias.html', context)


def secGenerales(request, idSolicitante):
    print 'secGenerales..'

    if request.method=='POST':
        formGeneralesForm = GeneralesForm(request.POST)
        print formGeneralesForm
        formGeneralesForm.cleaned_data['idsolicitante'] = idSolicitante
        print 'valido_ ' + str(formGeneralesForm.is_valid())
        if formGeneralesForm.is_valid():
           formGeneralesForm.save()
           messages.success(request, 'Continue ingresando sus datos...')
           return HttpResponseRedirect (reverse('empleados.views.secEconomico',kwargs={'idSolicitante':idSolicitante}))
        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formGeneralesForm = GeneralesForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formGeneralesForm': formGeneralesForm,
        'action':'Continuar',
    })
    return render_to_response ('secGenerales.html', context)

def secEconomico(request, idSolicitante):
    print 'secEconomico..'

    if request.method=='POST':
        formEconomicoForm = EconomicoForm(request.POST)
        print formEconomicoForm
        formEconomicoForm.cleaned_data['idsolicitante'] = idSolicitante
        print 'valido_ ' + str(formEconomicoForm.is_valid())
        if formEconomicoForm.is_valid():
           formEconomicoForm.save()
           messages.success(request, 'Sus datos han sido registrados exitosamente, nosotros lo contacteremos..')
           messages.info(request, 'Por favor, responda el siguiente cuestionario.')
           return HttpResponseRedirect (reverse('empleados.views.index'))
        else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        formEconomicoForm = EconomicoForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
        'formEconomicoForm': formEconomicoForm,
        'action':'Continuar',
    })
    return render_to_response ('secEconomico.html', context)


@login_required
def documentosEmpleado(request, empleado_id):
    archivos = []
    if request.method == 'POST':
        #formDoc = ArchivosForm(initial={'idsolicitante':empleado_id})
        #archivo = Archivos.objects.get()
        formDoc = ArchivosForm(request.POST, request.FILES)

        print formDoc
        if formDoc.is_valid():
            
            print formDoc.cleaned_data['idsolicitante']
            print formDoc.cleaned_data['idDoc']
            print formDoc.cleaned_data['nombreDoc']
            nameFile = formDoc.cleaned_data['nombreDoc']
            try:
                tipoDoc = Catdoc.objects.get(nombreDoc = formDoc.cleaned_data['idDoc'])
                print tipoDoc.nombreDoc

                archivo = Archivos.objects.get(idsolicitante = formDoc.cleaned_data['idsolicitante'], idDoc = tipoDoc.pk)
                if archivo:
                    print 'eliminando archivo anterior' + str(archivo.nombreDoc)
                    ruta = settings.MEDIA_ROOT + str(archivo.nombreDoc)
                    os.remove(ruta)
                formDoc = ArchivosForm(request.POST, request.FILES, instance=archivo)
                formDoc.save()
                messages.success(request, u'Archivos actualizados exitosamente')
            except Exception:
                formDoc.save()
                messages.success(request, u'Archivos cargados exitosamente')


    else:
        formDoc = ArchivosForm(initial={'idsolicitante':empleado_id})



    #archivos = Archivos.objects.filter(idsolicitante =empleado.objects.get(pk=empleado_id))
    archivos = Archivos.objects.filter(idsolicitante =empleado_id)

    context = RequestContext(request,{
        'formDoc':formDoc,
        'action': 'Editar',
        'archivos': archivos,
        'empleadoId' : empleado_id
    })
    return render_to_response('empleados_doc.html', context)



def descargarDoc(request, nombreArchivo):
    ruta = settings.MEDIA_ROOT + str(nombreArchivo)
    print ruta
    wrapper = FileWrapper( open( ruta, "r" ) )
    content_type = mimetypes.guess_type( ruta )[0]

    response = HttpResponse(wrapper, content_type = content_type)
    response['Content-Length'] = os.path.getsize( ruta )
    response['Content-Disposition'] = 'attachment; filename=%s' % \
                                       smart_str( os.path.basename( ruta ) )

    return response


def borrarDoc(request, nombreArchivo, empleado_id):

    print 'Este es el id que envio del empleado : ' + empleado_id
    formDoc = ArchivosForm(initial={'idsolicitante':empleado_id})
    ruta = settings.MEDIA_ROOT + str(nombreArchivo)
    print 'Esta es la Ruta' + ruta
    print 'Este es el nombre del Archivo: ' + nombreArchivo
    archivo = get_object_or_404(Archivos, nombreDoc=nombreArchivo, idsolicitante =empleado_id)
    archivo.delete()
    os.remove(ruta)
    messages.success(request, u'Se elimino el archivo ' + nombreArchivo)
    archivos = Archivos.objects.filter(idsolicitante =empleado_id)


    context = RequestContext(request,{
        'formDoc':formDoc,
        'action': 'Editar',
        'archivos': archivos,
        'empleadoId' : empleado_id
    })
    return render_to_response('empleados_doc.html', context)

class credencialPdf(PDFTemplateView):

    template_name = "credencial.html"
    def get_context_data(self, pk, **kwargs):
        empleadoInfo = empleado.objects.get(clave=pk)
        return super(credencialPdf, self).get_context_data(
            pagesize="A4",
            title="Credencial de " + empleadoInfo.nombre,
            emp = empleadoInfo,
            **kwargs
        )



@login_required
def fotosEmpleado(request, empleado_id):
    print "llave=",empleado_id
    dat = get_object_or_404(empleado, pk=empleado_id)
    fotosFlag = 'visible'
    barrasFlag = 'visible'
    qrFlag = 'visible'
    if request.method == 'POST':
        formImagen = UploadForm(request.FILES)
        if formImagen.is_valid():
            formImagen.save()
            messages.success(request, 'Se ha guardado imagen ')
        else:
            messages.error(request, 'Ha ocurrido un error. Por favor verifique los datos.')
        formImagen = UploadForm(request.FILES)

        try:
            IMG1=str(request.FILES['imagen1'])
            cut_IMG1 = IMG1.split('.')
            extIMG1 = cut_IMG1[1]
            if extIMG1 !='jpg':
                messages.error(request, 'Error Foto 1: el archivo (%s) no es de extension .jpg '%request.FILES['imagen1'])
            else:

                if request.FILES['imagen1'] is not None or extIMG1=='jpj':
                    newdoc1 = Imagen(imagen1 = request.FILES['imagen1'],imagen2 ='imgEmpleados/default.jpg',imagen3 ='imgEmpleados/default.jpg',imagen4 = 'imgEmpleados/default.jpg')
                    newdoc1.nombre = empleado_id
                    newdoc1.save(formImagen)
                    newdoc1.delete()
                    messages.success(request, 'La Foto 1: (%s) se agrego correctamente '%request.FILES['imagen1'])



                    lista1 = os.listdir(settings.MEDIA_ROOT + 'imgEmpleados/')
                    for lis1 in lista1:
                        PARTE1 = str(lis1)
                        num1=500
                        if PARTE1 == str(request.FILES['imagen1']):
                            llave1 = str(empleado_id)
                            NUEVAPARTE1 = PARTE1.split('.')
                            newimg1=llave1+'_'+'FOTO.'+NUEVAPARTE1[1]
                            os.rename (settings.MEDIA_ROOT + 'imgEmpleados/%s'%PARTE1, settings.MEDIA_ROOT + 'imgEmpleados/%s'%newimg1)
                        num1 +=1
        except Exception:
            print "error foto 1"

        try:
            IMG2=str(request.FILES['imagen2'])
            cut_IMG2 = IMG2.split('.')
            extIMG2 = cut_IMG2[1]
            if extIMG2 !='jpg':
                messages.error(request, 'Error Foto 2: el archivo (%s) no es de extension .jpg '%request.FILES['imagen2'])
            else:

                if request.FILES['imagen2'] is not None or extIMG2=='jpj':
                    newdoc2 = Imagen(imagen1 ='imgEmpleados/default.jpg' ,imagen2 = request.FILES['imagen2'],imagen3 ='imgEmpleados/default.jpg',imagen4 = 'imgEmpleados/default.jpg')
                    newdoc2.nombre = empleado_id
                    newdoc2.save(formImagen)
                    newdoc2.delete()
                    messages.success(request, 'La Foto 2: (%s) se agrego correctamente '%request.FILES['imagen2'])
                    lista2 = os.listdir(settings.MEDIA_ROOT + 'imgEmpleados/')
                    for lis2 in lista2:
                        PARTE2 = str(lis2)
                        num2=1000
                        if PARTE2 == str(request.FILES['imagen2']):
                            llave2 = str(empleado_id)
                            NUEVAPARTE2 = PARTE2.split('.')
                            newimg2=llave2+'_'+'BARRAS.'+NUEVAPARTE2[1]
                            os.rename (settings.MEDIA_ROOT + 'imgEmpleados/%s'%PARTE2, settings.MEDIA_ROOT + 'imgEmpleados/%s'%newimg2)
                        num2 +=1
        except Exception:
            print "error foto 2"

        try:
            IMG3=str(request.FILES['imagen3'])
            cut_IMG3 = IMG3.split('.')
            extIMG3 = cut_IMG3[1]
            if extIMG3 !='jpg':
                messages.error(request, 'Error Foto 3: el archivo (%s) no es de extension .jpg '%request.FILES['imagen3'])
            else:
                if request.FILES['imagen3'] is not None or extIMG3=='jpj':
                    newdoc3 = Imagen(imagen1 = 'imgEmpleados/default.jpg',imagen2 ='imgEmpleados/default.jpg',imagen3 = request.FILES['imagen3'],imagen4 = 'imgEmpleados/default.jpg')
                    newdoc3.nombre = empleado_id
                    newdoc3.save(formImagen)
                    newdoc3.delete()
                    messages.success(request, 'La Foto 3: (%s) se agrego correctamente '%request.FILES['imagen3'])
                    lista3 = os.listdir(settings.MEDIA_ROOT + 'imgEmpleados/')
                    for lis3 in lista3:
                        PARTE3 = str(lis3)
                        num3=1500
                        if PARTE3 == str(request.FILES['imagen3']):
                            llave3 = str(empleado_id)
                            NUEVAPARTE3 = PARTE3.split('.')
                            newimg3=llave3+'_'+'QR.'+NUEVAPARTE3[1]
                            os.rename (settings.MEDIA_ROOT + 'imgEmpleados/%s'%PARTE3, settings.MEDIA_ROOT + 'imgEmpleados/%s'%newimg3)
                            num3 +=1
        except Exception:
            print "error foto 3"



    else:
        formImagen = UploadForm()
        if os.path.isfile(settings.MEDIA_ROOT + "imgEmpleados/" + str(empleado_id) + "_FOTO.jpg") is False:
            fotosFlag = 'hidden'

        if os.path.isfile(settings.MEDIA_ROOT + "imgEmpleados/" + str(empleado_id) + "_BARRAS.jpg") is False:
            barrasFlag = 'hidden'
        if os.path.isfile(settings.MEDIA_ROOT + "imgEmpleados/" + str(empleado_id) + "_QR.jpg") is False:
            qrFlag = 'hidden'





    context = RequestContext(request,{
        'empleadopk':empleado_id,
        'formImagen':formImagen,
        'nombre':dat,
        'action': 'Subir Archivos',
        'fotosFlag':fotosFlag,
        'barrasFlag':barrasFlag,
        'qrFlag':qrFlag,
    })
    return render_to_response('empleados_foto.html', context)


##### Docuemntos


def index_docs (request):
    searchform = SearchDocsForm (request.GET)
    CatDoc_list = Catdoc.objects.all()
    CatDoc_list= CatDoc_list.order_by('-pk')
    paginator = Paginator(CatDoc_list, 80)
    page = request.GET.get('page')
    try:
        empdoc = paginator.page(page)
    except PageNotAnInteger:
        empdoc = paginator.page(1)
    except EmptyPage:
        empdoc = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'empdoc':empdoc,
    })
    return render_to_response ('empdocumentos.html', context)

def documentos_add (request):
     user = request.user
     profile = user.get_profile()   
     if request.method == 'POST':         
         form = documentosForm(request.POST)
         if form.is_valid ():
             documento = form.save()
             messages.success(request, 'Documento registrado de forma exitosa')
             return HttpResponseRedirect (reverse('empleados.views.index_docs'))
         else:
             messages.error(request, 'El documento ya existe')
     else: 
         form = documentosForm()
     context = RequestContext (request, {
         'form': form,
         'action':'Agregar',
      })
     return render_to_response ('empdocumentos_form.html',context)

def docu_edit (request, catdoc_id):
     user = request.user
     profile = user.get_profile()
     documento = get_object_or_404(Catdoc, pk=catdoc_id)
     if request.method == 'POST':
        form = documentosForm(request.POST, instance = documento)
        if form.is_valid():
            doc = form.save()
            messages.success(request, 'Se ha editado el documento')
            return HttpResponseRedirect (reverse('empleados.views.index_docs'))
        else: 
            messages.error(request,'No se pudo editar el documento')
     else: 
         form = documentosForm(instance=documento)
     context = RequestContext (request, {
           'form': form,
           'action':'Editar',
      })
     return render_to_response ('empdocumentos_form.html', context)
@login_required
def docu_del (request, catdoc_id):
    documento = get_object_or_404(Catdoc, pk = catdoc_id)
    message = 'El documento %s ha sido borrado.' %documento.nombreDoc
    documento.delete()
    messages.success(request, message)
    return HttpResponseRedirect(reverse('empleados.views.index_docs',))
 
         
### Puestos


def index_p (request):

    searchform = SearchPuestosForm (request.GET)
    Puestos_list = Puestos.objects.all()
    Puestos_list= Puestos_list.order_by('-pk')
    paginator = Paginator(Puestos_list, 80)
    page = request.GET.get('page')
    try:
        puestos = paginator.page(page)
    except PageNotAnInteger:
        puestos = paginator.page(1)
    except EmptyPage:
        puestos = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'puestos':puestos,
    })
    return render_to_response ('emppuestos.html', context)

def puesto_add (request):

     user = request.user
     profile = user.get_profile()
   
     if request.method == 'POST':         
         form = puestoForm(request.POST)
         if form.is_valid ():
             puesto = form.save()
             messages.success(request, 'Puesto registrado de forma exitosa')
             return HttpResponseRedirect (reverse('empleados.views.index_p'))
         else:
             messages.error(request, 'No se pudo crear el Puesto favor de revisar los datos....')
     else: 
         form = puestoForm()
     context = RequestContext (request, {
         'form': form,
         'action':'Agregar',
      })
     return render_to_response ('emppuestos_form.html',context)


def puesto_edit (request, puestos_id):
     user = request.user
     profile = user.get_profile()
     puesto = get_object_or_404(Puestos, pk=puestos_id)
     if request.method == 'POST':
        form = puestoForm(request.POST, instance = puesto)
        if form.is_valid():
            puesto = form.save()
            messages.success(request, 'Se ha editado el Puesto')
            return HttpResponseRedirect (reverse('empleados.views.index_p'))
        else: 
            messages.error(request,'No se pudo editar el documento')
     else: 
         form = puestoForm(instance=puesto)
     context = RequestContext (request, {
           'form': form,
           'action':'Editar',
      })
     return render_to_response ('emppuestos_form.html', context)
@login_required

def puesto_del (request, puestos_id):
    puesto = get_object_or_404(Puestos, pk = puestos_id)
    message = 'El puesto %s ha sido borrado.' %puesto.nombre
    puesto.delete()
    messages.success(request, message)
    return HttpResponseRedirect(reverse('empleados.views.index_p',))

def movimiento_emp (request):

    if request.method == 'POST':

       form = MovEmpForm(request.POST)

       if form.is_valid():
             emp = request.POST['empleado']
             nuevoStatus = request.POST['tipo']
             empActual = empleado.objects.get(id = emp)
             empActual.status = nuevoStatus
             empActual.save()
             form.save()
   
             messages.success(request, 'Se ha registrado el movimiento')
             return HttpResponseRedirect (reverse('empleados.views.index'))
       else: 
             messages.error(request, 'No se ha regsitrado el movimiento, revise la informacion')
    else:
        form = MovEmpForm()
    context = RequestContext (request, {
            'form' : form, 
            'action' : 'Regsitrar',
})
    return render_to_response('movEmp.html', context)

@login_required
def generaPdfEmpleado (request, empleado_id):

    templateString = ("expedienteEmpleadoPdf.html")
    template = get_template(templateString)

    empleadoDatos = get_object_or_404(empleado, pk=empleado_id)

    form = empleadoDatos
    sexo = SEXO[empleadoDatos.sexo - 1]
    nacion = NACIONALIDAD[empleadoDatos.nacion - 1]
    estadocivil = CIVIL[empleadoDatos.estadocivil - 1]
    tipo_lic = TIPO_LIC[empleadoDatos.tipo_lic - 1]
    categoria = CATEGORIAS[empleadoDatos.categoria - 1]
    parentesco = PARENTESCOS[empleadoDatos.parentesco - 1]
    escolaridad = CAT_ESCOLARIDAD[empleadoDatos.escolaridad - 1]
    hijos = HIJOS[empleadoDatos.hijos]

    myContextObject = {
        'form': form,
        'empleadopk':empleadoDatos.pk,
        'sexo':sexo[1],
        'nacion':nacion[1],
        'estadocivil':estadocivil[1],
        'tipo_lic': tipo_lic[1],
        'categoria': categoria[1],
        'parentesco': parentesco[1],
        'escolaridad':escolaridad[1],
        'hijos':hijos[1],
    }

    html = template.render(Context(myContextObject))
    file = open(settings.MEDIA_ROOT + "documentosEmp/EmpleadoNo" + empleado_id + ".pdf", "w+b")
    links    = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8', link_callback=links)
    file.seek(0)
    pdf = file.read()
    file.close()

    archivos = Archivos.objects.all().filter(idsolicitante=empleado_id)
    merger = PdfFileMerger()
    merger.append(fileobj=open(settings.MEDIA_ROOT + "documentosEmp/EmpleadoNo" + empleado_id + ".pdf", "rb"))
    for arch in archivos:
        try:
            merger.append(fileobj=open(settings.MEDIA_ROOT + str(arch.nombreDoc), "rb"))
        except IOError:
            print('Archivo ' + str(arch.nombreDoc) + ', no encontrado')


    output = open(settings.MEDIA_ROOT + "documentosEmp/EmpleadoNo" + empleado_id + "_Expediente.pdf", "wb")
    merger.write(output)
    merger.close()

    pdfSal =  open(settings.MEDIA_ROOT + "documentosEmp/EmpleadoNo" + empleado_id + "_Expediente.pdf", "r")
    response = HttpResponse(pdfSal, mimetype="application/pdf")
    response["Content-Disposition"] = "attachment; filename=" + "EmpleadoNo" + empleado_id + "_Expediente.pdf"
    return response

def cuestionario(request, idSolicitante):
    print 'cuesId' + str(idSolicitante)
    if request.method == 'POST':
        form = InfoGralForm(request.POST)
        print form
        #form.cleaned_data['idsolicitante'] = idSolicitante
        print form
        print 'valido_ ' + str(form.is_valid())
        if form.is_valid():
            form.save()
            messages.success(request, 'Continue respondiendo el cuestionario...')
            return HttpResponseRedirect (reverse('empleados.views.cuestionario2',kwargs={'idSolicitante':idSolicitante}))
        else:
            messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        form = InfoGralForm(initial={'idsolicitante':idSolicitante})
        print 'Desde forma'
        #form = InfoGralForm()

    context = RequestContext (request, {
            'form':form,
            'action' : 'Continuar..',
    })

    return render_to_response('cuestionario1.html', context)

def cuestionario2(request, idSolicitante):

    hijosFormSet = modelformset_factory(infohijos, form=InfoHijosForm, max_num=5, extra=5, can_delete=True)

    if request.method == 'POST':
       form = CuestionarioForm(request.POST)
       formsetHijo = hijosFormSet(request.POST)
       print form
       form.cleaned_data['idsolicitante'] = idSolicitante
       print formsetHijo
       print 'valido_ ' + str(form.is_valid())
       print 'valido_ ' + str(formsetHijo.is_valid())
       if form.is_valid() and formsetHijo.is_valid():
           #form.cleaned_data['idsolicitante'] = idSolicitante
           form.save()
           formsetHijo.save()

           msg1 = 'Se ha creado una nueva solicitud de empleado numero: ' + idSolicitante + ' , favor de revisar en el modulo de "SOLICITUDES DE EMPLEO"\n\n'
           msg2 = '\n\n Contacto: \n\n  Departamento de Sistemas. '
           msg  = msg1 +  msg2  
           send_mail('Aviso de Nueva Solicitud: ', msg, 'controladministrativo@logisticavitesse.com.mx' , ['griselda@logisticavitesse.com.mx', 'genseg@hotmail.com'], fail_silently = True)## cambiar en productivo, fail_silently=False)

           messages.success(request, 'Gracias, ha finalizado el proceso.')
           return HttpResponseRedirect (reverse('empleados.views.solicitudeslista'))
       else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        precarga=[{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,}]
        hijosFormSet = hijosFormSet(initial=precarga, queryset=infohijos.objects.all().filter(idsolicitante=idSolicitante))
        form = CuestionarioForm(initial={'idsolicitante':idSolicitante})

    context = RequestContext (request, {
            'form':form,
            'hijosFormSet':hijosFormSet,
            'action' : 'Finalizar',
    })

    return render_to_response('Cuestionario2.html', context)


def solicitudEmpleo(request):

    if request.method == 'POST':
        form = solicitudForm(request.POST)
        print(form)
        #form.cleaned_data['estatus'] = 1
        #form.estatus = 1
        print(form.is_valid())

        if form.is_valid():
            soli = form.save()
            print soli.pk
            messages.success(request, 'Continue respondiendo la solicitud...')
            return HttpResponseRedirect (reverse('empleados.views.solicitudEmpleo2',kwargs={'idSolicitante':soli.pk}))
        else:
            messages.error(request, 'Por favor, verifique la informacion.')

    else:
        defaultEstatus = {'estatus':1}
        form = solicitudForm()

    context = RequestContext (request, {
            'form':form,
            'action' : 'Finalizar',
    })
    return render_to_response('solicitud.html', context)


def solicitudEmpleo2(request, idSolicitante):
    formset_familiares  = modelformset_factory(Familiares, form=FamiliaresForm, max_num=10, extra=5, can_delete=True)#, exclude=['idsolicitante'])
    formset_escolaridad = modelformset_factory(Escolaridad, form=EscolaridadForm, max_num=10, extra=5, can_delete=True)
    formset_empleos = modelformset_factory(Empleos, form=EmpleosForm, max_num=4, extra=4, can_delete=True)
    formset_referencia = modelformset_factory(Referencias, form=ReferenciasForm, max_num=4, extra=4, can_delete=True)

    if request.method == 'POST':
        familiaresForm = formset_familiares(request.POST)
        escolaridadForm = formset_escolaridad(request.POST)
        empleosForm = formset_empleos(request.POST)
        referenciaForm = formset_referencia(request.POST)
        print familiaresForm
        print '****************************************************************'
        print(escolaridadForm)
        print '****************************************************************'
        print(empleosForm)
        print '****************************************************************'
        print(referenciaForm)
        print '****************************************************************'
        print(familiaresForm.is_valid())
        print(escolaridadForm.is_valid())
        print(empleosForm.is_valid())
        print(referenciaForm.is_valid())
        if familiaresForm.is_valid() and escolaridadForm.is_valid() and empleosForm.is_valid() and referenciaForm.is_valid():
            familiaresForm.save()
            escolaridadForm .save()
            empleosForm.save()
            referenciaForm.save()
            messages.success(request, 'Continue respondiendo la solicitud...')
            return HttpResponseRedirect (reverse('empleados.views.cuestionario',kwargs={'idSolicitante':idSolicitante}))
        else:
            messages.error(request, 'Por favor, verifique la informacion.')

    else:
        solicitante=[{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},]
        formset_familiares = formset_familiares(initial=solicitante, queryset=Familiares.objects.all().filter(idsolicitante=idSolicitante))#queryset=Solicitud.objects.all().filter(idsolicitante=idSolicitante))
        formset_escolaridad = formset_escolaridad(initial=solicitante, queryset=Escolaridad.objects.all().filter(idsolicitante=idSolicitante))
        formset_empleos = formset_empleos(initial=solicitante, queryset=Empleos.objects.all().filter(idsolicitante=idSolicitante))
        formset_referencia = formset_referencia(initial=solicitante, queryset=Referencias.objects.all().filter(idsolicitante=idSolicitante))

    context = RequestContext (request, {
            'formset_familiares': formset_familiares,
            'formset_escolaridad':formset_escolaridad,
            'formset_empleos': formset_empleos,
            'formset_referencia':formset_referencia,
            'action' : 'Finalizar',
    })
    return render_to_response('solicitud2.html', context)


@login_required
def solicitudeslista(request):
    solicitudes_list = Solicitud.objects.filter(estatus = 1 )
    paginator = Paginator(solicitudes_list, 10)
    page = request.GET.get('page')

    try:
        solicitudes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        solicitudes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        solicitudes = paginator.page(paginator.num_pages)

    context = RequestContext(request,{
        'solicitudes': solicitudes,
        'estatus':ESTATUS
    })

    return render_to_response('listaSolicitudes.html', context)

def cambiarEstatus(request, idSolicitante, estatus):
    
    solicitud = Solicitud.objects.get(pk=idSolicitante)
    solicitud.estatus = estatus
    print 'este es el status' + str(estatus)
    if estatus == '4':
        cve=empleado.objects.all().order_by('-id')
        newid = str(cve[0].id+ 1)
        nclave = newid
        nnombre = solicitud.nombre
        print nclave
        print 'Este es el nombre:' + nnombre
        nSN= solicitud.segundoNombre  ### Posible error
        print 'Este es el segundo nombre :' + nSN
        nap= solicitud.paterno
        print nap
        nam= solicitud.materno
        print nam
        nsexo = solicitud.sexo
        nedad = solicitud.edad
        nnacion = solicitud.nacionalidad
        nec = solicitud.estadoCivil
        nln = solicitud.lugarNacimiento
        nce = 'Favor de Llenar los datos'
        ncet = 'Favor de llenar los datos'
        ncec = 'Favor de llenar los datos'
        snss = solicitud.nss  ### subir a 20 en empleados, actual en 12.
        nnss = snss[:12]
        nlicencia = solicitud.numLicencia
        ntipolic = 1
        ncurp = solicitud.curp
        nescolaridad = 8
        ncartilla = 'Desde Solicitud'
        nstatus = 9
        nfechanac = str(solicitud.fechaNacimiento)
        ncategoria = 6 
        nlicfecharef = '1980-01-01' ####puede ser causa de problema por el formato
        nparentesco = 9
        nceropalo = 0
        ncerrc = 0
        scalle = solicitud.domicilio ####solo tomar los primeros 30 caracteres
        ncalle = scalle[:30]
        nexterior = 'Solicitud'
        ninterior = 'Solicitud'
        scolonia = solicitud.colonia  ### solo tomar los primeros 30 caracteres
        ncolonia = scolonia[:29]
        print ncolonia
        nestado = 'Solicitud'
        ncp = solicitud.cp
        print ncp

        empleado.objects.create(nombre = nnombre, segundo_nombre = nSN, apellidop = nap, apellidom = nam, sexo = nsexo, edad = nedad, nacion = nnacion,
           estadocivil = nec, lugar_nacimiento = nln, contacto_emergencia_nom = nce, contacto_emergencia_tel = ncet, contacto_emergencia_cel = ncec, 
           nss = nnss, licencia = nlicencia, tipo_lic = ntipolic, escolaridad = nescolaridad, Cartilla = ncartilla, status = nstatus, fecha_nac = nfechanac,
           exterior =nexterior, interior = ninterior, colonia = ncolonia, estado = nestado, cp = ncp, clave = nclave, categoria = ncategoria, 
           lic_fecha_ref = nlicfecharef, parentesco = nparentesco, cer_opalo = nceropalo, cer_rc = ncerrc, calle = ncalle)
                
        msg1 = 'Se ha contratado el empleado ' + nnombre + ' ' + nap + ' ' + ' ' + nam +' favor completar el Registro\n\n'
        msg2 = 'En el modulo de Empleados '
        msg3 = '\n\n Contacto: \n\n  Departamento de Recursos Humanos. '
        msg  = msg1 +  msg2 + msg3 
        send_mail('Aviso de contratacion: ', msg, 'controladministrativo@logisticavitesse.com.mx' , ['griselda@logisticavitesse.com.mx', 'genseg@hotmail.com'], fail_silently = False)## cambiar en productivo, fail_silently=False)

        solicitud.save()
        messages.success(request, 'La solicitud tiene el nuevo estatus: ' + get_item(ESTATUS, int(estatus)) + ' , Favor de llenar los datos faltantes en el modulo de Empleados. Se ha enviado un correo a RH. ')
    elif estatus == '1':
        solicitud.save()
        messages.success(request, 'La solicitud tiene el nuevo estatus: ' + get_item(ESTATUS, int(estatus)) + ' , Por el momento el empleado queda como posible contratacion ')
    elif estatus == '3':
        solicitud.save()
        messages.error(request, 'La solicitud tiene el nuevo estatus: ' + get_item(ESTATUS, int(estatus)) + ' , La solicitud se he eliminado de la lista de candidatos ')
        
   # except Exception:
    else:
        messages.error(request, 'Error al realizar el cambio de estatus')
    return HttpResponseRedirect (reverse('empleados.views.solicitudeslista',))


def generarPdfSolicitud(request, idSolicitante):

    templateString = ("solicitudPdf.html")
    template = get_template(templateString)

    solicitudDatos = get_object_or_404(Solicitud, pk=idSolicitante)
    familiares = Familiares.objects.all().filter(idsolicitante=idSolicitante)
    referencias = Referencias.objects.all().filter(idsolicitante=idSolicitante)
    empleos = Empleos.objects.all().filter(idsolicitante=idSolicitante)
    escolaridad = Escolaridad.objects.all().filter(idsolicitante=idSolicitante)
    hijos = infohijos.objects.all().filter(idsolicitante=idSolicitante)
    cuestionarioDatos = get_object_or_404(Cuestionario, idsolicitante=idSolicitante)
    informacion = get_object_or_404(InfoGral, idsolicitante=idSolicitante)


    myContextObject = {
        'form': solicitudDatos,
        'viajar': get_item(OPCIONN, int(solicitudDatos.viajar)),
        'ingreso': get_item(OPCIONN, int(solicitudDatos.ingreso)),
        'casa': get_item(OPCIONN, int(solicitudDatos.casa)),
        'auto': get_item(OPCIONN, int(solicitudDatos.auto)),
        'conyuge': get_item(OPCIONN, int(solicitudDatos.conyuge)),
        'renta': get_item(OPCIONN, int(solicitudDatos.renta)),
        'deudas': get_item(OPCIONN, int(solicitudDatos.deudas)),
        'sindicato': get_item(OPCIONN, int(solicitudDatos.sindicato)),
        'familiaresT': get_item(OPCIONN, int(solicitudDatos.familiaresT)),
        'seguro': get_item(OPCIONN, int(solicitudDatos.seguro)),
        'afianzado': get_item(OPCIONN, int(solicitudDatos.afianzado)),
        'nacionalidad': get_item(NACIONALIDAD, int(solicitudDatos.nacionalidad)),
        'viveCon': get_item(VIVECON, int(solicitudDatos.viveCon)),
        'dependientes': get_item(DEPENDIENTES, int(solicitudDatos.dependientes)),
        'sexo': get_item(SEXO, int(solicitudDatos.sexo)),
        'estadoCivil': get_item(CIVIL, int(solicitudDatos.estadoCivil)),
        'salud': get_item(SALUD, int(solicitudDatos.salud)),
        'cronico': get_item(CRONICO, int(solicitudDatos.cronico)),
        'medio': get_item(CAT_MEDIO, int(solicitudDatos.medio)),
        'formset_familiares':familiares,
        'parentesco': PARENTESCO,
        'viveFinado': VF,
        'formset_escolaridad':escolaridad,
        'nivel': CAT_ESCOLARIDAD,
        'formset_empleos': empleos,
        'formset_referencia':referencias,
        'hijosFormSet': hijos,
        'formQ': informacion,
        'form2':cuestionarioDatos,
    }

    html = template.render(Context(myContextObject))
    file = open(settings.MEDIA_ROOT + "documentosEmp/SolicitudNo" + idSolicitante + ".pdf", "w+b")
    links    = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8', link_callback=links)
    file.seek(0)
    pdf = file.read()
    file.close()

    pdfSal =  open(settings.MEDIA_ROOT + "documentosEmp/SolicitudNo" + idSolicitante + ".pdf", "r")
    response = HttpResponse(pdfSal, mimetype="application/pdf")
    response["Content-Disposition"] = "attachment; filename=" + "SolicitudNo" + idSolicitante + "_Resumen.pdf"
    return response





@register.filter
def get_item(dictionary, key):
    key = int(key)
    dato = dictionary[key - 1]
    return dato[1]

@login_required
def validaArchivos(request,pk):
    empleadoInfo = empleado.objects.get(clave=pk)
    incompleto = False
    mensaje = ''
    if os.path.isfile(settings.MEDIA_ROOT + "imgEmpleados/" + str(empleadoInfo.pk) + "_FOTO.jpg") is False:
        mensaje = 'No existe la foto del empleado No. ' + pk
        messages.error(request, mensaje)
        incompleto = True
    print mensaje
    if os.path.isfile(settings.MEDIA_ROOT + "imgEmpleados/" + str(empleadoInfo.pk) + "_BARRAS.jpg") is False:
        mensaje = ' No existe el codigo de barras del empleado No. ' + pk
        messages.error(request, mensaje)
        incompleto = True
    if incompleto:
        return  HttpResponseRedirect(reverse('empleados.views.index'))
    else:
        return HttpResponseRedirect (reverse('credencial',kwargs={'pk':pk}))
