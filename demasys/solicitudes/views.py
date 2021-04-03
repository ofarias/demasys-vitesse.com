# coding=utf-8
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import permission_required, login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from solicitudes.models import Solicitudes, conceptos, TIPO_STATUS, FORMAS_D_PAGO, ArchivoPendiente
from solicitudes.forms import SolicitudForm, Sol_Edit_1_Form, Sol_Edit_2_Form,SearchForm, Sol_Edit_3_Form, Report_solForm, CAMPOS, Search_Form_Con, conceptos_form, reporteForm, archivoPendienteForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
from django.contrib.auth.models import Group
from django.db.models import Q

from django.db import connection, transaction
from django.http import QueryDict
####JC
import xlwt
from xlwt import Workbook,XFStyle,Borders, Pattern, Font, easyxf

from datetime import datetime
import time
import logging
import sys
from datetime import date, timedelta,datetime


from decimal import Decimal
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from easy_pdf.views import PDFTemplateView
from django.forms.models import modelformset_factory
from workflow.models import Workflow, WorkflowActivity, Participant, Role, Transition
from cuentas.models import Perfil
from django.contrib.auth.models import User
##from util import to_word

from cuentas.models import Perfil
from catalogos.models import Operador
from beneficiarios.models import Benefi
from viajes.models import CONCEPTO_GASTO, Gasto, Destino, Viaje
from sepomex.models import Sepomex
from contable.models import Area, Movimientos, Partidas
from django.db.models import Sum
from contable.views import saldoPartidaXArea
from catalogos.models import Economico
from inventario.models import Productos, Movimientos as Movimientos2
import MySQLdb

import json
from django.http import HttpResponse
from django.conf import settings

import sys, os
import mimetypes
from django.utils.encoding import smart_str
from django.core.servers.basehttp import FileWrapper


logger = logging.getLogger(__name__)

@login_required
def index(request):

    searchform = SearchForm(request.GET)
      
    filters = {}

    if ('pk' in request.GET) and request.GET['pk'].strip():
        filters['pk'] = request.GET['pk']
    if ('solicitante' in request.GET) and request.GET['solicitante'].strip():
        filters['solicitante'] = request.GET['solicitante']
    if ('beneficiario' in request.GET) and request.GET['beneficiario'].strip():
        filters['beneficiario__pk'] = request.GET['beneficiario']
    if ('fecha'in request.GET) and request.GET ['fecha'].strip():
        filters['fecha']= request.GET['fecha']
    if ('importe' in request.GET)and request.GET['importe'].strip():
        filters['importe']= request.GET['importe']
    if ('status' in request.GET) and request.GET['status'].strip():
        filters['status']= request.GET['status']
    if ('refer' in request.GET)and request.GET['refer'].strip():
        filters['refer']= request.GET['refer']
    if ('sol_bill' in request.GET)and request.GET['sol_bill'].strip():
        filters['sol_bill']= request.GET['sol_bill']
    if ('concepts' in request.GET)and request.GET['concepts'].strip():
        filters['concepts']= request.GET['concepts']
    if ('fecha_aut' in request.GET)and request.GET['fecha_aut'].strip():
        filters['fecha_aut']= request.GET['fecha_aut']
    if ('motivo_rech' in request.GET)and request.GET['motivo_rech'].strip():
        filters['motivo_rech']= request.GET['motivo_rech']
    if ('benef_otros' in request.GET)and request.GET['benef_otros'].strip():
        filters['benef_otros']= request.GET['benef_otros']
    #if ('cancelado' in request.GET) and request.GET['cancelado'].strip():
    #	filters['cancelado']= request.GET['cancelado']
    if ('destino' in request.GET) and request.GET['destino'].strip():
            destinos = Destino.objects.filter(destino_clave_municipio=request.GET['destino']).values_list('viaje_id', flat=True)
            filters['workflowactivity__id__in'] = destinos
    ##filtes ['solicitante__id__in']=

    solic_list = Solicitudes.objects.filter(**filters)        

    if not bool(filters):
        solic_list= solic_list.order_by('-pk').exclude(status = 5)
   
    paginator = Paginator(solic_list, 300)
    page = request.GET.get('page')

    try:
        solics = paginator.page(page)
    except PageNotAnInteger:
        solics = paginator.page(1)
    except EmptyPage:
        solics = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'solics':solics,
    })

    return render_to_response ('Solicitudes.html', context)

@csrf_exempt
@login_required


def index_pendientes(request):

    searchform = SearchForm(request.GET)
      
    filters = {}

    if ('pk' in request.GET) and request.GET['pk'].strip():
        filters['pk'] = request.GET['pk']
    if ('solicitante' in request.GET) and request.GET['solicitante'].strip():
        filters['solicitante'] = request.GET['solicitante']
    if ('beneficiario' in request.GET) and request.GET['beneficiario'].strip():
        filters['beneficiario__pk'] = request.GET['beneficiario']
    if ('fecha'in request.GET) and request.GET ['fecha'].strip():
        filters['fecha']= request.GET['fecha']
    if ('importe' in request.GET)and request.GET['importe'].strip():
        filters['importe']= request.GET['importe']
    if ('status' in request.GET) and request.GET['status'].strip():
        filters['status']= request.GET['status']
    if ('refer' in request.GET)and request.GET['refer'].strip():
        filters['refer']= request.GET['refer']
    if ('sol_bill' in request.GET)and request.GET['sol_bill'].strip():
        filters['sol_bill']= request.GET['sol_bill']
    if ('concepts' in request.GET)and request.GET['concepts'].strip():
        filters['concepts']= request.GET['concepts']
    if ('fecha_aut' in request.GET)and request.GET['fecha_aut'].strip():
        filters['fecha_aut']= request.GET['fecha_aut']
    if ('motivo_rech' in request.GET)and request.GET['motivo_rech'].strip():
        filters['motivo_rech']= request.GET['motivo_rech']
    if ('benef_otros' in request.GET)and request.GET['benef_otros'].strip():
        filters['benef_otros']= request.GET['benef_otros']
    #if ('cancelado' in request.GET) and request.GET['cancelado'].strip():
    #   filters['cancelado']= request.GET['cancelado']
    if ('destino' in request.GET) and request.GET['destino'].strip():
            destinos = Destino.objects.filter(destino_clave_municipio=request.GET['destino']).values_list('viaje_id', flat=True)
            filters['workflowactivity__id__in'] = destinos
    ##filtes ['solicitante__id__in']=

    solic_list = Solicitudes.objects.filter(**filters)        

    if not bool(filters):
        solic_list= solic_list.filter(status= 1).order_by('-pk')

    paginator = Paginator(solic_list, 300)
    page = request.GET.get('page')

    try:
        solics = paginator.page(page)
    except PageNotAnInteger:
        solics = paginator.page(1)
    except EmptyPage:
        solics = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'solics':solics,
    })

    return render_to_response ('Solicitudes_pendientes.html', context)

