# coding: utf-8
from django.template.context import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail

#from forms import UsuarioForm, PerfilModelForm,PermissionGroup

from forms import UsuarioForm, PerfilModelForm


from models import Perfil
from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from cuentas.forms import UsuarioPerfilForm
######################################################################################
import json
from django.views.decorators.csrf import csrf_exempt
#from django.contrib.auth.models import User,Group,Permission
##JC



@login_required
def usuarios(request):
    user = request.user
    profile = user.get_profile()
    
    usuarios_list = Perfil.objects.all()
    paginator = Paginator(usuarios_list, 10)
    page = request.GET.get('page')
    
    try:
        usuarios = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        usuarios = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        usuarios = paginator.page(paginator.num_pages)
    
    context = RequestContext(request,{
        'usuarios': usuarios,
    })
    return render_to_response('usuarios.html', context)


@login_required
def agregar_usuario(request):
    user = request.user
    profile = user.get_profile()
    form = UsuarioForm()
    form2 = PerfilModelForm()

    if request.method == "POST":
        form = UsuarioForm(request.POST)
        form2 = PerfilModelForm(request.POST)
        listaValores = request.POST.getlist('user_permissions')

        #todosPermisos = Permission.objects.all()
        #user.user_permissions.clear()
        #for i in todosPermisos:           
        #    if str(i.id) in listaValores:
        #        print str(i.id)
        #        user.user_permissions.add(i)
        user.user_permissions.add()


        if form.is_valid() and form2.is_valid():
            usuario = form.save(commit=False)
            password = User.objects.make_random_password(8)
            usuario.set_password(password)
            usuario.save()
            form.save_m2m() #guardar los muchos-a-muchos 
            
            perfil = form2.save(commit=False)
            perfil.user = usuario
            perfil.save()
            form2.save_m2m()

            #TODO: Mandar email al usuario con su contraseña
            #se tiene listo el template para notificacion de creacion de usuario
            #codigo completo en notificaciones/test_notificacion
            #Params 
            #        @preheader type:string #breve descripcion del contenido de la notificacion
            #        @fecha type:date #fecha que aparecera en la notificacion
            #        @nombre type:string #nombre completo
            #        @username type:string #nombre del usuario
            #        @password type:string #contraseña del usuario sin encriptar
            #        @site type:string #ruta url del dominio para que muestre las fotos 
            
            send_mail(u'Contraseña sistema Vitesse', 
                      u'Usuario: %s \n Contraseña: %s'%(usuario.username, password),
                       'no-reply@logisticavitesse.com.mx',
                      [usuario.email], fail_silently=False)
            messages.success(request, 'El usuario %s, ha sido agregado.'%perfil.user.get_short_name())
            return redirect('cuentas.views.usuarios')
        
    context = RequestContext(request,{ 
        'form': form,
        'form2': form2,
        'action': 'Agregar',
    })
    return render_to_response('agregar_usuario.html', context)

@login_required
def editar_usuario(request, id_usuario):
    user = request.user
    #print 'ok=', user.has_perm('beneficiarios.add_benefi') 
    profile = user.get_profile()
    perfil = get_object_or_404(Perfil, pk=id_usuario)

    print 'usrid=' , perfil.cliente



    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=perfil.user)
        form2 = PerfilModelForm(request.POST, instance=perfil)
        listaValores = request.POST.getlist('user_permissions')
        #listaValores = Permission.objects.all()
        #todosPermisos = Permission.objects.all()
        #user.user_permissions.clear()
        #for i in todosPermisos:           
        #    if str(i.id) in listaValores:
        #        print str(i.id)
        #        user.user_permissions.add(i)
        user.user_permissions.add()
        
        if form.is_valid() and form2.is_valid():
            usuario = form.save()            
            perfil = form2.save()
            messages.success(request, 'El usuario %s, ha sido modificado.'%perfil.user.get_short_name())
            return redirect('cuentas.views.usuarios')
    else:
        form = UsuarioForm(instance=perfil.user)
        form2 = PerfilModelForm(instance=perfil)
        
    context = RequestContext(request,{ 
        'form': form,
        'form2': form2,
        'action': 'Editar',
    })
    return render_to_response('agregar_usuario.html', context)

