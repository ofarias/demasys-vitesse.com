#coding: utf-8
from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    (r'^grappelli/', include('grappelli.urls')),    
    (r'^catalogos/', include('catalogos.urls')),
    (r'^clientes/', include('clientes.urls')),
    (r'^workflow/', include('workflow.urls')),
    (r'^cuentas/', include('cuentas.urls')),
    (r'^viajes/', include('viajes.urls')),
    (r'^sepomex/', include('sepomex.urls')),
    (r'^dashboard/', include('dashboards.urls')),
    (r'^$', 'dashboards.views.index'), 
    (r'^solicitudes/', include ('solicitudes.urls')),
    (r'^beneficiarios/', include ('beneficiarios.urls')),
    (r'^contable/', include ('contable.urls')),
    (r'^inventario/', include ('inventario.urls')),
    (r'^empleados/',include ('empleados.urls')),
    (r'^externo/',include ('externo.urls')),
    (r'^reporte/',include ('reporte.urls')),
)

if settings.LOCAL:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
           {'document_root': settings.MEDIA_ROOT}),
    )