@csrf_exempt
@login_required
def agregar(request):

    userid = request.user.id  ### obtengo el id del usurio 
    user = request.user    ### obtengo el usuario
    profile = user.get_profile()  ### obtengo el nombre completo del usuario
    u1 = Perfil.objects.get(user_id = userid)  ## Obtengo el user_id en base al id del usurio
    Hoy = date.today()
   
    if request.method=='POST':
        form = SolicitudForm(request.POST)

        vencimiento = date.today()+timedelta(days= 7)
        print 'Este es el vencimiento'
        print vencimiento

        if form.is_valid():
            conc = request.POST['concepts']
            CONC= len(conc)
            #kmm = request.POST['kilometraje']
            #km = kmm.isdigit()
            prod = request.POST['producto']
            unidades = request.POST['unidades']


            VlEco = request.POST['id_unidad']
            valorEconomico = len(VlEco)
            VlCaP = request.POST['sol_bill']
            valorCartaPorte = len(VlCaP)
            n=request.POST['kilometraje']
            print n
            kilo = 0
            if len(n) > 0:
                kilo += float(n)

            if CONC > 0:
                checaVal = conceptos.objects.all().filter(id=conc)
                ecoFlag = True
                porteFlag = True
                conProd = False
                if checaVal[0].economico and valorEconomico == 0:
                    messages.warning(request, 'El concepto %s, requiere seleccione un Economico' % checaVal[0].nombre_conc)
                    ecoFlag = False
                if checaVal[0].economico and kilo < 1:
                    messages.warning(request, 'Kilometraje debe ser mayor a 0')
                    ecoFlag = False
                if checaVal[0].carta_porte and valorCartaPorte == 0:
                    messages.warning(request, 'El concepto %s, requiere seleccione una CartaPorte' % checaVal[0].nombre_conc)
                    porteFlag = False

                uKilo = 0
                kserv= 0
                if (checaVal[0].economico and ecoFlag) or (checaVal[0].carta_porte and porteFlag):
                    economico = get_object_or_404(Economico, pk=VlEco)
                    kserv= economico.kilometrajeServicio
                    print 'valor del km Servicio:' + str(kserv)
                    uKilo = economico.ultimoKilometraje
                    print 'valor del km ultimo' + str(uKilo)

                if prod:
                    conProd = True

                if kilo < uKilo:
                    messages.warning(request, 'El kilometraje no puede ser menor al último kilometraje registrado anteriomente.')
                elif prod  and float(unidades) < 0.01:
                    messages.warning(request, 'La unidad del producto debe ser mayor a cero.')
                elif ecoFlag and porteFlag:
                    messages.success(request, 'La solicitud se ha registrado correctamente.')

                    solic = form.save(commit = False)
                    solic.fecha = Hoy
                    solic.fecha_vencimiento = vencimiento
		    solic.solicitante_id = u1.id##userid
		    solic = form.save()


                    if conProd:

                        unidad = Economico.objects.get(pk=VlEco)

                        movimientos = Movimientos2()
                        movimientos.idEconomico = unidad
                        movimientos.idSolicitud = solic.pk
                        movimientos.unidades = Decimal(unidades)
                        movimientos.movimiento = 'S'
                        producto = Productos.objects.get(pk = prod)

                        producto.existencia = producto.existencia - Decimal(movimientos.unidades)
                        producto.save()
                        movimientos.idProducto = producto
                        movimientos.save()

                    if kilo > uKilo and kilo < (kserv + uKilo):
                        restaK = (kserv + uKilo) - kilo
                        sresta = str(restaK)
                        unicode_str = sresta.decode('ascii')
                        utf8_str = unicode_str.encode('utf-8')

                        messages.warning(request, 'La unidad No. %s, requiere servicio en los proximos %s kilometros' % (VlEco, restaK))
                    if kilo > (kserv + uKilo):
                        messages.warning(request, 'La unidad No. %s, requiere servicio inmediatamente' % VlEco)


                    return HttpResponseRedirect (reverse ('solicitudes.views.index'))
                #else:
                context = RequestContext (request, {
                'form':form,
                'action':'Agregar',})
                return render_to_response ('Solicitudes_add.html', context)
            else:
                messages.warning(request, 'Seleccione un concepto')

        else:
            context = RequestContext (request, {
                    'form':form,
                    'action':'Agregar',})
            return render_to_response ('Solicitudes_add.html', context)
            messages.error(request, 'Ha ocurrido algun error, favor de revisar los datos. ')


    else:
        form = SolicitudForm()
    context = RequestContext (request, {
        'form':SolicitudForm,
        'today':Hoy,
        'action':'Agregar',
    })
    return render_to_response ('Solicitudes_add.html', context)

@login_required
def edit (request, solicitudes_id):  ### este modulo es para editar las solicitudes o cancelarlas.
    solicitudes = get_object_or_404(Solicitudes, pk=solicitudes_id)
    current_user = request.user
    valor = solicitudes.status
       

    if request.method=='POST':
        form = SolicitudForm(request.POST, instance = solicitudes)
	
        if form.is_valid():
            if valor != 1:
                render_to_response ('Solicitudes_edit.html', {'form':form})
                messages.error(request, 'Solo se pueden editar Solicitudes pendientes, favor de revisar')
            else:
                form=form.save(commit = False)
                ##form.status = 1
                form.save()
                messages.success(request, 'La solicitud se ha editado o cancelado')
            return HttpResponseRedirect (reverse('solicitudes.views.index'))
        else:
            messages.error(request,'Ha ocurrido algun error, favor de revisar los datos.')
    else:
        form = SolicitudForm(instance=solicitudes)
    context = RequestContext (request,{
        'form':form,
        'action':'Editar',
	'action2':'Cancelar',
    })
    return render_to_response ('Solicitudes_add.html',context)

@login_required
def autorizar(request, solicitudes_id):

    Hoy = date.today()
    Solicitudes.objects.filter(pk=solicitudes_id).update(status= 2, fecha_aut = Hoy)
    messages.success(request, 'Se ha autorizado la solicitud %s' %solicitudes_id)
    return redirect(index_pendientes)

@login_required
def editar(request, solicitudes_id):### Este modulo es para autorizar.
    solicitudes = get_object_or_404(Solicitudes, pk=solicitudes_id)
    current_user = request.user
    valor = solicitudes.status
   
    if request.method == 'POST':
        form = Sol_Edit_1_Form(request.POST, instance=solicitudes)
        
        if form.is_valid():
            if valor != 1:## or current_user != 'Alejandro':
                render_to_response('Solicitudes_edit.html', {'form':form})
                messages.error(request,'Solo se pueden Autorizar solicitudes Pendientes')
            else:
                form=form.save(commit = False)
                #form.status = 2
                form.save()
                messages.success(request,'Se ha Aprovado / Rechazado la solicitud')
            return HttpResponseRedirect(reverse('solicitudes.views.index'))

        else:
            render_to_response('Solicitudes_edit.html', {'form': form})
            messages.error(request,'La solicitud no se pudo Aprovar / Rechazar, favor de revisar.')
    else:
        form = Sol_Edit_1_Form(instance=solicitudes)
    
    context = RequestContext (request,{
        'form':form,
        'action':'Autorizar',
    })

    return render_to_response('Solicitudes_edit.html', context)
   