@login_required
def perfil(request):
    user = request.user
    perfil = user.get_profile()

    
    if request.method == "POST":
        form = UsuarioPerfilForm(request.POST, instance=perfil.user)
        form2 = PerfilModelForm(request.POST, instance=perfil)
        if form.is_valid() and form2.is_valid():
            usuario = form.save()            
            perfil = form2.save()
            messages.success(request, 'El usuario %s, ha sido modificado.'%perfil.nombre_corto())
            return redirect('cuentas.views.perfil')
    else:
        form = UsuarioPerfilForm(instance=perfil.user)
        form2 = PerfilModelForm(instance=perfil)
        
    context = RequestContext(request,{ 
        'form': form,
        'form2': form2,
        'perfil': perfil,
    })
    return render_to_response('mi_perfil.html', context)


#agregado jc
@login_required
def usuariosprivilegios(request):
    user = request.user
    profile = user.get_profile()
    formPriv = PerfilModelFormUpdate()

    
    if request.method == "POST":
        llaveCtaPerf = request.POST.get('llave')
        #catModEco_A = request.POST.get('catModEco_A')
        #catModEco_B = request.POST.get('catModEco_B')
        #catModEco_M = request.POST.get('catModEco_M')
        context = RequestContext(request,{ 
            #'form': form,
            'formPriv': formPriv,
            'action': 'Asignar Privilegios',
        })
        
        if llaveCtaPerf is None or llaveCtaPerf =='':
            messages.error(request, u'Seleccione el Usuario al que desea asignar permisos ')
            return render_to_response('agregar_usuarioPermisos.html', context)
        else:

            if request.POST.get('catModEco_A') is None:
                catModEco_A = 0
            else:
                catModEco_A = 1


            if request.POST.get('catModEco_B') is None:
                catModEco_B = 0
            else:
                catModEco_B = 1


            if request.POST.get('catModEco_M') is None:
                catModEco_M = 0
            else:
                catModEco_M = 1


        qs = Perfil.objects.get(user_id=llaveCtaPerf)
        #print qs.query

        #for pet in qs:
        #print qs.id
        
        qs2 = Perfil.objects.filter(id=qs.id).update(catModEco_A=catModEco_A,
            catModEco_B=catModEco_B,catModEco_M=catModEco_M)
        #print 'ok'


        #form = UsuarioForm(request.POST)
        formPriv = PerfilModelFormUpdate(request.POST)
        messages.success(request, u'Los permisos se asignaron correctamente')
        return render_to_response('agregar_usuarioPermisos.html', context)
        #if form.is_valid() and form2.is_valid():
        if formPriv.is_valid():  
            

            #usuario = form.save(commit=False)
            #password = User.objects.make_random_password(8)
            #usuario.set_password(password)
            #usuario.save()
            #form.save_m2m()
            ##########################
            #perfil = formPriv.save(commit=False)
            #perfil.user = usuario
            #perfil.save()
            #formPriv.save_m2m()
            

            #TODO: Mandar email al usuario con su contraseña
            #se tiene listo el template para notificacion de creacion de usuario
            #codigo completo en notificaciones/test_notificacion
            #Params 
            #        @preheader type:string #breve descripcion del contenido de la notificacion
            #        @fecha type:date #fecha que aparecera en la notificacion
            #        @nombre type:string #nombre completo
            #        @username type:string #nombre del usuario
            #        @password type:string #cotraseña del usuario sin encriptar
            #        @site type:string #ruta url del dominio para que muestre las fotos 
            
            #send_mail(u'Contraseña sistema Vitesse', 
            #          u'Usuario: %s \n Contraseña: %s'%(usuario.username, password),
            #           'no-reply@logisticavitesse.com.mx',
            #          [usuario.email], fail_silently=False)
            messages.success(request, 'El usuario %s, ha sido agregado.'%perfil.user.get_short_name())
            return redirect('cuentas.views.usuarios')
        
    context = RequestContext(request,{ 
        #'form': form,
        'formPriv': formPriv,
        'action': 'Asignar Privilegios',
    })
    return render_to_response('agregar_usuarioPermisos.html', context)   


#AJAX
@csrf_exempt
def resultsPerfil(request):
    llaveCtaPerf = request.POST.get('pk')
    #qs = Perfil.objects.get(user_id=llaveCtaPerf)
    #print qs.query

    
    #print llaveCtaPerf
    return render_to_response('results.html', llaveCtaPerf)

