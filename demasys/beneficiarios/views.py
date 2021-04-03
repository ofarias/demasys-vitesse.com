from django.shortcuts import render, render_to_response,redirect, get_object_or_404
from django.template.context import RequestContext
from django.contrib.auth.decorators import permission_required, login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import messages

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from beneficiarios.models import Benefi
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
from django.db.models import Q
from django.db import connection, transaction
from django.http import QueryDict
from beneficiarios.forms import SearchForm, AgregarForm, EditForm



@login_required

def index(request):
	
	searchform = SearchForm(request.GET)
	
	filters = {}	

	if ('tipo' in request.GET) and request.GET['tipo'].strip():
		filters['tipo']=request.GET['tipo']
	if ('razon_social' in request.GET) and request.GET['razon_social'].strip():
		filters['razon_social']=request.GET['razon_social']
	if ('nombre' in request.GET) and request.GET['nombre'].strip():
		filters['nombre']=request.GET['nombre']
	if ('a_paterno' in request.GET) and request.GET['a_paterno'].strip():
		filters['a_paterno']=request.GET['a_paterno']
	if ('a_materno' in request.GET) and request.GET['a_materno'].strip():
		filters['a_materno']=request.GET['a_materno']
	if ('producto' in request.GET) and request.GET['producto'].strip():
		filters['producto']=request.GET['producto']
	

	beneficiarios = Benefi.objects.filter(**filters)

	if not bool (filters):
		beneficiarios = beneficiarios.order_by('tipo')
	
	paginator = Paginator(beneficiarios, 10)
	page = request.GET.get('page')
	
	try:
		benefic = paginator.page(page)
	except PageNotAnInteger:
		benefic = paginator.page(1)
	except EmptyPage:
		benefic = paginator.page(paginator.num_pages)
	context = RequestContext (request,{
		'searchform':searchform,
		'benefic':benefic,
	})

	return render_to_response ('beneficiarios.html', context)	


@login_required

def agregar(request):
	if request.method=='POST':
		form = AgregarForm(request.POST)
		if form.is_valid():

			ingreso = form.save()
			messages.success(request, 'Se ha registrado el beneficiario')
			return HttpResponseRedirect (reverse ('beneficiarios.views.index'))

		else:
			messages.error(request,'Ha ocurrido un error.')
	else:
		form = AgregarForm()
	context = RequestContext (request,{
		'form':AgregarForm,
		'action':'Agregar',
	})
	return render_to_response ('beneficiario_add.html', context)

@login_required

def editar (request, benefi_id):

	beneficiarios = get_object_or_404(Benefi, pk=benefi_id)	

	if request.method == 'POST':
		form = EditForm(request.POST, instance = beneficiarios)
		if form.is_valid():
			form.save()
			messages.success(request, 'Se ha Actualizado el beneficiario')
			return HttpResponseRedirect (reverse('beneficiarios.views.index'))
		else:
			render_to_response('beneficiaios_edit.html',{'form':form})
			messages.error(request,'No se actulizo, favor de revisar.')
	else:
		form = EditForm(instance=beneficiarios)
	context = RequestContext (request,{
		'form':form,
		'action':'Editar',
	})
	return render_to_response ('beneficiario_edit.html',context)

