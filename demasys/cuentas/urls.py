# coding: utf-8
from django.conf.urls import patterns,url
from django.contrib.auth.views import login, logout_then_login, password_change,\
    password_change_done

urlpatterns = patterns('cuentas.views',
    (r'^login/$',  login, {'template_name': 'login_form.html'}),
    (r'^logout/$', logout_then_login),
    (r'^password_change/$', password_change, {'template_name': 'password_change.html','post_change_redirect':'/'}),
    (r'^password_change_done/$', password_change_done),
    (r'^usuarios/$', 'usuarios'),
    (r'^usuarios/add/$', 'agregar_usuario'),
    (r'^usuarios/privilegios/$', 'usuariosprivilegios'),
    (r'^usuarios/privilegios/$', 'resultsPerfil'),
    (r'^usuarios/editar/(?P<id_usuario>\d+)/$', 'editar_usuario'),
    (r'^perfil/$', 'perfil'),


)