@login_required
def asignar (request, solicitudes_id):

    solicitudes = get_object_or_404(Solicitudes, pk=solicitudes_id)
    ctxBan = ''
    ctxCta = ''
    valor = solicitudes.status
    vencimiento=date.today()+timedelta(days=7)

    if request.method == 'POST':
        form = Sol_Edit_2_Form(request.POST, instance=solicitudes)
        current_user = request.user
        if form.is_valid():
            ##valor = form.cleaned_data['status']
            if valor != 2 :## or valor is 'Pagado':###
                render_to_response('Solicitudes_edit2.html',{'form':form})
                messages.error(request,'Solo se pueden Pagar solicitudes Aprobadas.')
            else:
                idPartida = form.cleaned_data['partida']
                idArea = form.cleaned_data['areas']
                monto = form.cleaned_data['importe_asig']
                fecha = form.cleaned_data['fecha_asig']
                viajeRef = form.cleaned_data['sol_bill']	  
            	#benefi_otro = Benefi.objects.filter(pk=idBenefi)
		### agregar el concepto al movimiento contable
		#viajeRef = solicitudes.sol_bill
                via=str(viajeRef)
            	numconc = solicitudes.concepts_id
		print numconc
		concepts = conceptos.objects.filter(id = numconc)### Conceptos 
		print 'Filtra el concepto'
		for conc in concepts:
                  nomconc = conc.nombre_conc
		#print nomconc
                print type (via)
                print via
		## finaliza el obtener el concepto
                form = form.save(commit = False)
                form.fecha_vencimiento = vencimiento
                if via:
                    print 'entra al if '
		    via = 0

		else:

                    via = via
	        print via
                saldo_partida_actual = saldoPartidaXArea(idPartida.id, idArea.id)
                movimiento = Movimientos(idPartida=Partidas.objects.get(id = idPartida.id),
                                         idArea = Area.objects.get(id = idArea.id),
                                         id_auth_user=current_user,
                                         importe=monto, tipo='C', ref_viaje = via,
                                         fecha=fecha, ref_solicitud = solicitudes.pk, montoPartida = saldo_partida_actual, concepto = nomconc)


                    
                movimiento.save()

		form.status = 4
		form.save()
                messages.success(request,'Se ha asignado la solicitud')
                return HttpResponseRedirect(reverse('solicitudes.views.index'))
        else:
            render_to_response('Solicitudes_edit2.html',{'form':form})
            messages.error(request,'He ocurrido algun error, favor de verificar los datos.')

    else:
        form = Sol_Edit_2_Form(instance=solicitudes)

        try:
            #print solicitudes.pk
            idBenefi = solicitudes.benef_otros.id
            beneficiarioBase = get_object_or_404(Benefi,  pk=idBenefi)
            ctxBan = beneficiarioBase.ban
            ctxCta = beneficiarioBase.no_cta
        except Exception:
            print 'No tiene beneficiario'


    saltoTotal = 100000

    pila = []
    pilaO = []
    for x in range(1,5):
        sal = Movimientos.objects.filter(tipo ='A', idPartida = x, idArea = 2).aggregate(importe__sum = Sum('importe'))
        abonoEfectivoC = sal['importe__sum']
        print abonoEfectivoC
        if abonoEfectivoC is None:
            abonoEfectivoC = 0
        cargoE = Movimientos.objects.filter(tipo ='C', idPartida = x, idArea = 2).aggregate(importe__sum = Sum('importe'))
        cargoEfectivo = cargoE['importe__sum']
        print cargoEfectivo
        if cargoEfectivo is None:
            cargoEfectivo = 0
        saldoC = abonoEfectivoC - cargoEfectivo
        print saldoC
        pila.append(saldoC)

        salO = Movimientos.objects.filter(tipo ='A', idPartida = x, idArea = 3).aggregate(importe__sum = Sum('importe'))
        abonoEfectivoO = salO['importe__sum']
        print abonoEfectivoO
        if abonoEfectivoO is None:
            abonoEfectivoO = 0
        cargoEO = Movimientos.objects.filter(tipo ='C', idPartida = x, idArea = 3).aggregate(importe__sum = Sum('importe'))
        cargoEfectivoO = cargoEO['importe__sum']
        print cargoEfectivoO
        if cargoEfectivoO is None:
            cargoEfectivoO = 0
        saldoO = abonoEfectivoO - cargoEfectivoO
        print saldoO
        pilaO.append(saldoO)

    saldoTransferencia = pila.pop()
    pila.pop()
    saldoVale = pila.pop()
    saldoEfectivo = pila.pop()

    saldoTO = pilaO.pop()
    pilaO.pop()
    saldoVO = pilaO.pop()
    saldoEO = pilaO.pop()

    for s in Solicitudes.objects.exclude(importe_asig=None).exclude(forma_pago=1).exclude(forma_pago=3):
        saltoTotal -= s.importe_asig


    context = RequestContext (request,{
        'form':form,
        'action':'Asignar',
        'saldoTotal':saltoTotal,
        'saldoEfectivo':saldoEfectivo,
        'saldoVale':saldoVale,
        'saldoTransferencia':saldoTransferencia,
        'saldoEO':saldoEO,
        'saldoVO':saldoVO,
        'saldoTO':saldoTO,
        'bancoVal': ctxBan,
        'cuentaVal': ctxCta,
    })

    return render_to_response ('Solicitudes_edit2.html', context)



@login_required
def cancelar_index (request):

    searchform = SearchForm(request.GET)
    filters = {}

    if  ('pk' in request.GET) and request.GET['pk'].strip():
        filters['__pk'] = request.GET['pk']
    if ('solicitante' in request.GET) and request.GET['solicitante'].strip():
        filters['solicitante'] = request.GET['solicitante']
    if ('beneficiario' in request.GET) and request.GET['beneficiario'].strip():
        filters['beneficiario__pk'] = request.GET['beneficiario']
    if ('fecha'in request.GET) and request.GET ['fecha'].strip():
        filters['fecha']= request.GET['fecha']
    if ('importe' in request.GET)and request.GET['importe'].strip():
        filters['importe']= request.GET['importe']
    if ('status' in request.GET)and request.GET['status'].strip():
        filters['status']= request.GET['status']
    ##filtes ['solicitante__id__in']=

    solic_list = Solicitudes.objects.filter(**filters)

    if not bool(filters):
        solic_list= solic_list.order_by('-pk')

    #solic_list = Solicitudes.objects.all()
    paginator = Paginator(solic_list, 10)
    page = request.GET.get('page')

    try:
        solics = paginator.page(page)
    except PageNotAnInteger:
        solics = paginator.page(1)
    except EmptyPage:
        solics = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'solics':solics,
    })

    return render_to_response ('Sol_cancel.html', context)
