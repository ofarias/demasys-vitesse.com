# coding: utf-8
from django.shortcuts import render
from forms import InventarioUploadForm, ProductoForm, reporteForm, MovimientosForm, MovimientosAddForm
from models import Productos, ExcelUpload, Movimientos
from django.contrib import messages
import openpyxl
from django.conf import settings
import os
from django.contrib.auth.decorators import permission_required, login_required
from django.core.exceptions import ObjectDoesNotExist
from decimal import Decimal
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.template.context import RequestContext
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
import xlwt
from xlwt import Workbook,XFStyle,Borders, Pattern, Font, easyxf
from django.http.response import HttpResponseRedirect, HttpResponse
from datetime import datetime


# Create your views here.

@login_required
def ExcelInventario(request):

    if request.method == 'POST':
        form = InventarioUploadForm(request.POST, request.FILES)


        if form.is_valid():
            newdoc = ExcelUpload(docfile = request.FILES['docfile'])
            nombreArchivo = str(newdoc.docfile)
            nombreArchivo = nombreArchivo.upper()
            if nombreArchivo.endswith('.XLSX'):
                newdoc.save()
                registraInventarioExc(request, str(newdoc.docfile))
                ExcelUpload.objects.all().delete()
            else:
                txtmsg = 'Archivo con formato inválido.'
                messages.error(request, txtmsg)

        return render(request,'subirInventario.html', {'form': form,})
    else:
        form = InventarioUploadForm()
    return render(request,'subirInventario.html', {'form': form,})


def registraInventarioExc(request, datoArchivo):
    user = request.user
    workbook = openpyxl.load_workbook(filename=settings.MEDIA_ROOT + datoArchivo, use_iterators=True)
    try:
        sheet = workbook.get_sheet_by_name('Inventario')
        exitos = 0
        numError = 0
        total = 0
        filasT = sheet.get_highest_row() + 1
        for row in range(2, filasT):
            total += 1
            try:
                movimientos = Movimientos()
                movimientos.fecha = sheet['C' + str(row)].value
                movimientos.costo = sheet['D' + str(row)].value
                movimientos.factor = sheet['E' + str(row)].value
                movimientos.unidades = sheet['B' + str(row)].value
                movimientos.movimiento = 'E'

                producto = Productos()
                producto.descripcion = sheet['A' + str(row)].value
                producto.existencia = float(movimientos.unidades * movimientos.factor)
                producto.costoUnitario = float(movimientos.costo / producto.existencia)
                producto.activo = 1

                prodBase = None
                try:
                    prodBase = Productos.objects.get(descripcion__iexact = sheet['A' + str(row)].value)
                except ObjectDoesNotExist:
                    prodBase = None

                if prodBase is None:
                    producto.save()
                    movimientos.idProducto = producto
                else:
                    movimientos.idProducto = prodBase
                    #Actualiza existencia & costos unitarios
                    existenciaActual = prodBase.existencia
                    prodBase.existencia = existenciaActual + Decimal(producto.existencia)
                    prodBase.costoUnitario = producto.costoUnitario
                    prodBase.save()

                movimientos.save()
                exitos += 1

            except KeyError:
                messages.error(request, u'Error al registrar el producto ' + str(sheet['A' + str(row)].value) + u' Verifique los datos')
                numError += 1


        archivoF = settings.MEDIA_ROOT +  datoArchivo
        os.remove(archivoF)
        if exitos == 0:
            messages.error(request, 'No se registraron los movimientos a Inventarios')
        if numError == 0:
            messages.success(request, 'Movimientos registrados exitosamente.')
        if exitos > 0 and numError > 0:
            messages.success(request, 'Carga parcial de Inventarios-compras.')

    except KeyError:
        messages.error(request, 'Archivo no contiene la hoja Inventario')

@login_required
def productos(request):
    productos_list = Productos.objects.all()
    paginator = Paginator(productos_list, 10)
    page = request.GET.get('page')

    try:
        productos = paginator.page(page)
    except PageNotAnInteger:
        productos = paginator.page(1)
    except EmptyPage:
        productos = paginator.page(paginator.num_pages)

    context = RequestContext(request,{
        'productos': productos,
    })

    return render_to_response('productos.html', context)

