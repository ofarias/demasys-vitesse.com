# coding: utf-8
from django.db import models
from django.contrib.auth.models import User,Group,Permission
from clientes.models import Cliente


class Perfil(models.Model):
    user = models.OneToOneField(User)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    apellido_materno = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=50, blank=True, null=True)
    
    
    def __unicode__(self):
        return self.user.get_full_name()
 