from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from reporte.models import ing_egre, nomina, MESES, CLIENTE, infoMensual
from reporte.forms import *
from django.contrib import messages
from django.template.loader import get_template
from django.template.defaulttags import register
from django.template import Context
from django.conf import settings
from empleados.models import empleado, Puestos, movimientos
from viajes.models import Viaje 
from clientes.models import Cliente
import sys, os
from xhtml2pdf import pisa
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Group
from django.db.models import Count, Q, Sum, Max 
import time, datetime
from datetime import datetime, date
from easy_pdf.views import PDFTemplateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage 


# Create your views here.


@login_required
def agregar(request):
    if request.method=='POST':
        form = IngresosEgresosForm(request.POST)
        if form.is_valid():

            ingreso = form.save()
            messages.success(request, 'Se han registrado los movimientos de egresos e ingresos')
            return HttpResponseRedirect (reverse ('reporte.views.agregarNomina',kwargs={'idReporte':ingreso.pk}))

        else:
            messages.error(request,'Ha ocurrido un error.')
    else:
        form = IngresosEgresosForm()
    context = RequestContext (request,{
        'form':IngresosEgresosForm,
        'action':'Agregar',
    })
    return render_to_response ('ingreEgre_form.html', context) 

@login_required
def agregarNomina(request, idReporte):
    if request.method=='POST':
        form = NominaForm(request.POST)
        print form
        form.cleaned_data['idRep'] = idReporte
        if form.is_valid():
            ingreso = form.save()
            messages.success(request, 'Se ha registrado la informacion de nomina')
            #return HttpResponseRedirect (reverse ('beneficiarios.views.index'))
            return HttpResponseRedirect (reverse ('reporte.views.agregarBruta',kwargs={'idReporte':idReporte}))
        else:
            messages.error(request,'Ha ocurrido un error.')
    else:
        form = NominaForm(initial={'idRep':idReporte})
    context = RequestContext (request,{
        'form':form,
        'action':'Agregar',
    })
    return render_to_response ('ingreNom_form.html', context) 

@login_required
def agregarBruta(request,idReporte):
    if request.method=='POST':
        form = BrutaForm(request.POST)
        print form
        form.cleaned_data['idRep'] = idReporte
        if form.is_valid():
            ingreso = form.save()
            messages.success(request, 'Se ha registrado las ventas Brutas')
            return HttpResponseRedirect (reverse ('reporte.views.agregarNeta',kwargs={'idReporte':idReporte}))
        else:
            messages.error(request,'Ha ocurrido un error.')
    else:
        form = BrutaForm(initial={'idRep':idReporte})
    context = RequestContext (request,{
        'form':form,
        'action':'Agregar',
    })
    return render_to_response ('ingreBruta_form.html', context)    

@login_required
def agregarNeta(request,idReporte):
    if request.method=='POST':
        form = NetaForm(request.POST)
        print form
        form.cleaned_data['idRep'] = idReporte
        if form.is_valid():
            ingreso = form.save()
            messages.success(request, 'Se ha registrado las ventas netas')
            return HttpResponseRedirect (reverse ('reporte.views.generarReporte',kwargs={'idReporte':idReporte}))
            
        else:
            messages.error(request,'Ha ocurrido un error.')
    else:
        form = NetaForm(initial={'idRep':idReporte})
    context = RequestContext (request,{
        'form':form,
        'action':'Agregar',
    })
    return render_to_response ('ingreNeta_form.html', context)

@login_required
def generarReporte(request, idReporte):

    templateString = ("archivoPdf.html")
    template = get_template(templateString)
    reporte = get_object_or_404(ing_egre, pk=idReporte)
    nom = get_object_or_404(nomina, idRep=idReporte)
    vbruta = get_object_or_404(venta_bruta, idRep=idReporte)
    vneta = get_object_or_404(venta_neta, idRep=idReporte)

    myContextObject = {
    'form':reporte,
    'nom':nom,
    'vb':vbruta,
    'vn':vneta,
    'meses':MESES,
    }

    html = template.render(Context(myContextObject))
    file = open(settings.MEDIA_ROOT + "documentosEmp/ReporteNo" + idReporte + ".pdf", "w+b")
    links    = lambda uri, rel: os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ''))
    pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file, encoding='utf-8', link_callback=links)
    file.seek(0)
    pdf = file.read()
    file.close()
    pdfSal =  open(settings.MEDIA_ROOT + "documentosEmp/ReporteNo" + idReporte + ".pdf", "r")
    response = HttpResponse(pdfSal, mimetype="application/pdf")
    response["Content-Disposition"] = "attachment; filename=" + "SolicitudNo" + idReporte + "_Resumen.pdf"
    return response


@register.filter
def get_item(dictionary, key):
    key = int(key)
    dato = dictionary[key - 1]
    return dato[1]

    if request.method=='POST':
        form = NetaForm(request.POST)
        print form
        form.cleaned_data['idRep'] = idReporte
        if form.is_valid():
            ingreso = form.save()
            messages.success(request, 'Se ha registrado las ventas netas')
            return HttpResponseRedirect (reverse ('reporte.views.generarReporte',kwargs={'idReporte':idReporte}))
            
        else:
            messages.error(request,'Ha ocurrido un error.')
    else:
        form = NetaForm(initial={'idRep':idReporte})
    context = RequestContext (request,{
        'form':form,
        'action':'Agregar',
    })
    return render_to_response ('ingreNeta_form.html', context)

@login_required



