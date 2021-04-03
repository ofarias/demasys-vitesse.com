#from twisted.internet.test._posixifaces import in_addr
from django.shortcuts import render
from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from solicitudes.models import Solicitudes, conceptos, TIPO_STATUS, FORMAS_D_PAGO

from empleados.forms import *


from django.forms.models import modelformset_factory, inlineformset_factory

from empleados.models import *

from django.template.defaulttags import register



def solicitudEmpleo(request, idSolicitante):

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
            return HttpResponseRedirect (reverse('externo.views.solicitudEmpleo2',kwargs={'idSolicitante':soli.pk}))
        else:
            messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')

    else:
        defaultEstatus = {'estatus':1}
        form = solicitudForm()

    context = RequestContext (request, {
            'form':form,
            'action' : 'Continuar',
    })
    return render_to_response('solicitud.html', context)


def solicitudEmpleo2(request, idSolicitante):
    formset_familiares  = modelformset_factory(Familiares, form=FamiliaresForm, max_num=10, extra=5, can_delete=True)#, exclude=['idsolicitante'])
    formset_escolaridad = modelformset_factory(Escolaridad, form=EscolaridadForm, max_num=6, extra=5, can_delete=True)
    formset_empleos = modelformset_factory(Empleos, form=EmpleosForm, max_num=4, extra=4, can_delete=True)
    formset_referencia = modelformset_factory(Referencias, form=ReferenciasForm, max_num=4, extra=4, can_delete=True)

    if request.method == 'POST':
        familiaresForm = formset_familiares(request.POST, prefix='fam')
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
            print 'borrrraaaaaaaaaaaaaaaaaaaaaaaaar'
            Familiares.objects.filter(idsolicitante=idSolicitante).delete()
            Escolaridad.objects.filter(idsolicitante=idSolicitante).delete()
            Empleos.objects.filter(idsolicitante=idSolicitante).delete()
            Referencias.objects.filter(idsolicitante=idSolicitante).delete()
            familiaresForm.save()
            escolaridadForm .save()
            empleosForm.save()
            referenciaForm.save()
            messages.success(request, 'Continue respondiendo la solicitud...')
            return HttpResponseRedirect (reverse('externo.views.cuestionario',kwargs={'idSolicitante':idSolicitante}))
        else:
            messages.error(request, 'Por favor, verifique la informacion.')

    else:
        solicitante=[{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},]
        formset_familiares = formset_familiares(initial=solicitante, queryset=Familiares.objects.all().filter(idsolicitante=idSolicitante), prefix='fam')#queryset=Solicitud.objects.all().filter(idsolicitante=idSolicitante))
        formset_escolaridad = formset_escolaridad(initial=solicitante, queryset=Escolaridad.objects.all().filter(idsolicitante=idSolicitante))
        formset_empleos = formset_empleos(initial=solicitante, queryset=Empleos.objects.all().filter(idsolicitante=idSolicitante))
        formset_referencia = formset_referencia(initial=solicitante, queryset=Referencias.objects.all().filter(idsolicitante=idSolicitante))

    context = RequestContext (request, {
            'formset_familiares': formset_familiares,
            'formset_escolaridad':formset_escolaridad,
            'formset_empleos': formset_empleos,
            'formset_referencia':formset_referencia,
            'action' : 'Continuar',
    })
    return render_to_response('solicitud2.html', context)



def cuestionario(request, idSolicitante):
    print 'cuesId' + str(idSolicitante)
    if request.method == 'POST':
        form = InfoGralForm(request.POST)
        print form
        #form.cleaned_data['idsolicitante'] = idSolicitante
        print form
        print 'valido_ ' + str(form.is_valid())
        if form.is_valid():
            InfoGral.objects.filter(idsolicitante=idSolicitante).delete()
            form.save()
            messages.success(request, 'Continue respondiendo el cuestionario...')
            return HttpResponseRedirect (reverse('externo.views.cuestionario2',kwargs={'idSolicitante':idSolicitante}))
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
       print 'valido_ ' + str(form.is_valid())
       print 'valido_ ' + str(formsetHijo.is_valid())
       print formsetHijo

       if form.is_valid() and formsetHijo.is_valid():
           #form.cleaned_data['idsolicitante'] = idSolicitante
           infohijos.objects.all().filter(idsolicitante=idSolicitante).delete()
           Cuestionario.objects.filter(idsolicitante=idSolicitante).delete()
           form.save()
           formsetHijo.save()
           messages.success(request, 'Gracias, ha finalizado el proceso.')
           return render_to_response('finaliza.html')
       else:
           messages.error(request, 'Ha ocurrido algun error, verifique los datos por favor.')
    else:
        precarga=[{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,},{'idsolicitante': idSolicitante,}]

        hijosFormSet = hijosFormSet(initial=precarga,queryset=infohijos.objects.all().filter(idsolicitante=idSolicitante))
        try:
            solicitante = Cuestionario.objects.get(idsolicitante=idSolicitante)
            form = CuestionarioForm(initial={'idsolicitante':idSolicitante}, instance=solicitante)
        except ObjectDoesNotExist:
            form = CuestionarioForm(initial={'idsolicitante':idSolicitante})


    context = RequestContext (request, {
            'form':form,
            'hijosFormSet':hijosFormSet,
            'action' : 'Finalizar',
    })

    return render_to_response('Cuestionario2.html', context)



@register.filter
def get_item(dictionary, key):
    key = int(key)
    dato = dictionary[key - 1]
    return dato[1]