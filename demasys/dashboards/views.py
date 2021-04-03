# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import permission_required, login_required
from django.utils.dateformat import format
from django.db.models import Q

from datetime import date, timedelta,datetime
from dateutil.relativedelta import relativedelta
import json
import xlwt
from viajes.models import ViajeStatus, Viaje, Destino, ReporteUnidad, MovUnidad
from django.db.models.aggregates import Count, Max, Min
from django.http.response import HttpResponse, HttpResponseRedirect
#agregado JC
from django.core.mail import send_mail
from empleados.models import empleado
from cuentas.models import Perfil
from solicitudes.models import Solicitudes
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str
import mimetypes
import datetime


@login_required
def index(request):

    userid = request.user.id 
    user = request.user
    u1= Perfil.objects.get(user_id=userid)

    hoy = date.today()
    sol_vencida = Solicitudes.objects.filter(status = 4)###Obtenemos las pagadas
    for sol in sol_vencida:
        fv = sol.fecha_vencimiento
        ##print 'Esta es la solicitud'
        ##print str(sol.pk)

        if fv and fv < hoy :
            ######vencida = Solicitudes.objects.filter(pk=sol.pk).update(status = 6)
            ##emp= empleado.objects.filter(id = sol.solicitante).update(status = 1)
            print '<--- ' + str(sol.pk)
    
    if userid == 80 or userid == 81 or userid == 82:
        messages.success(request, 'Bienvenido: %s , en este modulo podras ver la informacion que el personal de Logistica Vitesse comparte con sus clientes.'%u1)
        return HttpResponseRedirect(reverse('viajes.views.indexArchivos'))

    if userid >= 20:
        messages.success(request, 'El Usuario es: %s'%u1)
        return HttpResponseRedirect(reverse('viajes.views.agregaMovimiento' ))

    ##Operadores_list = Operadores_list = empleado.objects.filter(Q(puesto_id=8)|Q(puesto_id=9)|Q(puesto_id =10)|Q(puesto_id = 11)|Q(puesto_id = 12), status = 1 ).order_by('lic_vigencia')
    ##misOperadores   = []
    ##if Operadores_list:
    ##    for operador in Operadores_list:
    ##        today       = date.today()
    ##        today7      = today + timedelta(days=7)
    ##        vigencia    = operador.lic_vigencia
    ##        fechamas    = today7
    ##        nombre      = 'NOMBRE:  ' + operador.nombre +' '+ operador.segundo_nombre +' '+ operador.apellidop +' '+ operador.apellidom + ' \n FECHA VIGENCIA: ' + str(vigencia) + '\n\n'   
    ##        if operador.lic_vigencia == None:
    ##            print "vacio"
    ##        else:
    ##            if  vigencia > fechamas:
    ##                print "fin" 
    ##            else:
    ##                print "manda Email" 
    ##                misOperadores.append(nombre)
    ##
    ##    	    msg1 = 'LISTA DE OPERADORES CON LICENCIA DE VIGENCIA CADUCADA  \n\n\n\n'
    ##                msg2 = '-----------------------------------------------------------------\n '.join(misOperadores)
    ##                msg3 = '\n\n\n\n Contacto: \n\n  departamento de sistemas. '
    ##                msg  = msg1 + msg2 + msg3 
    ##	       ##  send_mail('VIGENCIA DE LICENCIA OPERADORES', msg, 'controladministrativo@logisticavitesse.com.mx',
    ##	       ##    ['carlos@logisticavitesse.com.mx', 'esin_garandad@yahoo.com.mx', 'julio@logisticavitesse.com.mx', 'jonathan@logisticavitesse.com.mx', 'mario@logisticavitesse.com.mx', 'victor@logisticavitesse.com.mx', 'alejandromc@logisticavitesse.com.mx', 'cinthia@logisticavitesse.com.mx', 'mara@logisticavitesse.com.mx'], fail_silently=False)

    revision_List = revision_List = ReporteUnidad.objects.filter(status=1)
    misRevisiones=[]
    if revision_List:
        for revision in revision_List:
            unidad = str(revision.reporta)
            reporte = str(revision.pk)
            info = 'Reporte No: ' + reporte + ', de la unidad : ' + unidad + '.'
            misRevisiones.append(info)

        #print 'Manda correo Con Pendientes por revisar'
        msg1 = 'LISTA DE UNIDADES PENDIENTES POR REVISAR : \n\n\n'
        msg2 = '--------------------------------------- \n '.join(misRevisiones)
        msg3 = '\n\n\n\n Contacto: \n\n  departamento de sistemas. '
        msg = msg1 + msg2 + msg3

    ##  send_mail('IMPORTANTE CONTROL ADMINISTRATIVO, TE INFORMA QUE EXISTE UN REPORTE DE UNIDAD PENDIENTE POR  REVISAR', msg, 'controladministrativo@logisticavitesse.com.mx',  
    ##  ['julio@logisticavitesse.com.mx', 'victor@logisticavitesse.com.mx', 'alejandromc@logisticavitesse.com.mx', 'griselda@logisticavitesse.com.mx'], fail_silently=False)
      
        #['genseg@hotmail.com'], fail_silently=False)  
        #print 'Mensaje enviado'
    
    autorizar_List = ReporteUnidad.objects.filter(status=7)
    misRevisadas=[]
    if autorizar_List:
        for autorizar in autorizar_List:
            unidad = autorizar.reporta
            misRevisadas.append(str(unidad))

        #print 'Manda correo Con Pendientes por autorizar'

        msg1 = 'LISTA DE UNIDADES PENDIENTES POR AUTORIZAR : \n\n\n '
        msg2 = '--------------------------------------- \n '.join(misRevisadas)
        msg3 = '\n\n\n\n Contacto: \n\n  departamento de sistemas. '
        msg = msg1 + msg2 + msg3

    ##    send_mail(' IMPORTANTE CONTROL ADMINISTRATIVO, TE INFORMA QUE EXISTE UN REPORTE DE UNIDAD PENDIENTE POR AUTORIZAR', msg, 'controladministrativo@logisticavitesse.com.mx', 
    ##    ['julio@logisticavitesse.com.mx', 'victor@logisticavitesse.com.mx', 'alejandromc@logisticavitesse.com.mx'], fail_silently=False)
      
        #['genseg@hotmail.com'], fail_silently=False)           
        #print 'Mensaje enviado'


    ######## enviar correo de los viajes no facturados  ###########

    ##viajes_Sin_Factura= Viaje.objects.filter(factura = None)
    ##today = date.today()
    ##listadoVSF = []
    ##for vsf in viajes_Sin_Factura:
    ##    viajesSinFactura = 'El viaje :' + str(vsf.pk) + ', del cliente '+ str(vsf.cliente) + ' , con fecha de Salida: ' + str(vsf.fecha_salida) + ' y con fecha de cierre ' + str(vsf.fecha_entmcia) + ', no se encuentra Facturado' + '\n\n'
    ##    if vsf.fecha_entmcia and vsf.factura != 'Cancelado':
    ##        fecha = vsf.fecha_entmcia
    ##        fecha10 = fecha + timedelta(days=10)
    ##        if today > fecha10:
    ##            ##print 'El viaje: '+ str(vsf.pk) + ', del cliente '+ str(vsf.cliente) +', con la Fecha de Salida del ' + str(fecha) + 'y fecha de entrega ' + str(vsf.fecha_entmcia) 
    ##            listadoVSF.append(viajesSinFactura)
    ##            ##print 'Envia correo'
    ##        else:
    ##            ##print 'No en la lista'
    ##msg1 = 'LISTA DE VIAJES NO FACTURADOS  \n\n\n\n'
    ##msg2 = '-----------------------------------------------------------------\n '.join(listadoVSF)
    ##msg3 = '\n\n\n\n Contacto: \n\n  departamento de sistemas. '
    ##msg  = msg1 + msg2 + msg3

    ##send_mail('LISTA DE VIAJES NO FACTURADOS', msg, 'controladministrativo@logisticavitesse.com.mx',
    ##['ivonne@logisticavitesse.com.mx', 'alejandromc@logisticavitesse.com.mx', 'mara@logisticavitesse.com.mx', 'griselda@logisticavitesse.com.mx', 'carlos@logisticavitesse.com.mx'], fail_silently=False)

    ##['ivonne@logisticavitesse.com.mx', 'alejandromc@logisticavitesse.com.mx', 'mara@logisticavitesse.com.mx', 'griselda@logisticavitesse.com.mx', 'carlos@logisticavitesse.com.mx'], fail_silently=False)


    ########## Acutaliza color de los viajes cerrados hace 7 dias y que no esten facturados ####

    ##for vnf in viajes_Sin_Factura:
    ##    if vnf.fecha_entmcia != None:
    ##        print vnf.id
    ##        ##print 'Viaje Cerrado'
    ##        print vnf.fecha_entmcia
    ##        ##print 'Fecha de cierre'
    ##        fechaSalida =vnf.fecha_salida
    ##        fechaMaxima = fechaSalida + timedelta(days=7)
    ##        if today > fechaMaxima and vnf.status_doc <= 7:
    ##            #print 'Estos viajes superan los 15 dias sin factura despues de su cierre'
    ##            #print vnf.id
    ##            sa= vnf.status_doc
    ##            ns= sa + 10
    ##            Viaje.objects.filter(pk = str(vnf.id)).update(status_doc=ns)


    ############ enviar correos con los viajes del dia de ayer solo 1 ves##########