def obtenerDatos(request):

    if request.method=='POST':

        form = repMensualForm(request.POST)
        print 'Este es el formulario para guardar en la tabla reportes'
        if form.is_valid():
            
            mes = request.POST['mes']
            
            print test

            repmensual= infoMensual.objects.filter(mes= mes)
            if repmensual:
                print 'este es el mes que existe' + mes
                if request.POST['text_nom1']:
                    infoMensual.objects.filter(mes=mes).update(text_nom1 = request.POST['text_nom1'])
                if request.POST['text_nom2']:
                    infoMensual.objects.filter(mes=mes).update(text_nom2 = request.POST['text_nom2'])
                if request.POST['text_nom3']:
                    infoMensual.objects.filter(mes=mes).update(text_nom3 = request.POST['text_nom3'])
                if request.POST['text_nom4']:
                    infoMensual.objects.filter(mes=mes).update(text_nom4 = request.POST['text_nom4'])
                if request.POST['text_nom5']:
                    infoMensual.objects.filter(mes=mes).update(text_nom5= request.POST['text_nom5'])
                if request.POST['text_nom6']:
                    infoMensual.objects.filter(mes=mes).update(text_nom6= request.POST['text_nom6'])
                if request.POST['text_nom7']:
                    infoMensual.objects.filter(mes=mes).update(text_nom7= request.POST['text_nom7'])
                if request.POST['text_nom8']:
                    infoMensual.objects.filter(mes=mes).update(text_nom8= request.POST['text_nom8'])
                if request.POST['text_nom9']:
                    infoMensual.objects.filter(mes=mes).update(text_nom9= request.POST['text_nom9'])
                if request.POST['text_nom10']:
                    infoMensual.objects.filter(mes=mes).update(text_nom10= request.POST['text_nom10'])
                if request.POST['org_dir']:
                    infoMensual.objects.filter(mes=mes).update(org_dir= request.POST['org_dir'])
                if request.POST['org_jft']:
                    infoMensual.objects.filter(mes=mes).update(org_jft= request.POST['org_jft'])
                if request.POST['org_jfa']:
                    infoMensual.objects.filter(mes=mes).update(org_jfa= request.POST['org_jfa'])
                if request.POST['org_f']:
                    infoMensual.objects.filter(mes=mes).update(org_f= request.POST['org_f'])
                if request.POST['org_cli']:
                    infoMensual.objects.filter(mes=mes).update(org_cli=request.POST['org_cli'])

                ########## aqui continuar con los cambios de los datos##########

            else:

                infoMensual.objects.create(mes=mes)

                mesant= infoMensual.objects.filter(mes=mes)

                if request.POST['text_nom1']:
                    infoMensual.objects.filter(mes=mes).update(text_nom1 = request.POST['text_nom1'])
                else:
                    infoMensual.objects.filter(mes=mes).update(text_nom1 = request.POST['text_nom1'])
                if request.POST['text_nom2']:
                    infoMensual.objects.filter(mes=mes).update(text_nom2 = request.POST['text_nom2'])
                if request.POST['text_nom3']:
                    infoMensual.objects.filter(mes=mes).update(text_nom3 = request.POST['text_nom3'])
                if request.POST['text_nom4']:
                    infoMensual.objects.filter(mes=mes).update(text_nom4 = request.POST['text_nom4'])
                if request.POST['text_nom5']:
                    infoMensual.objects.filter(mes=mes).update(text_nom5= request.POST['text_nom5'])
                if request.POST['text_nom6']:
                    infoMensual.objects.filter(mes=mes).update(text_nom6= request.POST['text_nom6'])
                if request.POST['text_nom7']:
                    infoMensual.objects.filter(mes=mes).update(text_nom7= request.POST['text_nom7'])
                if request.POST['text_nom8']:
                    infoMensual.objects.filter(mes=mes).update(text_nom8= request.POST['text_nom8'])
                if request.POST['text_nom9']:
                    infoMensual.objects.filter(mes=mes).update(text_nom9= request.POST['text_nom9'])
                if request.POST['text_nom10']:
                    infoMensual.objects.filter(mes=mes).update(text_nom10= request.POST['text_nom10'])
                if request.POST['org_dir']:
                    infoMensual.objects.filter(mes=mes).update(org_dir= request.POST['org_dir'])
                if request.POST['org_jft']:
                    infoMensual.objects.filter(mes=mes).update(org_jft= request.POST['org_jft'])
                if request.POST['org_jfa']:
                    infoMensual.objects.filter(mes=mes).update(org_jfa= request.POST['org_jfa'])
                if request.POST['org_f']:
                    infoMensual.objects.filter(mes=mes).update(org_f= request.POST['org_f'])
                if request.POST['org_cli']:
                    infoMensual.objects.filter(mes=mes).update(org_cli=request.POST['org_cli'])

                print 'Este mes no existe: ' + mes
                print 'debe de crear el mes: '


        else: 
            messages.error(request,'Ha ocurrido un error')
    else:
        form=repMensualForm()
    context = RequestContext(request,{
        'form':form,
        'action':'Obtener',
        })
    return render_to_response('generaRepMensual.html', context)

@login_required
def indexReportes(request):
    reportes_list = infoMensual.objects.all()             
    paginator = Paginator(reportes_list, 12)
    page = request.GET.get('page')
    
    try:
        reportes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        reportes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        reportes = paginator.page(paginator.num_pages)
    
        
    context = RequestContext(request,{             
        'reportes': reportes,
    })        
    return render_to_response('reportesMensuales.html', context)



##class IncidenteView(PDFTemplateView):
##    template_name = "repIncidencia.html"
    
##    def get_context_data(self, pk, **kwargs):