@login_required
def cancelar (request, solicitudes_id):

    solicitudes = get_object_or_404(Solicitudes, pk=solicitudes_id)

    if request.method == 'POST':
        form = Sol_Edit_3_Form(request.POST, instance=solicitudes)

        if form.is_valid():
            form.save()
            messages.success(request,'La solicitud se marco como cancelada, recuerda que esta operacion no afecta el saldo')
            return HttpResponseRedirect(reverse('solicitudes.views.cancelar_index'))
        else:
            render_to_response('Soliciudes_cancel.html',{'form':form})
            messages.error(request,'He ocurrido algun error...')

    else:
        form = Sol_Edit_3_Form(instance=solicitudes)

    context = RequestContext (request,{
        'form':form,
        'action':'Guardar',
    })

    return render_to_response ('Solicitudes_cancel.html', context)


def reporte_sol(request):

    searchform = Report_solForm()

    context = RequestContext(request,{
    'searchform': searchform
    })

    return render_to_response('reporte_sol.html', context)

@csrf_exempt
def reportesresults(request):

    #if request.method != 'POST':
    campos = []
    searchform = Report_solForm(request.POST)

    if searchform.is_valid():
        campos = searchform.cleaned_data['campos']


    filters = {}
    if ('pk' in request.POST) and request.POST['pk'].strip():
        filters['pk'] = request.POST['pk']
    if ('solicitante' in request.POST) and request.POST['solicitante'].strip():
        filters['solicitante'] = request.POST['solicitante']
    if ('beneficiario' in request.POST) and request.POST['beneficiario'].strip():
        filters['beneficiario'] = request.POST['beneficiario']
    if ('fecha'in request.POST) and request.POST ['fecha'].strip():
        filters['fecha']= request.POST['fecha']
    if ('importe' in request.POST)and request.POST['importe'].strip():
        filters['importe']= request.POST['importe']
    if ('status' in request.POST)and request.POST['status'].strip():
        filters['status']= request.POST['status']
    if ('refer' in request.POST)and request.POST['refer'].strip():
        filters['refer']= request.POST['refer']
    if ('sol_bill' in request.POST)and request.POST['sol_bill'].strip():
        filters['sol_bill']= request.POST['sol_bill']
    if ('concepto' in request.POST)and request.POST['concepto'].strip():
        filters['concepto']= request.POST['concepto']
    if ('fecha_aut' in request.POST)and request.POST['fecha_aut'].strip():
        filters['fecha_aut']= request.POST['fecha_aut']
    if ('motivo_rech' in request.POST)and request.POST['motivo_rech'].strip():
        filters['motivo_rech']= request.POST['motivo_rech']



    solic = Solicitudes.objects.filter(**filters)
    context = RequestContext(request,{
        'solics': solics,
        'campos': campos,
        'action': 'Editar',
    })

    return render_to_response('results.html', context)

@csrf_exempt
@login_required
def reportsexcel(request):
    response = HttpResponse(mimetype="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=reporte.xls'

    campos = []
    searchform = Report_solForm(request.POST)
    if searchform.is_valid():
        campos = searchform.cleaned_data['campos']


    inicial = None
    final = None
    filters = {}
    if ('pk') in request.POST and request.POST['pk'].strip():
        filters['pk'] = request.POST['pk']
    if ('solicitante' in request.POST) and request.POST['solicitante'].strip():
        filters['solicitante'] = request.POST['solicitante']
    if ('operador' in request.POST) and request.POST['operador'].strip():
        filters['beneficiario'] = request.POST['operador']
    if ('benef_otros' in request.POST) and request.POST['benef_otros'].strip():
        filters['benef_otros'] = request.POST['benef_otros']
    if ('fecha_from'in request.POST) and request.POST ['fecha_from'].strip():
        #filters['fecha']= request.POST['fecha_from']
        inicial = request.POST['fecha_from']
    if ('fecha_to'in request.POST) and request.POST ['fecha_to'].strip():
        #filters['fecha']= request.POST['fecha_to']
        final = request.POST['fecha_to']
    if ('status' in request.POST)and request.POST['status'].strip():
        filters['status']= request.POST['status']
    if ('concepts' in request.POST)and request.POST['concepts'].strip():
        filters['concepts']= request.POST['concepts']
    if ('forma_pago' in request.POST)and request.POST['forma_pago'].strip():
        filters['forma_pago']= request.POST['forma_pago']
    if ('sol_bill' in request.POST)and request.POST['sol_bill'].strip():
        filters['sol_bill']= request.POST['sol_bill']

    if inicial and final:
        filters['fecha__range'] = (inicial, final)

    solics = Solicitudes.objects.filter(**filters)


    if solics.count():
        wb = xlwt.Workbook()
        ws = wb.add_sheet('Reporte')

        date_format = xlwt.XFStyle()
        date_format.num_format_str = 'dd/mm/yyyy'

        columna = 0
        for campo in campos:
            ws.write(1, columna, dict(CAMPOS)[campo])
            columna += 1

        primitive = [int, str, bool, long, Decimal]
        fechaXls = False

        renglon = 2
        for solic in solics:
            columna = 0
            for campo in campos:

                #print 'campoRaw ' + str(campo)
                if campo == 'fecha_asig' or campo == 'fecha_aut' or campo == 'fecha_canc' or campo == 'fecha':
                    fechaXls = True

                campo = multi_getattr(solic,campo)## Esto es para el filtrado ....campo.replace("__", ".")
                ##campo = campo.split("__")
                ##value = multi_getattr(solic,campo) ###value = multi_getattr(solic,campo[1])
                if type(campo) not in primitive:
                    try:
                        campo = campo.__unicode__()
                    except AttributeError:
                        campo = campo
                #print 'campoRaw ' + str(campo)

                if fechaXls:
                    ws.write(renglon, columna, campo, date_format)
                else:
                    ws.write(renglon, columna, campo)# value)
                columna += 1
                fechaXls = False
            renglon += 1

        wb.save(response)
        return response
    else:
        return HttpResponse ('No se encontraron registros---')

def multi_getattr(obj, attr, default = None):
    """
    Get a named attribute from an object; multi_getattr(x, 'a.b.c.d') is
    equivalent to x.a.b.c.d. When a default argument is given, it is
    returned when any attribute in the chain doesn't exist; without
    it, an exception is raised when a missing attribute is encountered.

    """
    attributes = attr.split(".")
    for i in attributes:
        try:
            #print 'campo ' + i
            if i == 'solicitante_id':
                obj = obj.solicitante.user.get_full_name()
            elif i == 'beneficiario_id':
                obj = obj.beneficiario. __unicode__()
            elif i == 'benef_otros_id':
                obj = obj.benef_otros.__unicode__()
            elif i == 'concepts_id':
                obj = obj.concepts.__unicode__()
            elif i == 'status':
                obj = TIPO_STATUS[obj.status-1]
                obj = obj[1]
            elif i == 'forma_pago':
                obj = FORMAS_D_PAGO[obj.forma_pago-1]
                obj = obj[1]
            elif i == 'sol_bill':
                obj = obj.sol_bill.pk
            else:
                obj = getattr(obj, i)

        except (AttributeError, Exception):
                return default
                #if default:
                #    return default
                #else:
                #    raise

    return obj

def index_con (request):

    searchform = Search_Form_Con (request.GET)
    filters = {}

    if ('nombre_conc' in request.GET) and request.GET ['nombre_conc'].strip():
        filters['nombre_conc']=request.GET['nombre_conc']

    concepto_list = conceptos.objects.filter(**filters)

    if not bool (filters):
        concepto_list = concepto_list.order_by('nombre_conc')

    paginator = Paginator(concepto_list, 10)
    page = request.GET.get('page')

    try:
        concepto = paginator.page(page)
    except PageNotAnInteger:
        concepto = paginator.page(1)
    except EmptyPage:
        concepto = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'concepto':concepto,
    })

    return render_to_response ('Solconceptos.html', context)