@login_required
def productoadd(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            prod = form.save(commit = False)
            prod.existencia = 0
            prod.costoUnitario = 0  
            prod = form.save()
            messages.success(request, 'Se ha agregado el producto %s' % prod.descripcion)
            return HttpResponseRedirect(reverse('inventario.views.productos',))
        else:
            messages.error(request, 'Ha ocurrido un error. Por favor verifique los datos.')
    else:
        form = ProductoForm()

    context = RequestContext(request,{
        'form': form,
        'action': 'Agregar',
    })

    return render_to_response('producto_form.html', context)

@login_required
def productoedit(request, producto_id):
    prodDato = get_object_or_404(Productos, pk=producto_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=prodDato)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado el producto %s' % prodDato.descripcion)
            return HttpResponseRedirect(reverse('inventario.views.productos',))
        else:
            messages.error(request, 'Ha ocurrido un error. Por favor verifique los datos.')
    else:
        form = ProductoForm(instance=prodDato)

    context = RequestContext(request,{
        'form': form,
        'action': 'Editar',
    })

    return render_to_response('producto_form.html', context)

@login_required
def productodelete(request, producto_id):
    prodDato = get_object_or_404(Productos, pk=producto_id)

    message = 'El producto %s ha sido eliminado.'%  prodDato.descripcion
    prodDato.delete()

    messages.success(request, message)
    return HttpResponseRedirect(reverse('inventario.views.productos',))

@login_required
def reporteMovimientos(request):

    form = reporteForm
    if request.method == "POST":
        form = reporteForm(request.POST)
        if form.is_valid():
            formExc = form.cleaned_data
            prod = formExc['producto']

            filters = {}
            filters['fecha__range'] = (formExc['fecha_from'], formExc['fecha_to'])
            filters['movimiento'] = formExc['tipo']
            if formExc['producto'] is not None:
                print 'no es vacio'
                filters['idProducto'] = prod.id

            movimientos = Movimientos.objects.filter(**filters)


            wb = xlwt.Workbook(encoding='utf8')
            ws = wb.add_sheet('Reporte')
            date_format = xlwt.XFStyle()
            date_format.num_format_str = 'dd/mm/yyyy'
            formatoNum = XFStyle()
            formatoNum.num_format_str = '$ #,##0.00'
            font = xlwt.Font() # Crear Font
            font.name = 'Arial'
            font.height = 20 * 12  #22pt
            font.bold = True
            font.italic = True
            style = xlwt.XFStyle() # Crar Style
            style = xlwt.easyxf('pattern: pattern solid, fore_colour light_blue;') #background color
            style.font = font

            columnas = [
                    (u"Producto", 70),
                    (r'Fecha de Compra', 15),
                    (u"Costo", 70),
                    (u"Unidades", 70),
                    (u"Factor", 70),
                    (u"Num. Solicitud", 70),
                    (u"Economico", 70),
            ]

            posx = 0
            for col in xrange(len(columnas)):
                ws.write(0, posx, columnas[col][0])
                posx += 1

            renglon = 1
            excelGenerado = False
            if movimientos.count():
                for mov in movimientos:
                    try:
                        prod = mov.idProducto
                        ws.write(renglon, 0, prod.descripcion)
                        ws.col(0).width=4500
                        ws.write(renglon, 1, mov.fecha, date_format)
                        ws.col(0).width=4000
                        ws.write(renglon, 2, mov.costo, formatoNum)
                        ws.col(0).width=3000
                        ws.write(renglon, 3, mov.unidades)
                        ws.col(0).width=3000
                        ws.write(renglon, 4, mov.factor)
                        ws.col(0).width=3000
                        ws.write(renglon, 5, mov.idSolicitud)
                        ws.col(0).width=3000
                        ws.write(renglon, 6, mov.idEconomico)
                        ws.col(0).width=3000

                        renglon += 1
                    except ObjectDoesNotExist:
                        renglon += 1
                        #print 'No existe Producto relacionado'
                    except ObjectDoesNotExist as detalle:
                        renglon += 1
                        print 'Error no existen datos:', detalle

                excelGenerado = True

            else:
                messages.warning(request, 'No se encontraron registros con los criterios seleccionados')
                form = reporteForm(request.POST)
                return render(request,'reporteMovimientos.html', {'form': form,})

            if excelGenerado:
                response = HttpResponse(mimetype="application/vnd.ms-excel")
                response['Content-Disposition'] = 'attachment; filename=reporte.xls'
                wb.save(response)
                return response

        else:
            messages.error(request, 'Algunos campos son requeridos.')
        print 'genera excel'
    else:

        form = reporteForm
    context = RequestContext(request,{
        'form': form,
    })
    return render_to_response('reporteMovimientos.html', context)

def movimiento_asig(request):

    
    if request.method == 'POST':
 
       form = MovimientosForm(request.POST)
       
       if form.is_valid():
          
           prod = request.POST['idProducto']      
           prodBase = Productos.objects.get(id = prod) 
           cant = request.POST['unidades'] 

           existenciaActual = prodBase.existencia  

           prodBase.existencia = existenciaActual - Decimal(cant) 
           prodBase.save() 
           form.save() 
             
           messages.success(request, 'Se ha registrado el movimiento')
           return HttpResponseRedirect  (reverse('inventario.views.productos'))
       else: 
           messages.error(request, 'No se ha registrado el movimiento')

    else:

        form = MovimientosForm()

    context = RequestContext (request, {
            'form' : form, 
            'action': 'Asignar',
})
    return render_to_response('movimiento_asig.html', context)

def movimiento_add(request):

    
    if request.method == 'POST':
 
       form = MovimientosAddForm(request.POST)
       
       if form.is_valid():
          
           prod = request.POST['idProducto']    
           prodBase = Productos.objects.get(id = prod) 
           cant = request.POST['unidades'] 
           costoNuevo = request.POST['costo']
           existenciaActual = prodBase.existencia
           prodBase.costoUnitario = costoNuevo
           prodBase.existencia = existenciaActual + Decimal(cant) 
           prodBase.save() 
           form.save() 
             
           messages.success(request, 'Se ha registrado el movimiento')
           return HttpResponseRedirect  (reverse('inventario.views.productos'))
       else: 
           messages.error(request, 'No se ha registrado el movimiento')

    else:

        form = MovimientosAddForm()

    context = RequestContext (request, {
            'form' : form, 
            'action': 'Comprar',
})
    return render_to_response('movimiento.html', context)