##        incidente = ReporteUnidad.objects.get(pk=pk)        
##        return super(IncidenteView, self).get_context_data(
##            pagesize="A4",
##            title="Incidente " + pk,
##            incidente=incidente,

##            **kwargs
##        )

class ReporteMensualView(PDFTemplateView):
    template_name = "Reporte_Mensual.html"
    
    def get_context_data(self, pk, **kwargs):
        info = infoMensual.objects.get(pk=pk)#### aqui buscamos el mes seleccionado.

        ############ PRUEBA DE RECABAR INFORMACION###########
        if info.mes:

            lista_Dir = Puestos.objects.filter(tipo = 1)
            lista_Adm = Puestos.objects.filter(tipo = 2)
            lista_Ope = Puestos.objects.filter(tipo = 3)
            lista_Man = Puestos.objects.filter(tipo = 4)
            lista_Cho = Puestos.objects.filter(tipo = 5)
            emppleado_alta = empleado.objects.filter(status = 1)
            nomdir=empleado.objects.filter(status =1, puesto = lista_Dir)
            nomadm=empleado.objects.filter(status = 1, puesto = lista_Adm)
            nomope=empleado.objects.filter(status = 1, puesto = lista_Ope)
            nomman=empleado.objects.filter(status =1, puesto = lista_Man)
            nomcho=empleado.objects.filter(status=1, puesto = lista_Cho)
            ntotal = emppleado_alta.count()
            nd = nomdir.count()
            na = nomadm.count()
            no = nomope.count()
            nm = nomman.count()
            nc = nomcho.count()     
            nt = nd + na + no + nm + nc
            print 'Estos son los Directivos: ' + str(nd)
            print 'Estos son los Administrativos: ' + str(na)
            print 'Estos son los Operativos: ' + str (no)
            print 'Estos son los de Mantenimiento: ' + str(nm)
            print 'Estos son los choferes: ' + str(nc)    
            print 'Este es el total de los empleados' + str (nt) +  "Estos son los totales activos" + str(ntotal)

            #### Datos de Movimientos ####
            mes = str(info.mes)
            print 'Este es el mes que se selecciono:' + str(mes)
            if mes == 'Enero':
                inicial = '2016-01-01'
                final = '2016-01-30'
            elif mes == 'Febrero':
                inicial = '2016-02-01'
                final = '2016-02-28'
            elif mes == 'Marzo':
                inicial = '2016-03-01'
                final = '2016-03-31'
            elif mes == 'Abril':
                inicial = '2016-04-01'
                final = '2016-04-30'
            elif mes == 'Mayo':
                inicial = '2016-05-01'
                final = '2016-05-31'
            elif mes == 'Junio':
                inicial = '2016-06-01'
                final = '2016-06-30'
            elif mes == 'Julio':
                inicial = '2016-07-01'
                final = '2016-07-31'
            elif mes == 'Agosto':
                inicial = '2016-08-01'
                final = '2016-08-31'
            elif mes == 'Septiembre':
                inicial = '2016-09-01'
                final = '2016-09-30'
            elif mes == 'Octubre':
                inicial = '2016-10-01'
                final = '2016-10-31'
            elif mes == 'Novimebre':
                inicial = '2016-11-01'
                final = '2016-11-30'
            elif mes == 'Diciembre':
                inicial = '2016-12-01'
                final = '2016-12-01'

            filters={}
            filters_viaje={}
            if inicial and final:
                filters['fecha__range'] = (inicial, final)
                filters_viaje['fecha_salida__range'] = (inicial, final)

            print 'Inica la obtencion de datos.'
            #mov_alta2 = movimientos.objects.filter(fecha = mesdjango)
            #print mov_alta2.query
            mov_alta = movimientos.objects.filter(Q(tipo = 1) | Q(tipo = 3), **filters)
            mov_baja = movimientos.objects.filter(Q(tipo = 2)| Q(tipo = 7)|Q(tipo = 8), **filters)
            mov_alta_adm = movimientos.objects.filter(Q(tipo = 1)| Q(tipo = 2), empleado = nomadm, **filters)
            mov_alta_cho = movimientos.objects.filter(Q(tipo = 1)| Q(tipo = 2), empleado = nomope, **filters)
            print 'estos son los movimientos de Administracion ' + str(mov_alta_adm.count())
            print 'estos son los movimientos de Choferes' + str (mov_alta_cho.count())
            altas = mov_alta.count()
            bajas = mov_baja.count()
            total_movemp = int(altas) + int (bajas)
            print 'Altas = ' + str(altas)
            print 'Bajas = ' + str(bajas)
            print 'Total de Movimientos = ' + str(total_movemp)
            ################# Hasta aqui la informacion de la primer hoja #####################

            #########   Inicia las ventas Brutas y YTY POR CLIENTE ###########

            viajes= Viaje.objects.filter(**filters_viaje).aggregate(Sum('facturacion_flete'))
            print viajes
            fac_viajes = viajes.values()
            for val_fac in fac_viajes:
                fact_mes= val_fac
                print 'Este es el valor de la factura mensual' + str(fact_mes)

            clientes = Cliente.objects.all()

            for cli in clientes:
                clie = cli.id
                clien = cli.nombre
                viajes_1 = Viaje.objects.filter(cliente = clie, **filters_viaje).aggregate(Sum('facturacion_flete'))
                viajes_1 = viajes_1.values()
                for fac_cli in viajes_1:
                    cli_venta_mensual = fac_cli
                    print 'Este es el valor de la facturacion de ' + str(clien) + ' : ' + str(cli_venta_mensual)

            venta_samsung = Viaje.objects.filter(cliente = 1, **filters_viaje).aggregate(Sum('facturacion_flete'), Sum('facturacion_maniobra'), Sum('facturacion_desvio'),
                Sum('facturacion_reparto'), Sum('facturacion_ferri'), Sum('facturacion_ferri'), Sum('facturacion_otros'))
            print venta_samsung
            a= 0
            ventatot = 0
            for ven_sam in venta_samsung.values():
                i = 1
                a=a+i
                print a
                venta_sam = ven_sam                
                ventapar = ven_sam
                ventatot = ventatot + ventapar
                print venta_sam  
                print ventatot
           
        ################   Termina Ventas LG y Samsung ##################
            ######## Inicia comparativo de ventas Mensuales Anuales########
            ##Enero###
            filters_enero15 ={}
            filters_enero={}
            inicial15 = '2015-01-01'
            final15 = '2015-01-30'
            filters_enero15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-01-30'
            filters_enero['fecha_salida__range']=(inicial, final) 
            ven_enero_15 = Viaje.objects.filter(cliente = 1, **filters_enero15).aggregate(Sum('facturacion_flete'))
            for ven0115 in ven_enero_15.values():
                Venta0115 = ven0115
                print 'Venta Samsung Enero 2015 : ' + str(Venta0115)
            ven_enero = Viaje.objects.filter(cliente=1, **filters_enero).aggregate(Sum('facturacion_flete'))
            for ven0116 in ven_enero.values():
                Venta0116= ven0116
                print 'Venta Samsung Enero 2016 : ' + str(Venta0116)
            difEnero = float 
            difEnero = ((float(ven0116)/float(ven0115)) -1) * 100
            difEne = int(ven0115)-int (ven0116)
            print difEne     
            print 'Diferencia Enero: ' + str(difEnero) 
            #### Febrero ####
            filters_feb15 ={}
            filters_feb={}
            inicial15 = '2015-02-01'
            final15 = '2015-02-28'
            filters_feb15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-02-01' 
            final= '2016-02-28'
            filters_feb['fecha_salida__range']=(inicial, final) 
            ven_feb_15 = Viaje.objects.filter(cliente = 1, **filters_feb15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_feb_15.values():
                Venta0215 = ven0215
                print 'Venta Samsung Febrero 2015 : ' + str(Venta0215)
            ven_feb = Viaje.objects.filter(cliente=1, **filters_feb).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_feb.values():
                Venta0216= ven0216
                print 'Venta Samsung Febrero 2016 : ' + str(Venta0216)
            difFebrero = float 
            difFebrero = ((float(ven0216)/float(ven0215)) -1) * 100
            diffeb = int(ven0215)-int (ven0216)
            print diffeb     
            print 'Diferencia Febrero: ' + str(difFebrero) 
            ##### Marzo ########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-03-01'
            final15 = '2015-03-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-03-01' 
            final= '2016-03-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0315 in ven_mar_15.values():
                Venta0315 = ven0315
                print 'Venta Samsung Marzo 2015 : ' + str(Venta0315)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0316 in ven_mar.values():
                Venta0316= ven0316
                print 'Venta Samsung Marzo 2016 : ' + str(Venta0316)
            difMarzo = float 
            difMarzo = ((float(ven0316)/float(ven0315)) -1) * 100
            difMar = int(ven0315)-int (ven0316)
            print difMar     
            print 'Diferencia Marzo: ' + str(difMarzo) 
            ##### Abril ########
            filters_abr15 ={}
            filters_abr={}
            inicial15 = '2015-04-01'
            final15 = '2015-04-30'
            filters_abr15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-04-01' 
            final= '2016-04-30'
            filters_abr['fecha_salida__range']=(inicial, final) 
            ven_abr_15 = Viaje.objects.filter(cliente = 1, **filters_abr15).aggregate(Sum('facturacion_flete'))
            for ven0415 in ven_abr_15.values():
                Venta0415 = ven0415
                print 'Venta Samsung Abril 2015 : ' + str(Venta0415)
            ven_abr = Viaje.objects.filter(cliente=1, **filters_abr).aggregate(Sum('facturacion_flete'))
            for ven0416 in ven_abr.values():
                Venta0416= ven0416
                print 'Venta Samsung Abril 2016 : ' + str(Venta0416)
            difAbril = float 
            difAbril = ((float(ven0216)/float(ven0415)) -1) * 100
            difAbr = int(ven0415)-int (ven0416)
            print difAbr     
            print 'Diferencia Abril: ' + str(difAbril) 
            ######### Mayo##########
            filters_may15 ={}
            filters_may={}
            inicial15 = '2015-05-01'
            final15 = '2015-05-31'
            filters_may15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-05-01' 
            final= '2016-05-31'
            filters_may['fecha_salida__range']=(inicial, final) 
            ven_may_15 = Viaje.objects.filter(cliente = 1, **filters_may15).aggregate(Sum('facturacion_flete'))
            for ven0515 in ven_may_15.values():
                Venta0515 = ven0515
                print 'Venta Samsung Mayo 2015 : ' + str(Venta0515)
            ven_may = Viaje.objects.filter(cliente=1, **filters_may).aggregate(Sum('facturacion_flete'))
            for ven0516 in ven_may.values():
                Venta0516= ven0516
                print 'Venta Samsung Mayo 2016 : ' + str(Venta0516)
            difMayo = float 
            difMayo = ((float(ven0516)/float(ven0515)) -1) * 100
            difMay = int(ven0515)-int (ven0516)
            print difEne     
            print 'Diferencia Mayo: ' + str(difMayo)
            ######### Junio ##########
            filters_jun15 ={}
            filters_jun={}
            inicial15 = '2015-06-01'
            final15 = '2015-06-30'
            filters_jun15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-06-01' 
            final= '2016-06-30'
            filters_jun['fecha_salida__range']=(inicial, final) 
            ven_jun_15 = Viaje.objects.filter(cliente = 1, **filters_jun15).aggregate(Sum('facturacion_flete'))
            for ven0615 in ven_jun_15.values():
                Venta0615 = ven0615
                print 'Venta Samsung Junio 2015 : ' + str(Venta0615)
            ven_jun = Viaje.objects.filter(cliente=1, **filters_jun).aggregate(Sum('facturacion_flete'))
            for ven0616 in ven_jun.values():
                Venta0616= ven0616
                print 'Venta Samsung Junio 2016 : ' + str(Venta0616)
            difJunio = float 
            difJunio = ((float(ven0216)/float(ven0615)) -1) * 100
            difJun = int(ven0215)-int (ven0616)
            print difJun     
            print 'Diferencia Junio: ' + str(difJunio)  
            ######### Julio##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-07-01'
            final15 = '2015-07-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-07-01' 
            final= '2016-07-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0715 in ven_mar_15.values():
                Venta0715 = ven0715
                print 'Venta Samsung Julio 2015 : ' + str(Venta0715)
            ven_jul = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0716 in ven_jul.values():
                Venta0716= ven0716
                print 'Venta Samsung Julio 2016 : ' + str(Venta0716)
            if ven0716 == None:
                ven0716 = 0
            difJulio = float 
            difJulio = ((float(ven0716)/float(ven0715)) -1) * 100
            difJul = int(ven0715)-int (ven0716)
            print difJul     
            print 'Diferencia Julio: ' + str(difJulio) 
             ######### Agosto ##########
            filters_ago15 ={}
            filters_ago={}
            inicial15 = '2015-08-01'
            final15 = '2015-08-30'
            filters_ago15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-08-01' 
            final= '2016-08-30'
            filters_ago['fecha_salida__range']=(inicial, final) 
            ven_ago_15 = Viaje.objects.filter(cliente = 1, **filters_ago15).aggregate(Sum('facturacion_flete'))
            for ven0815 in ven_ago_15.values():
                Venta0815 = ven0815
                print 'Venta Samsung Agosto 2015 : ' + str(Venta0815)
            ven_mar = Viaje.objects.filter(cliente=1, **filters_ago).aggregate(Sum('facturacion_flete'))
            for ven0816 in ven_mar.values():
                Venta0816= ven0816
                print 'Venta Samsung Agosto 2016 : ' + str(Venta0816)
            if ven0816 == None:
                ven0816 = 0
            difAgosto = float 
            difAgosto = ((float(ven0816)/float(ven0815)) -1) * 100
            difAgo = int(ven0815)-int (ven0816)
            print difAgo     
            print 'Diferencia Agosto: ' + str(difAgo) 
             ######### Septiembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-09-01'
            final15 = '2015-09-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-09-01' 
            final= '2016-09-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_sep_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0915 in ven_sep_15.values():
                Venta0915 = ven0915
                print 'Venta Samsung Septiembre 2015 : ' + str(Venta0915)
            ven_sep = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0916 in ven_sep.values():
                Venta0916= ven0916
                print 'Venta Samsung Septiembre 2016 : ' + str(Venta0916)
            if ven0916 == None:
                ven0916 = 0
            difSeptiembre = float 
            difSeptiembre = ((float(ven0916)/float(ven0915)) -1) * 100
            difSep = int(ven0915)-int (ven0916)
            print difSep     
            print 'Diferencia Septiembre: ' + str(difSeptiembre) 
            ######### Octubre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-10-01'
            final15 = '2015-10-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-10-01' 
            final= '2016-10-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_oct_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven1015 in ven_oct_15.values():
                Venta1015 = ven1015
                print 'Venta Samsung Octubre 2015 : ' + str(Venta1015)
            ven_oct = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven1016 in ven_oct.values():
                Venta1016= ven1016
                print 'Venta Samsung Octubre 2016 : ' + str(Venta1016)
            if ven1016 == None:
                ven1016 = 0
            difOctubre = float 
            difOctubre = ((float(ven1016)/float(ven1015)) -1) * 100
            difOct = int(ven1015)-int (ven1016)
            print difOct     
            print 'Diferencia Octubre: ' + str(difOctubre) 
             ######### Noviembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-11-01'
            final15 = '2015-11-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-11-01' 
            final= '2016-11-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_nov_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven1115 in ven_nov_15.values():
                Venta1115 = ven1115
                print 'Venta Samsung Noviembre 2015 : ' + str(Venta1115)
            ven_nov = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven1116 in ven_nov.values():
                Venta1116= ven1116
                print 'Venta Samsung Noviembre 2016 : ' + str(Venta1116)
            if ven1116 == None:
                ven1116 = 0
            difNoviembre = float 
            difNoviembre = ((float(ven1116)/float(ven1115)) -1) * 100
            difNov = int(ven1115)-int (ven1016)
            print difNov     
            print 'Diferencia Novimebre: ' + str(difNoviembre) 
            ######### Diciembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-12-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-12-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_dic_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven1215 in ven_dic_15.values():
                Venta1215 = ven1215
                print 'Venta Samsung Diciembre 2015 : ' + str(Venta1215)
            ven_dic = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven1216 in ven_dic.values():
                Venta1216= ven1216
                print 'Venta Samsung Diciembre 2016 : ' + str(Venta1216)
            if ven1216 == None:
                ven1216 = 0
            difDiciembre = float 
            difDiciembre = ((float(ven1216)/float(ven1215)) -1) * 100
            difDic = int(ven1215)-int (ven1216)
            print difDic     
            print 'Diferencia Diciembre: ' + str(difDiciembre)
            ######### 2015 ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-01-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_anu_15 = Viaje.objects.filter(cliente = 1, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven1315 in ven_anu_15.values():
                Venta1315 = ven1315
                print 'Venta LG 2015 : ' + str(Venta1315)
            ven_anu = Viaje.objects.filter(cliente=1, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven1316 in ven_anu.values():
                Venta1316= ven1316
                print 'Venta LG 2016 : ' + str(Venta1316)
            if ven1316 == None:
                ven1316 = 0
            difAnual = float 
            difAnual = ((float(ven1316)/float(ven1315)) -1) * 100
            difAnu = int(ven1315)-int (ven1316)
            print difAnu     
            print 'Diferencia Anual: ' + str(difAnual)  
        ################   Termina Ventas LG y LG ##################
            ######## Inicia comparativo de ventas Mensuales Anuales########
            ##Enero###
            filters_enero15 ={}
            filters_enero={}
            inicial15 = '2015-01-01'
            final15 = '2015-01-30'
            filters_enero15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-01-30'
            filters_enero['fecha_salida__range']=(inicial, final) 
            ven_enero_15 = Viaje.objects.filter(cliente = 2, **filters_enero15).aggregate(Sum('facturacion_flete'))
            for ven0115 in ven_enero_15.values():
                Venta0115LG = ven0115
                print 'Venta LG Enero 2015 : ' + str(Venta0115)
            ven_enero = Viaje.objects.filter(cliente=2, **filters_enero).aggregate(Sum('facturacion_flete'))
            for ven0116 in ven_enero.values():
                Venta0116LG= ven0116
                print 'Venta LG Enero 2016 : ' + str(Venta0116)
            difEneroLG = float 
            difEneroLG = ((float(ven0116)/float(ven0115)) -1) * 100
            difEneLG = int(ven0115)-int (ven0116)
            print difEneLG     
            print 'Diferencia Enero: ' + str(difEneroLG) 
            #### Febrero ####
            filters_feb15 ={}
            filters_feb={}
            inicial15 = '2015-02-01'
            final15 = '2015-02-28'
            filters_feb15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-02-01' 
            final= '2016-02-28'
            filters_feb['fecha_salida__range']=(inicial, final) 
            ven_feb_15 = Viaje.objects.filter(cliente = 2, **filters_feb15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_feb_15.values():
                Venta0215LG = ven0215
                print 'Venta LG Febrero 2015 : ' + str(Venta0215)
            ven_feb = Viaje.objects.filter(cliente=2, **filters_feb).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_feb.values():
                Venta0216LG= ven0216
                print 'Venta LG Febrero 2016 : ' + str(Venta0216)
            difFebreroLG = float 
            difFebreroLG = ((float(ven0216)/float(ven0215)) -1) * 100
            difFebLG = int(ven0215)-int (ven0216)
            print difFebLG     
            print 'Diferencia Febrero: ' + str(difFebreroLG) 
            ##### Marzo ########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-03-01'
            final15 = '2015-03-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-03-01' 
            final= '2016-03-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0315LG in ven_mar_15.values():
                Venta0315LG = ven0315
                print 'Venta LG Marzo 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0316LG in ven_mar.values():
                Venta0316LG= ven0316
                print 'Venta LG Marzo 2016 : ' + str(Venta0216)
            difMarzoLG = float 
            difMarzoLG = ((float(ven0316LG)/float(ven0315LG)) -1) * 100
            difMarLG = int(ven0315LG)-int (ven0316LG)
            print difMarLG     
            print 'Diferencia Marzo: ' + str(difMarLG) 
            ##### Abril ########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-04-01'
            final15 = '2015-04-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-04-01' 
            final= '2016-04-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0415LG in ven_mar_15.values():
                Venta0415LG = ven0415
                print 'Venta LG Abril 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0416LG in ven_mar.values():
                Venta0416LG= ven0416
                print 'Venta LG Abril 2016 : ' + str(Venta0316LG)
            difAbrilLG = float 
            difAbrilLG = ((float(ven0416)/float(ven0415)) -1) * 100
            difAbrLG = int(ven0415LG)-int (ven0416LG)
            print difAbrLG     
            print 'Diferencia Abril: ' + str(difAbrilLG) 
            ######### Mayo##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-05-01'
            final15 = '2015-05-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-05-01' 
            final= '2016-05-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_may_15LG = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0515LG in ven_may_15.values():
                Venta0515LG = ven0515
                print 'Venta LG Mayo 2015 : ' + str(Venta0515LG)
            ven_mayLG = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0516LG in ven_mayLG.values():
                Venta0516LG= ven0516LG
                print 'Venta LG Mayo 2016 : ' + str(Venta0516LG)
            difMayoLG = float 
            difMayoLG = ((float(ven0516LG)/float(ven0515LG)) -1) * 100
            difMayLG = int(ven0515LG)-int (ven0516LG)
            print difMayLG     
            print 'Diferencia Mayo: ' + str(difMayLG)
            ######### Junio ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-06-01'
            final15 = '2015-06-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-06-01' 
            final= '2016-06-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_jun_15LG = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0615LG in ven_jun_15LG.values():
                Venta0615LG = ven0615LG
                print 'Venta LG Junio 2015 : ' + str(Venta0615LG)
            ven_junLG = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0616LG in ven_jun.values():
                Venta0616LG= ven0616LG
                print 'Venta LG Junio 2016 : ' + str(Venta0616LG)
            difJunioLG = float 
            difJunioLG = ((float(ven0616LG)/float(ven0615LG)) -1) * 100
            difJunLG = int(ven0615LG)-int (ven0616LG)
            print difJunLG     
            print 'Diferencia Junio: ' + str(difJunioLG)  
            ######### Julio##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-07-01'
            final15 = '2015-07-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-07-01' 
            final= '2016-07-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_jul_15LG = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0715LG in ven_jun_15LG.values():
                Venta0715LG = ven0715LG
                print 'Venta LG Julio 2015 : ' + str(Venta0715LG)
            ven_julLG = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0716LG in ven_julLG.values():
                Venta0716LG= ven0716LG
                print 'Venta LG Julio 2016 : ' + str(Venta0716)
            if ven0716LG == None:
                ven0716LG = 0
            difJulioLG = float 
            difJulioLG = ((float(ven0716LG)/float(ven0715LG)) -1) * 100
            difJulLG = int(ven0715LG)-int (ven0716LG)
            print difJulLG     
            print 'Diferencia Julio: ' + str(difJulioLG) 
             ######### Agosto ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-08-01'
            final15 = '2015-08-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-08-01' 
            final= '2016-08-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_ago_15LG = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0815LG in ven_ago_15LG.values():
                Venta0815LG = ven0815LG
                print 'Venta LG Agosto 2015 : ' + str(Venta0815LG)
            ven_agoLG = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0816LG in ven_agoLG.values():
                Venta0816LG= ven0816LG
                print 'Venta LG Agosto 2016 : ' + str(Venta0816LG)
            if ven0816LG == None:
                ven0816LG = 0
            difAgostoLG = float 
            difAgostoLG = ((float(ven0816LG)/float(ven0815LG)) -1) * 100
            difAgoLG = int(ven0815LG)-int (ven0816LG)
            print difAgoLG     
            print 'Diferencia Agosto: ' + str(difAgostoLG) 
             ######### Septiembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-09-01'
            final15 = '2015-09-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-09-01' 
            final= '2016-09-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_sep_15LG = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0915LG in ven_sep_15LG.values():
                Venta0915LG = ven0915LG
                print 'Venta LG Septiembre 2015 : ' + str(Venta0915LG)
            ven_sepLG = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0916LG in ven_sepLG.values():
                Venta0916LG= ven0916LG
                print 'Venta LG Septiembre 2016 : ' + str(Venta0916LG)
            if ven0916LG == None:
                ven0916LG = 0
            difSeptiembreLG = float 
            difSeptiembreLG = ((float(ven0216)/float(ven0215)) -1) * 100
            difSepLG = int(ven0215)-int (ven0216)
            print difSepLG     
            print 'Diferencia Septiembre: ' + str(difSepLG) 
            ######### Octubre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-10-01'
            final15 = '2015-10-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-10-01' 
            final= '2016-10-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_oct_15LG = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven1015LG in ven_oct_15LG.values():
                Venta1015LG = ven1015LG
                print 'Venta LG Octubre 2015 : ' + str(Venta1015LG)
            ven_octLG = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven1016LG in ven_octLG.values():
                Venta1016LG= ven1016LG
                print 'Venta LG Octubre 2016 : ' + str(Venta1016LG)
            if ven1016LG == None:
                ven1016LG = 0
            difOctubreLG = float 
            difOctubreLG = ((float(ven0216)/float(ven0215)) -1) * 100
            difOctLG = int(ven0215)-int (ven0216)
            print difOctLG     
            print 'Diferencia Octubre: ' + str(difOctubreLG) 
             ######### Noviembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-11-01'
            final15 = '2015-11-30'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-11-01' 
            final= '2016-11-30'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Noviembre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Noviembre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Novimebre: ' + str(difEnero) 
            ######### Diciembre ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-12-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-12-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG Diciembre 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG Diciembre 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Diciembre: ' + str(difEnero)
            ######### 2015 ##########
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-01-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(cliente = 2, **filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta LG 2015 : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(cliente=2, **filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta LG 2016 : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Anual: ' + str(difEnero)
            #############  Venta Bruta ##############
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-01-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(**filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Bruta : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(**filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Bruta : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Anual: ' + str(difEnero)
            ############# Ventas Netas ###############
            filters_mar15 ={}
            filters_mar={}
            inicial15 = '2015-01-01'
            final15 = '2015-12-31'
            filters_mar15['fecha_salida__range']=(inicial15, final15)
            inicial= '2016-01-01' 
            final= '2016-12-31'
            filters_mar['fecha_salida__range']=(inicial, final) 
            ven_mar_15 = Viaje.objects.filter(**filters_mar15).aggregate(Sum('facturacion_flete'))
            for ven0215 in ven_mar_15.values():
                Venta0215 = ven0215
                print 'Venta Neta : ' + str(Venta0215)
            ven_mar = Viaje.objects.filter(**filters_mar).aggregate(Sum('facturacion_flete'))
            for ven0216 in ven_mar.values():
                Venta0216= ven0216
                print 'Venta Neta : ' + str(Venta0216)
            if ven0216 == None:
                ven0216 = 0
            difEnero = float 
            difEnero = ((float(ven0216)/float(ven0215)) -1) * 100
            difEne = int(ven0215)-int (ven0216)
            print difEne     
            print 'Diferencia Anual: ' + str(difEnero)
        ########### FINALIZA LA PRUBA################
         ##### Facturas Samsung 

            fact_sam = Viaje.objects.filter(cliente=1, **filters_viaje)
            for facturas in fact_sam:
                fact = facturas.factura
                fecha_viaje = facturas.fecha_salida 
                print 'Factura : ' + str(fact) + ' con fecha : ' + str(fecha_viaje) 
            #### Facturas LG 
            venta_lg = Viaje.objects.filter(cliente = 2, **filters_viaje).aggregate(Sum('facturacion_flete'), Sum('facturacion_maniobra'), Sum('facturacion_desvio'),
                Sum('facturacion_reparto'), Sum('facturacion_ferri'), Sum('facturacion_ferri'), Sum('facturacion_otros'))
            print venta_lg
            a= 0
            ventatot_lg = 0
            for ven_lg in venta_lg.values():
                venta_lg = ven_lg                
                ventatot_lg = ventatot + venta_lg
                print venta_lg 
                print ventatot_lg
            ##### Facturas LG 
            fact_lg = Viaje.objects.filter(cliente=2, **filters_viaje)
            for facturas in fact_lg:
                fact = facturas.factura
                fecha_viaje = facturas.fecha_salida 
                print 'Factura LG : ' + str(fact) + ' con fecha : ' + str(fecha_viaje) 

        #for datos in infoMensual:
        importe = 'Este es el importe......'    
        #importe = viaje.gastos_salida_total()*Decimal(1.20)
        ##iva = importe*Decimal(0.16) ### Asi se crean los campo para enviarlos desde el return super, self...
        
        return super(ReporteMensualView, self).get_context_data(
            pagesize="A4 landscape",
            title="Carta Porte " + pk, ### Aqui se nombra el archivo de salida.
            fact_lg=fact_lg,### Aqui mandamos el valor de las facturas de LG del mes de enero.
            fact_sam=fact_sam,
            info=info,### Asi mandamos el valor del Arreglo para poder sacarlo por un for en el template o como solo enviamos un registro, lo sacamos en arreglo.campo.
            importe=importe,
            #### clasificacion 'n' = nomina, 'd' = Directivos 
            nd = nd,
            na = na,
            no = no,
            nm = nm,
            nc = nc,
            nt = nt, 
            ##### Movimientos de nomina ########
            mov_alta_adm = str(mov_alta_adm.count()),
            mov_alta_cho = str (mov_alta_cho.count()),
            altas =str(altas),
            bajas = bajas,
            #### Inicia el YTY de Samsung ########
            venta0115 = Venta0115,
            venta0116 = Venta0116,
            difEnero = difEnero,
            venta0215 = Venta0215,
            venta0216 = Venta0216,
            difFebrero = difFebrero,
            venta0315 = Venta0315,
            venta0316 = Venta0316,
            difMarzo = difMarzo,
            venta0415 = Venta0415,
            venta0416 = Venta0416,
            difAbril = difAbril, 
            venta0515 = Venta0515,
            venta0516 = Venta0516,
            difMayo = difMayo, 
            venta0615 = Venta0615,
            venta0616 = Venta0616,
            difJunio = difJunio,
            venta0715 = Venta0715,
            venta0716 = Venta0716,
            difJulio = difJulio,
            venta0815 = Venta0815,
            venta0816 = Venta0816,
            difAgosto = difAgosto,
            venta0915 = Venta0915,
            venta0916 = Venta0916,
            difSeptiembre = difSeptiembre,
            venta1015 = Venta1015,
            venta1016 = Venta1016,
            difOctubre = difOctubre,
            venta1115 = Venta1115,
            venta1116 = Venta1116,
            difNoviembre = difNoviembre,
            venta1215 = Venta1215,
            venta1216 = Venta1216,
            difDiciembre = difDiciembre,
            venta1315 = Venta1315,
            venta1316 = Venta1316,
            difAnual = difAnual,
            ########## Termina el YTY Samsugn #########
            ########## Inicia el YTY LG  #############
            venta0115LG = Venta0115LG,
            venta0116LG = Venta0116LG,
            difEneroLG = difEneroLG,
            venta0215LG = Venta0215LG,
            venta0216LG = Venta0216LG,
            difFebreroLG = difFebreroLG,
            venta0315LG = Venta0315LG,
            venta0316LG = Venta0316LG,
            difMarzolLG = difMarzoLG,
            venta0415LG = Venta0415LG,
            venta0416LG = Venta0416LG,
            difAbrilLG = difAbrilLG,
            venta0515LG = Venta0515LG,
            venta0516LG = Venta0516LG,
            difMayoLG = difMayoLG, 
            venta0615LG = Venta0615LG,
            venta0616LG = Venta0616LG,
            difJunioLG = difJunioLG,
            venta0715LG = Venta0715LG,
            venta0716LG = Venta0716LG,
            difJulioLG = difJulioLG,
            venta0815LG = Venta0815LG,
            venta0816LG = Venta0816LG, 
            difAgostoLG = difAgostoLG,
            venta0915LG = Venta0815LG,
            venta0916LG = Venta0816LG, 
            difSeptiembreLG = difSeptiembreLG,
            venta1015LG = Venta1015LG,
            venta1016LG = Venta1016LG, 
            difOctubreLG = difOctubreLG,
            ### Aqui mandamos el nombre del campo puro y lo recuperamos en el HTML solo con un {{campo}}
            **kwargs
        )