##########JC
def agregar_con (request):
    if request.method == 'POST':
        form = conceptos_form(request.POST)
        if form.is_valid():
            ingreso = form.save()
            messages.success(request, 'Se ha agregado el concepto')
            return HttpResponseRedirect (reverse('solicitudes.views.index_con'))
        else:
            messages.error(request, 'Ha ocurrido algun error al dar de alta el registro')
    else:
        form = conceptos_form()
    context = RequestContext(request, {
        'form':conceptos_form,
        'action':'Agregar'
    })
    return render_to_response ('solconceptos_add.html', context)


def editar_con (request, Conceptos_id):
    Conceptos = get_object_or_404(conceptos, pk=Conceptos_id)
    current_user = request.user

    if request.method == 'POST':
        form = conceptos_form(request.POST, instance=Conceptos)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado correctamente el concepto')
            return HttpResponseRedirect(reverse('solicitudes.views.index_con'))
        else:
            render_to_response('solconceptos_edit.html',{'form':form})
            messages.error(request,'Ha ocurrido algun error, favor de revisar sus datos.')
    else:
        form = conceptos_form(instance=Conceptos)
    context = RequestContext (request,{
        'form':form,
        'action':'Editar',
    })

    return render_to_response ('solconceptos_edit.html',context)

@csrf_exempt
def cuenta_banco(request):
    if request.method == 'POST':
        response_data = {}
        idBenefi = request.POST.get('pk')
        try:
            benefi_otro = Benefi.objects.filter(pk=idBenefi)
            for res in benefi_otro:
                response_data['bancoVal'] = res.ban
                response_data['cuentaVal'] = res.no_cta
        except ValueError:
            print 'no existen datos'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )


def reporteGastos(request):
    print 'click'
    form = reporteForm(request.POST)
    return render(request,'reporteGastos.html', {'form': form,})

@csrf_exempt
@login_required
def generaReporte(request):
    print 'Generando...'

    filters = {}
    filtersViaje = {}
    inicial = None
    final = None
    gastosViaje = None
    if ('id_viaje') in request.POST and request.POST['id_viaje'].strip():
        filters['sol_bill'] = request.POST['id_viaje']
        filtersViaje['pk'] = request.POST['id_viaje']
    if ('operador') in request.POST and request.POST['operador'].strip():
        filters['beneficiario'] = request.POST['operador']
        filtersViaje['operador'] = request.POST['operador']
    if ('fecha_from') in request.POST and request.POST['fecha_from'].strip():
        inicial = request.POST['fecha_from']
    if ('fecha_to') in request.POST and request.POST['fecha_to'].strip():
        final = request.POST['fecha_to']


    response = HttpResponse(mimetype="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=reporte.xls'

    if inicial and final:
        filters['fecha_asig__range'] = (inicial, final)
        filtersViaje['fecha_salida__range'] = (inicial, final)
    elif inicial or final:
        messages.error(request, 'Seleccione completo rango de fechas.')
        form = reporteForm(request.POST)
        return render(request,'reporteGastos.html', {'form': form,})

    if not len(filters):
        messages.error(request, 'Seleccione por lo menos un filtro o un rango de fechas')
        form = reporteForm(request.POST)
        return render(request,'reporteGastos.html', {'form': form,})


    ## solicitudes = Solicitudes.objects.filter(**filters)
    viajes = Viaje.objects.filter(**filtersViaje)
    #solicitudes = Solicitudes.objects.filter(sol_bill=5553)
    wb = xlwt.Workbook(encoding='utf8')
    ws = wb.add_sheet('Reporte')
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/mm/yyyy'
    formatoNum = XFStyle()
    formatoNum.num_format_str = '$#,##0.00'
    font = xlwt.Font() # Crear Font
    font.name = 'Arial'
    font.height = 20 * 12  #22pt
    font.bold = True
    font.italic = True
    style = xlwt.XFStyle() # Crar Style
    style = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue;') #background color
    style.font = font # Aplicar Font al Style
    ws.write_merge(0, 0, 0, 15, r'Control de Asignación de Gastos', style)
    columnas = [
            (r'Fecha de Salida', 15),
            (u"Carta Porte", 70),
            (u"Cliente.", 70),
            (u"Departamento", 70),
            (u"Concepto Gasto", 70),
            (u"Importe Gasto",70),
            (u"Factura", 70),
            (u"Fecha Pago", 70),
            (u"Facturacion Flete", 70),
            (u"Facturacion Casetas", 70),
            (u"Fact. Maniobras Locales", 80), 
            (u"Fact. Maniobras Foraneas", 80 ),
            (u"Facturacion Subtotal", 70),
            (u"Facturacion IVA", 70),
            (u"Facturacion Retenciones", 70),
            (u"Facturacion Total",70),
    ]

    posx = 0
    for col in xrange(len(columnas)):
        ws.write(1, posx, columnas[col][0])
        posx += 1

    renglon=2


    if viajes.count():
        for viajeD in viajes:
            v= viajeD.id
            print str(v)
            movimientos = Movimientos.objects.filter(ref_viaje= v)
            for mov in movimientos:
                idmov = mov.id
                print idmov
                try:
                    #print '>>> ' + str(solic.pk)
                    #print '>>> ' + str(solic.sol_bill.pk)
                    #sollbil =  multi_getattr(solic,'sol_bill')
                    #ws.write(renglon, 1, viajeD.operador.__unicode__())
                    
                    ws.write(renglon, 0, viajeD.fecha_salida, date_format)
                    #validar los vacios
                    ws.col(0).width=3000
                    ws.write(renglon, 1, viajeD.pk)
                    ws.col(1).width=6250
                    ws.write(renglon, 2, viajeD.cliente.__unicode__())
                    ws.col(2).width=3000
                    ws.write(renglon, 3, viajeD.departamento.__unicode__())
                    ws.col(3).width=3000
                    ws.write(renglon, 4, mov.concepto)
                    ws.col(4).width=3000
                    ws.write(renglon, 5, mov.importe, formatoNum)
                    ws.col(5).width=6250
                    ws.write(renglon, 6, viajeD.factura)
                    ws.col(6).width=6250
                    ws.write(renglon, 7, '')
                    ws.col(7).width=4000
                    ws.write(renglon, 8, viajeD.facturacion_flete, formatoNum)
                    ws.col(8).width=5000
                    ws.write(renglon, 9,  viajeD.casetas_lg, formatoNum)
                    #ws.col(9).width=6250
                    #destino = Destino.objects.filter(viaje=viajeD.pk)
                    #destinoTxt = ''
                    #for desd in destino:
                    #    destinoTxt =  direccion_recupera(desd.destino_clave_municipio)
                    #ws.write(renglon, 10,destinoTxt)
                    ws.col(9).width=5000
                    ws.write(renglon, 10, viajeD.maniobras_locales, formatoNum)
                    ws.col(10).width=5000
                    ws.write(renglon, 11, viajeD.maniobras_foraneas, formatoNum)
                    ws.col(11).width=5000
                    ws.write(renglon, 12, viajeD.factura_subtotal, formatoNum)
                    ws.col(12).width=5000
                    ws.write(renglon, 13, viajeD.factura_iva, formatoNum)
                    ws.col(13).width=5000
                    ws.write(renglon, 14, viajeD.factura_retenciones, formatoNum)
                    ws.col(14).width=5000
                    ws.write(renglon, 15, viajeD.factura_total, formatoNum)
                    ws.col(15).width=5000
                    

                    posCon = 12

                    renglon += 1
                except Exception as detalle:
                    print 'Error no existen datos Viaje:', detalle
                    print sys.exc_info()

            excelGenerado = True
    else:
        messages.warning(request, 'No se encontraron registros con los criterios seleccionados')
        form = reporteForm(request.POST)
        return render(request,'reporteGastos.html', {'form': form,})

    if excelGenerado:
        wb.save(response)
        return response



def direccion_recupera(ids):

    ids_array = ids.split(',')

    edos = []
    asenta = []
    for id in ids_array:
        e, a = id.split('-')
        edos.append(e)
        asenta.append(a)

    municipio = ''
    resultados = Sepomex.objects.filter(id_asenta_cpcons__in=asenta, clave_estado__in=edos).values('id_asenta_cpcons', 'clave_estado', 'municipio', 'estado', 'ciudad').distinct()
    data = []
    for resultado in resultados:

        if resultado['ciudad'] != '' and resultado['ciudad'] != resultado['municipio']:
            municipio = '%s (%s)'%(resultado['municipio'], resultado['ciudad'])
        else:
            municipio = resultado['municipio']


    return municipio

def saldos_index (requests):
    searchform = SearchForm_saldos (request.GET)
    filters = {}

    if ('pk' in request.GET) and request.GET['pk'].strip():
        filters['pk'] = request.GET['pk']
    if ('solicitante' in request.GET) and request.GET['solicitante'].strip():
        filters['solicitante'] = request.GET['solicitante']
    if ('beneficiario' in request.GET) and request.GET['beneficiario'].strip():
        filters['beneficiario__pk'] = request.GET['beneficiario']
    if ('fecha'in request.GET) and request.GET ['fecha'].strip():
        filters['fecha']= request.GET['fecha']
    if ('destino' in request.GET) and request.GET['destino'].strip():
        destinos = Destino.objects.filter(destino_clave_municipio=request.GET['destino']).values_list('viaje_id', flat=True)
        filters['workflowactivity__id__in'] = destinos
    ##filtes ['solicitante__id__in']=

    saldos_list = saldos.objects.filter(**filters)

    if not bool(filters):
        saldos_list= solic_list.order_by('-pk')

    #solic_list = Solicitudes.objects.all()
    paginator = Paginator(solic_list, 10)
    page = request.GET.get('page')

    try:
        solics = paginator.page(page)
    except PageNotAnInteger:
        solics = paginator.page(1)
    except EmptyPage:
        solics = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'solics':solics,
    })

    return render_to_response ('Solicitudes.html', context)


	

