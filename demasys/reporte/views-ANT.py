from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import permission_required, login_required
from reporte.models import ing_egre, nomina, MESES, CLIENTE
from reporte.forms import *
from django.contrib import messages
from django.template.loader import get_template
from django.template.defaulttags import register
from django.template import Context
from django.conf import settings
import sys, os
from xhtml2pdf import pisa


# Create your views here.
@login_required
def agregar(request):
    if request.method=='POST':
        form = IngresosEgresosForm(request.POST)
        if form.is_valid():
            ingreso = form.save()
            messages.success(request, 'Se ha registrado el beneficiario')
            #return HttpResponseRedirect (reverse ('beneficiarios.views.index'))
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
def agregarNomina(request):
    if request.method=='POST':
        form = NominaForm(request.POST)
        if form.is_valid():
            #ingreso = form.save()
            messages.success(request, 'Se ha registrado el beneficiario')
            #return HttpResponseRedirect (reverse ('beneficiarios.views.index'))
        else:
            messages.error(request,'Ha ocurrido un error.')
    else:
        form = NominaForm()
    context = RequestContext (request,{
        'form':NominaForm,
        'action':'Agregar',
    })
    return render_to_response ('ingreNom_form.html', context) 

@login_required
def agregarBruta(request):
    if request.method=='POST':
        form = BrutaForm(request.POST)
        if form.is_valid():
            #ingreso = form.save()
            messages.success(request, 'Se ha registrado el beneficiario')
            #return HttpResponseRedirect (reverse ('beneficiarios.views.index'))
        else:
            messages.error(request,'Ha ocurrido un error.')
    else:
        form = BrutaForm()
    context = RequestContext (request,{
        'form':BrutaForm,
        'action':'Agregar',
    })
    return render_to_response ('ingreBruta_form.html', context)    

@login_required
def agregarNeta(request):
    if request.method=='POST':
        form = NetaForm(request.POST)
        if form.is_valid():
            #ingreso = form.save()
            messages.success(request, 'Se ha registrado el beneficiario')
            #return HttpResponseRedirect (reverse ('beneficiarios.views.index'))
        else:
            messages.error(request,'Ha ocurrido un error.')
    else:
        form = NetaForm()
    context = RequestContext (request,{
        'form':NetaForm,
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