#   lista_viajes_ayer=MovUnidad.objects.filter(email=0)
#   today=datetime.timedelta(days=0)
#   # La fecha de hoy es:
#   hoy = date.today()
#   # Para calcular la de ayer, restamos un día
#   ayer = hoy + datetime.timedelta(days=-1)
#   print ayer
#    # Y para mañana, sumamos un día
#    manana = hoy + datetime.timedelta(days=1)
#    print type(manana)
#    print 'tipos de fecha'
#    print type(today)
#    listadoVA =[]
#    for va in lista_viajes_ayer:
#        lista = str(va.destino2)
#        lista1 =  str(va.cliente)
#        lista2 =  str(va.departamento) 
#        lista3 = str(va.unidad) 
#        lista4 = str(va.operador) 
#        lista5 = str(va.destino) 
#        lista6 = (va.obs)
#        lista7 = '------------'
#        if va.ts and va.ts < hoy:
#            listadoVA.append(lista)
#            listadoVA.append(lista1)
#            listadoVA.append(lista2)
#            listadoVA.append(lista3)
#            listadoVA.append(lista4)
#            listadoVA.append(lista5)
#            listadoVA.append(lista6)
#            listadoVA.append(lista7)
#            MovUnidad.objects.filter(destino2=va.destino2).update(email = 1) 
#    if listadoVA:
#        msg1 = ' VIAJES DIARIOS \n\n\n'
#        msg2 = '\n '.join(listadoVA)
#        msg3 = '\n\n\n Contacto: \n\n  departamento de sistemas. '
#        msg  = msg1 + msg2 + msg3
#        print listadoVA
    ##    send_mail('LISTA DE VIAJES DIARIO', msg, 'controladministrativo@logisticavitesse.com.mx',
    ##    ['griselda@logisticavitesse.com.mx', 'alejandromc@logisticavitesse.com.mx'], fail_silently=False)
    ##['griselda@logisticavitesse.com.mx', 'alejandromc@logisticavitesse.com.mx'], fail_silently=False)

    today = date.today()

    viajes = ViajeStatus.objects.filter(created_on__year=today.year,
                           created_on__month=today.month)
    
    #Destinos
    destinos = Destino.objects.filter(viaje__fecha_salida__year=today.year,
                           viaje__fecha_salida__month=today.month).values('destino_clave_municipio').annotate(num_visitas=Count('destino_clave_municipio'))
                           
    #Viajes por economico
    economicos = Viaje.objects.filter(fecha_salida__year=today.year,
                           fecha_salida__month=today.month).values('economico__placas').annotate(num_viajes=Count('economico'))
                           
    #Status
    nuevas = ViajeStatus.objects.filter(workflowactivity__fecha_salida__year=today.year,
                           workflowactivity__fecha_salida__month=today.month, state = 1).count()
                           
    autorizadas = ViajeStatus.objects.filter(workflowactivity__fecha_salida__year=today.year,
                           workflowactivity__fecha_salida__month=today.month, state = 2).count()      
                           
    enruta = ViajeStatus.objects.filter(workflowactivity__fecha_salida__year=today.year,
                           workflowactivity__fecha_salida__month=today.month, state__in = [3,4,5]).count() 
                           
    facturacion = ViajeStatus.objects.filter(workflowactivity__fecha_salida__year=today.year,
                           workflowactivity__fecha_salida__month=today.month, state = 7).count() 
                           
    all_status = ViajeStatus.objects.values('state__name').filter(workflowactivity__fecha_salida__year=today.year,
                           workflowactivity__fecha_salida__month=today.month).annotate(data=Count('state'))

    fechas = Viaje.objects.all().aggregate(Max('fecha_salida'), Min('fecha_salida'))    
    fecha_final = fechas['fecha_salida__max'].replace(day=1)
    fecha_inicio = fechas['fecha_salida__min'].replace(day=1)    
    dates_range = []
    
    while fecha_inicio <= fecha_final:        
        dates_range.append(fecha_inicio)
        fecha_inicio += relativedelta(months=1)    
        
    dates_range.sort(reverse=True)         
                           
    status = json.dumps(list(all_status))
    status = status.replace('state__name', 'label')
    
    context = RequestContext(request,{ 
        'viajes': viajes,
        'destinos': destinos,       
        'economicos': economicos,   
        'nuevas': nuevas,    
        'autorizadas': autorizadas,
        'enruta': enruta,
        'facturacion': facturacion,    
        'all_status': status,
        'dates_range': dates_range,          
    })    
    
    return render_to_response('index.html', context)

