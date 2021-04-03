# coding: utf-8
from django.contrib import admin
from models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nombre_corto', 'facturacion_colonia', 'activo')
    search_fields = ['nombre', 'nombre_corto']
    
admin.site.register(Cliente, ClienteAdmin)