def saldos_add (request):

	if request.method == 'POST':
        	form = saldos_add_form(request.POST)
        	if form.is_valid():
            		ingreso = form.save()
            		messages.success(request, 'Se ha actualizado el saldo')
            		return HttpResponseRedirect (reverse('solicitudes.views.saldos_index'))
        	else:
            		message.error(request, 'Ha ocurrido algun al actualizar el saldo')
   	else:
        	form = conceptos_form()
    	context = RequestContext(request, {
        	'form':saldos_add_form,
        	'action':'Guardar'
    	})

    	return render_to_response ('solconceptos_add.html', context)



@csrf_exempt
@login_required
def reporteContable(request):
    print 'Reporte Contable...'

    filters = {}
    filtersViaje = {}
    inicial = None
    final = None
    gastosViaje = None
    if ('id_viaje') in request.POST and request.POST['id_viaje'].strip():
        filters['sol_bill'] = request.POST['id_viaje']
        filtersViaje['pk'] = request.POST['id_viaje']
    if ('operador') in request.POST and request.POST['operador'].strip():
        filters['beneficiario'] = request.POST['operador']
        filtersViaje['operador'] = request.POST['operador']
    if ('fecha_from') in request.POST and request.POST['fecha_from'].strip():
        inicial = request.POST['fecha_from']
    if ('fecha_to') in request.POST and request.POST['fecha_to'].strip():
        final = request.POST['fecha_to']


    response = HttpResponse(mimetype="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=reporte.xls'

    if inicial and final:
        filters['fecha_asig__range'] = (inicial, final)
        filtersViaje['fecha_salida__range'] = (inicial, final)
    elif inicial or final:
        messages.error(request, 'Seleccione completo rango de fechas.')
        form = reporteForm(request.POST)
        return render(request,'reporteContable.html', {'form': form,})

    if not len(filters):
        messages.error(request, 'Seleccione por lo menos un filtro o un rango de fechas')
        form = reporteForm(request.POST)
        return render(request,'reporteContable.html', {'form': form,})


    solicitudes = Solicitudes.objects.filter(**filters)
    viaje = Viaje.objects.filter(**filtersViaje)

    #solicitudes = Solicitudes.objects.filter(sol_bill=5553)

    wb = xlwt.Workbook(encoding='utf8')
    ws = wb.add_sheet('Reporte')
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/mm/yyyy'
    formatoNum = XFStyle()
    formatoNum.num_format_str = '$#,##0.00'
    font = xlwt.Font() # Crear Font
    font.name = 'Arial'
    font.height = 20 * 12  #22pt
    font.bold = True
    font.italic = True
    style = xlwt.XFStyle() # Crar Style
    style = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue;') #background color
    style.font = font # Aplicar Font al Style
    #ws.write_merge(0, 0, 0, 14, r'Resumen contable', style)

    columnas = [
            (u"No. Movimiento", 70),
            (r'Fecha de Asignación', 15),
            (u"Nombre", 70),
            (u"No. de docto.", 70),
            (u"Cliente.", 70),
            (u"Departamento.",70),
            (u"Abono", 70),
            (u"Concepto", 70),
            (u"Referencia", 70),
            (u"Solicita", 70),
            (u"Fecha del Viaje", 70),
            (r'Económico', 70),
            (u"Beneficiario", 70),
            (u"DESTINO", 70),
            (u"SERVICIO", 70),
            (u"Forma de Pago", 70),
            (r"Área", 70),
            (u"Asignado por", 70),
            (u"Saldo Anterior", 70),
            (u"Nuevo Saldo", 70),

    ]

    posx = 0
    for col in xrange(len(columnas)):
        ws.write(0, posx, columnas[col][0])
        posx += 1

    print 'solicitudes '  + str(solicitudes.count())
    print 'viaje '  + str(viaje.count())
    renglon = 1
    excelGenerado = False
    if solicitudes.count():

        for solic in solicitudes:

            try:
                mov = Movimientos.objects.filter(ref_solicitud = solic.id)

                for movC in mov:
                    v = multi_getattr(solic,'sol_bill')
                    clientes=Viaje.objects.filter(id= v)
                    cliente=None
                    depto=None
                    for c in clientes:
                        cliente = str(c.cliente)
                        depto = str(c.departamento)
                    #print '>>> ' + str(solic.pk)
                    #print '>>> ' + str(solic.sol_bill.pk)
                    ws.write(renglon, 0, movC.pk)
                    ws.col(0).width=3000
                    sollbil =  multi_getattr(solic,'sol_bill')
                    ws.write(renglon, 1, solic.fecha_asig, date_format)
                    #validar los vacios
                    ws.col(1).width=3000
                    ws.write(renglon, 2, multi_getattr(solic,'beneficiario_id'))
                    ws.col(2).width=6250
                    ws.write(renglon, 3, sollbil)
                    ws.col(3).width=3000
                    ws.write(renglon, 4, cliente)
                    ws.col(4).width=3000
                    ws.write(renglon, 5, depto)
                    ws.col(5).width=3000
                    ws.write(renglon, 6, movC.importe,formatoNum)
                    ws.col(6).width=3000
                    ws.write(renglon, 7, solic.concepts.nombre_conc)
                    ws.col(7).width=3000
                    ws.write(renglon, 8, solic.refer)
                    ws.col(8).width=6250
                    ws.write(renglon, 9, solic.solicitante.__unicode__())
                    ws.col(9).width=6250
                    ws.write(renglon, 10, '')
                    #ws.write(renglon, 8, solic.sol_bill.fecha_salida, date_format)
                    ws.col(10).width=4000
                    ws.write(renglon, 11, '')
                    #ws.write(renglon, 9, solic.sol_bill.economico.pk)
                    ws.col(11).width=3000
                    ws.write(renglon, 12, multi_getattr(solic,'benef_otros_id'))
                    ws.col(12).width=6250
                    destino = Destino.objects.filter(viaje=sollbil)
                    destinoTxt = ''
                    for desd in destino:
                        destinoTxt =  direccion_recupera(desd.destino_clave_municipio)
                    ws.write(renglon, 13,destinoTxt)
                    ws.col(13).width=3000
                    ws.write(renglon, 14, '')
                    #ws.write(renglon, 12, solic.sol_bill.departamento.__unicode__())
                    ws.col(14).width=3000
                    ws.write(renglon, 15,  movC.idPartida.__unicode__())
                    ws.col(15).width=6250
                    ws.write(renglon, 16,  movC.idArea.__unicode__())
                    ws.col(16).width=6250
                    ws.write(renglon, 17,  movC.id_auth_user.first_name + ' ' + movC.id_auth_user.last_name)
                    ws.col(17).width=6250
                    ws.write(renglon, 18, movC.montoPartida,formatoNum)
                    ws.col(18).width=6250
                    nuevoSaldo = 0
                    if movC.tipo == 'A' and movC.montoPartida is not None:
                        nuevoSaldo = movC.montoPartida + movC.importe
                    elif movC.tipo == 'C' and movC.montoPartida is not None:
                        nuevoSaldo = movC.montoPartida - movC.importe
                    ws.write(renglon, 19, nuevoSaldo,formatoNum)
                    ws.col(18).width=6250

                    renglon += 1
            except ObjectDoesNotExist:
                renglon += 1
                #print 'No existe Viaje relacionado'
            except Exception as detalle:
                renglon += 1
                print 'Error no existen datos:', detalle
                print sys.exc_info()



        #wb.save(response)
        excelGenerado = True
        #return response

    if viaje.count():
        #ws.write_merge(renglon, renglon, 0, 14, r'Movimientos Contables de Viaje Regreso', style)
        #renglon += 1
        for viajeD in viaje:
            try:
                #print '>>> ' + str(solic.pk)
                #print '>>> ' + str(solic.sol_bill.pk)
                #sollbil =  multi_getattr(solic,'sol_bill')

                #mov = Movimientos.objects.filter(ref_viaje = viajeD.pk).exclude(ref_solicitud__null = True)
                mov = Movimientos.objects.filter(ref_viaje = viajeD.pk, ref_solicitud__isnull = True)

                for movC in mov:

                    #ws.write(renglon, 0, movC.pk)
                    ws.write(renglon, 0, movC.pk)
                    ws.col(0).width=3000
                    ws.write(renglon, 1, '')
                    #validar los vacios
                    ws.col(1).width=3000
                    ws.write(renglon, 2, viajeD.operador.__unicode__())
                    ws.col(2).width=6250
                    ws.write(renglon, 3, viajeD.pk)
                    ws.col(3).width=3000
                    ws.write(renglon, 4, viajeD.cliente.__unicode__())
                    ws.col(4).width=3000
                    ws.write(renglon, 5, viajeD.departamento.__unicode__())
                    ws.col(5).width=3000
                    ws.write(renglon, 6, movC.importe,formatoNum)
                    ws.col(6).width=3000
                    ws.write(renglon, 7, movC.concepto)
                    ws.col(7).width=3000
                    ws.write(renglon, 8, movC.comentarios)
                    ws.col(8).width=6250
                    ws.write(renglon, 9, '')
                    ws.col(9).width=6250
                    ws.write(renglon, 10, viajeD.fecha_salida, date_format)
                    ws.col(10).width=4000
                    ws.write(renglon, 11, viajeD.economico.pk)
                    ws.col(11).width=3000
                    ws.write(renglon, 12,  viajeD.operador.__unicode__())
                    ws.col(12).width=6250
                    destino = Destino.objects.filter(viaje=viajeD.pk)
                    destinoTxt = ''
                    for desd in destino:
                        destinoTxt =  direccion_recupera(desd.destino_clave_municipio)
                    ws.write(renglon, 13,destinoTxt)
                    ws.col(13).width=3000
                    ws.write(renglon, 14, viajeD.departamento.__unicode__())
                    ws.col(14).width=3000
                    ws.write(renglon, 15,  movC.idPartida.__unicode__())
                    ws.col(15).width=6250
                    ws.write(renglon, 16,  movC.idArea.__unicode__())
                    ws.col(16).width=6250
                    ws.write(renglon, 17,  movC.id_auth_user.first_name + ' ' + movC.id_auth_user.last_name)
                    ws.col(17).width=6250
                    ws.write(renglon, 18, movC.montoPartida,formatoNum)
                    ws.col(18).width=6250
                    nuevoSaldo = 0
                    if movC.tipo == 'A' and movC.montoPartida is not None:
                        nuevoSaldo = movC.montoPartida + movC.importe
                    elif movC.tipo == 'C' and movC.montoPartida is not None:
                        nuevoSaldo = movC.montoPartida - movC.importe
                    ws.write(renglon, 19, nuevoSaldo,formatoNum)
                    ws.col(18).width=6250


                    renglon += 1
            except Exception as detalle:
                print 'Error no existen datos Viaje:', detalle
                print sys.exc_info()

        excelGenerado = True
    else:
        messages.warning(request, 'No se encontraron registros con los criterios seleccionados')
        form = reporteForm(request.POST)
        return render(request,'reporteContable.html', {'form': form,})

    if excelGenerado:
        wb.save(response)
        return response

@login_required
def index_comprobantes(request):

    searchform = SearchForm(request.GET)
      
    filters = {}

    if ('pk' in request.GET) and request.GET['pk'].strip():
        filters['pk'] = request.GET['pk']
    if ('solicitante' in request.GET) and request.GET['solicitante'].strip():
        filters['solicitante'] = request.GET['solicitante']
    if ('beneficiario' in request.GET) and request.GET['beneficiario'].strip():
        filters['beneficiario__pk'] = request.GET['beneficiario']
    if ('fecha'in request.GET) and request.GET ['fecha'].strip():
        filters['fecha']= request.GET['fecha']
    if ('importe' in request.GET)and request.GET['importe'].strip():
        filters['importe']= request.GET['importe']
    if ('status' in request.GET) and request.GET['status'].strip():
        filters['status']= request.GET['status']
    if ('refer' in request.GET)and request.GET['refer'].strip():
        filters['refer']= request.GET['refer']
    if ('sol_bill' in request.GET)and request.GET['sol_bill'].strip():
        filters['sol_bill']= request.GET['sol_bill']
    if ('concepts' in request.GET)and request.GET['concepts'].strip():
        filters['concepts']= request.GET['concepts']
    if ('fecha_aut' in request.GET)and request.GET['fecha_aut'].strip():
        filters['fecha_aut']= request.GET['fecha_aut']
    if ('motivo_rech' in request.GET)and request.GET['motivo_rech'].strip():
        filters['motivo_rech']= request.GET['motivo_rech']
    if ('benef_otros' in request.GET)and request.GET['benef_otros'].strip():
        filters['benef_otros']= request.GET['benef_otros']
    #if ('cancelado' in request.GET) and request.GET['cancelado'].strip():
    #   filters['cancelado']= request.GET['cancelado']
    if ('destino' in request.GET) and request.GET['destino'].strip():
            destinos = Destino.objects.filter(destino_clave_municipio=request.GET['destino']).values_list('viaje_id', flat=True)
            filters['workflowactivity__id__in'] = destinos
    ##filtes ['solicitante__id__in']=
    solic_list = Solicitudes.objects.filter(status = 4)
    solic_list = solic_list.filter(**filters)        

    if not bool(filters):
        solic_list= solic_list.order_by('-pk').exclude(status = 5)
   
    paginator = Paginator(solic_list, 300)
    page = request.GET.get('page')

    try:
        solics = paginator.page(page)
    except PageNotAnInteger:
        solics = paginator.page(1)
    except EmptyPage:
        solics = paginator.page(paginator.num_pages)
    context = RequestContext (request, {
        'searchform':searchform,
        'solics':solics,
    })

    return render_to_response ('Solicitudes_Comprobantes.html', context)

@login_required
def subirArchivoPendiente(request, idSolicitud, tipo):
    print idSolicitud
    if request.method == 'POST':
        form = archivoPendienteForm(request.POST, request.FILES)
        print form
        #form.save()
        if form.is_valid():
            print 'Es valido'
            print idSolicitud
            print tipo
            print form.cleaned_data['idSolicitud']
            print form.cleaned_data['tipo']
            print form.cleaned_data['archivo']

            match = False
            nombreArchivo = str(form.cleaned_data['archivo'])
            nombreArchivo = nombreArchivo.upper()
            print nombreArchivo
            tipoArchivo = 'NoDefinido'
            if nombreArchivo.endswith('.PDF') and tipo == 'PDF':
                match = True
                tipoArchivo = 'PDF'
            elif nombreArchivo.endswith('.JPG') and tipo == 'JPG':
                match = True
                tipoArchivo = 'JPG'
            elif nombreArchivo.endswith('.XML') and tipo == 'XML':
                match = True
                tipoArchivo = 'XML'
            else:
                txtmsg = 'Extension de archivo no concuerda con opcion seleccionada.'
                messages.error(request, txtmsg)

            if match:
                try:
                    archivo = ArchivoPendiente.objects.get(idSolicitud = form.cleaned_data['idSolicitud'], tipo = form.cleaned_data['tipo'])
                    if archivo:
                        print 'eliminando archivo anterior ' + str(archivo.archivo)
                        ruta = settings.MEDIA_ROOT + str(archivo.archivo)
                        os.remove(ruta)
                    form = archivoPendienteForm(request.POST, request.FILES, instance=archivo)
                    form.save()

                    messages.success(request, u'Archivos actualizados exitosamente')
                except Exception:
                    form.save()
                    messages.success(request, u'Archivos cargados exitosamente')

                archivo = ArchivoPendiente.objects.get(idSolicitud = form.cleaned_data['idSolicitud'], tipo = form.cleaned_data['tipo'])
                solicitud = Solicitudes.objects.get(id = form.cleaned_data['idSolicitud'])

                if tipoArchivo == 'PDF':
                    solicitud.archivo_pdf = archivo.archivo
                elif tipoArchivo == 'JPG':
                    solicitud.archivo_jpg = archivo.archivo
                else:
                    solicitud.archivo_xml = archivo.archivo

                #ESta es la parte para cambiar de ESTATUS, al cambiar de status lo quita de la lista
                #solicitud.status = 7
                solicitud.save()

                return HttpResponseRedirect (reverse('solicitudes.views.index_comprobantes'))


        else:
            messages.error(request, 'Verifique el archivo')

    else:
        print idSolicitud
        print tipo
        form = archivoPendienteForm(initial={'idSolicitud':idSolicitud, 'tipo':tipo,})

    context = RequestContext(request,{
        'form':form,
        'solicitudes_id':idSolicitud,
        'tipo':tipo
    })

    return render_to_response('subirArchivo.html', context)


@login_required
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