@login_required
def reporte(request, year, month):
    response = HttpResponse(mimetype="application/vnd.ms-excel")
    response['Content-Disposition'] = 'attachment; filename=reporte-%s-%s.xls'%(month, year)
    
    fecha_reporte = date(year=int(year), month=int(month), day=1)
    viajes = ViajeStatus.objects.filter(workflowactivity__fecha_salida__year=year,
                           workflowactivity__fecha_salida__month=month)
    
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Reporte')
    
    date_format = xlwt.XFStyle()
    date_format.num_format_str = 'dd/mm/yyyy'
    
    ws.write(0, 0, format(fecha_reporte, "F Y"))
    
    ws.write(1, 0, 'Carta Porte')
    ws.write(1, 1, 'Status')
    ws.write(1, 2, 'Economico')
    ws.write(1, 3, 'Cliente')
    ws.write(1, 4, 'Operador')
    ws.write(1, 5, 'Destino')
    ws.write(1, 6, 'Load/Bill')
    ws.write(1, 7, 'Fecha Salida')
    ws.write(1, 8, 'Gastos de Salida')
    ws.write(1, 9, 'Gastos de Regreso')
    ws.write(1, 10, 'No. Factura')
    ws.write(1, 11, 'Flete')
    ws.write(1, 12, 'Casetas')
    ws.write(1, 13, 'Maniobra')
    ws.write(1, 14, 'Reparto')
    ws.write(1, 15, u'Desvío')
    ws.write(1, 16, 'Ferri')
    ws.write(1, 17, 'Otros')
    ws.write(1, 18, 'Subtotal')
    ws.write(1, 19, 'IVA')    
    ws.write(1, 20, u'Retención')
    ws.write(1, 21, 'Total')
    ws.write(1, 22, 'Observaciones')
    
    renglon = 2
    for viaje in viajes:
        #destinos = viaje.destino_set.all
        
        ws.write(renglon, 0, viaje.workflowactivity.pk)
        ws.write(renglon, 1, viaje.state.name)
        ws.write(renglon, 2, viaje.workflowactivity.economico.pk)
        ws.write(renglon, 3, viaje.workflowactivity.cliente.nombre_corto)
        ws.write(renglon, 4, viaje.workflowactivity.operador.__unicode__())
        ws.write(renglon, 5, viaje.workflowactivity.get_destinos())
        ws.write(renglon, 6, viaje.workflowactivity.referencia)
        ws.write(renglon, 7, viaje.workflowactivity.fecha_salida, date_format)
        ws.write(renglon, 8, viaje.workflowactivity.gastos_salida_total())
        ws.write(renglon, 9, viaje.workflowactivity.gastos_regreso_total())
        ws.write(renglon, 10, viaje.workflowactivity.factura)
        ws.write(renglon, 11, viaje.workflowactivity.facturacion_flete)
        ws.write(renglon, 12, viaje.workflowactivity.facturacion_casetas)
        ws.write(renglon, 13, viaje.workflowactivity.facturacion_maniobra)
        ws.write(renglon, 14, viaje.workflowactivity.facturacion_reparto)
        ws.write(renglon, 15, viaje.workflowactivity.facturacion_desvio)
        ws.write(renglon, 16, viaje.workflowactivity.facturacion_ferri)
        ws.write(renglon, 17, viaje.workflowactivity.facturacion_otros)
        ws.write(renglon, 18, viaje.workflowactivity.subtotal)
        ws.write(renglon, 19, viaje.workflowactivity.iva)
        ws.write(renglon, 20, viaje.workflowactivity.retencion)
        ws.write(renglon, 21, viaje.workflowactivity.total)
        ws.write(renglon, 22, viaje.workflowactivity.observaciones)
             
        renglon += 1

    wb.save(response)
    return response
    
    
    
