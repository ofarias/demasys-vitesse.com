# coding: utf-8

from django.contrib import admin
from models import *


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'email', 'telefono', 'cliente')
    
    def email(self, obj):
        return obj.user.email
    
admin.site.register(Perfil, PerfilAdmin)