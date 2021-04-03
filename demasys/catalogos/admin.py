# coding: utf-8
from django.contrib import admin
from models import ModeloEconomico, Economico, Operador

class ModeloEconomicoAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'capacidad',)
    search_fields = ['modelo',]
    list_filter = ('capacidad',)
    
admin.site.register(ModeloEconomico, ModeloEconomicoAdmin)

class EconomicoAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'color', 'placas', 'activo',)
    search_fields = ['placas',]
    list_filter = ('modelo', 'activo',)
    
admin.site.register(Economico, EconomicoAdmin)

class OperadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido_paterno', 'apellido_materno', 'telefono', 'activo',)
    search_fields = ['nombre', 'apellido_paterno', 'apellido_materno',]    
    
admin.site.register(Operador, OperadorAdmin)


