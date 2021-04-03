# coding: utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages

from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from clientes.models import Cliente, Departamento
from clientes.forms import ClienteForm, DepartamentoForm
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader

@login_required
def index(request):
    clientes_list = Cliente.objects.all()
    paginator = Paginator(clientes_list, 10)
    page = request.GET.get('page')

    try:
        clientes = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        clientes = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        clientes = paginator.page(paginator.num_pages)
    
    context = RequestContext(request,{ 
        'clientes': clientes,                         
    })    
    
    return render_to_response('clientes.html', context)

@login_required
def agregar(request):    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, 'Se ha agregado el cliente: %s'%cliente)
            return HttpResponseRedirect(reverse('clientes.views.index',))
        else:
            messages.error(request, 'Ha ocurrido un error. Por favor verifique los datos.')
    else:
        form = ClienteForm()
    
    context = RequestContext(request,{ 
        'form': form,
        'action': 'Agregar',
    })    
    
    return render_to_response('clientes_form.html', context)

@login_required
def editar(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Se ha editado el cliente: %s'%cliente)
            return HttpResponseRedirect(reverse('clientes.views.index',))
        else:
            messages.error(request, 'Ha ocurrido un error. Por favor verifique los datos.')
    else:
        form = ClienteForm(instance=cliente)
        
    context = RequestContext(request,{ 
        'form': form,
        'action': 'Editar',
    })    
    
    return render_to_response('clientes_form.html', context)

@login_required
def departamentos(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)    
    
    context = RequestContext(request,{         
        'cliente': cliente,
    })    
    
    return render_to_response('departamentos.html', context)

@login_required
@csrf_exempt
def departamentoadd(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    status = 'OK'
    use_json = False
    if request.method == 'POST':
        use_json = True
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            departamento = form.save(commit=False)
            departamento.cliente = cliente
            departamento.save()
            #messages.success(request, 'Se ha agregado el departamento: %s'%departamento)
            #return HttpResponseRedirect(reverse('clientes.views.index',))
        else:
            status = 'Error'
            #messages.error(request, 'Ha ocurrido un error. Por favor verifique los datos.')
    else:
        form = DepartamentoForm()
    
    context = RequestContext(request,{ 
        'cliente': cliente,
        'form': form,
        'action': 'Agregar',
    })    
    
    if use_json:
        t = loader.get_template('departamento_form.html')
        html = t.render(context)
        if status != 'OK':
            return HttpResponse(json.dumps({'status':status, 'html':html}), mimetype="application/json")
        else:
            return HttpResponse(json.dumps({'status':status, 'departamento':departamento.departamento, 'id':departamento.pk, 'activo': departamento.activo}), mimetype="application/json")
    else:    
        return render_to_response('departamento_form.html', context)

@login_required
@csrf_exempt    
def departamentoedit(request, departamento_id):
    departamento = get_object_or_404(Departamento, pk=departamento_id)
    status = 'OK'
    use_json = False
    
    if request.method == 'POST':
        use_json = True
        form = DepartamentoForm(request.POST, instance=departamento)
        if form.is_valid():
            form.save()            
        else:
            status = 'Error'
    else:
        form = DepartamentoForm(instance=departamento)
        
    context = RequestContext(request,{ 
        'form': form,
        'departamento': departamento,
        'action': 'Editar',
    })     
    
    if use_json:
        t = loader.get_template('departamento_form.html')
        html = t.render(context)
        if status != 'OK':
            return HttpResponse(json.dumps({'status':status, 'html':html}), mimetype="application/json")
        else:
            return HttpResponse(json.dumps({'status':status, 'departamento':departamento.departamento, 'id':departamento.pk, 'activo': departamento.activo}), mimetype="application/json")
    
    return render_to_response('departamento_form.html', context)

def recoleccion(request, cliente_id):
    cliente = Cliente.objects.values('recoleccion_clave_municipio', 'recoleccion_colonia', 'recoleccion_calle', 'recoleccion_numero', 'recoleccion_cp').get(pk=cliente_id)
    return HttpResponse(json.dumps(cliente), mimetype="application/json")
    
# def eliminar(request, cliente_id):
#     cliente = get_object_or_404(Cliente, pk=cliente_id)
#     
#     message = 'El cliente %s ha sido eliminado.'%cliente
#     cliente.delete()
#     
#     messages.success(request, message)
#     return HttpResponseRedirect(reverse('clientes.views.index',))  
