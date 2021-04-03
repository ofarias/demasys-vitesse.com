# coding: utf-8
from django import template
from django.template.defaultfilters import stringfilter
from sepomex.models import Sepomex

register = template.Library()

@register.filter
@stringfilter
def municipio(value):
    return_value = ''
    if value != '':
        edo, asenta = value.split('-')
        m = Sepomex.objects.filter(id_asenta_cpcons=asenta, clave_estado=edo).values('municipio').distinct()[0]
        """Removes all values of arg from the given string"""
        return_value = m['municipio']
    return return_value

@register.filter
@stringfilter
def estado(value):
    return_value = ''
    if value != '':
        edo, asenta = value.split('-')
        m = Sepomex.objects.filter(id_asenta_cpcons=asenta, clave_estado=edo).values('estado').distinct()[0]
        """Removes all values of arg from the given string"""
        return_value = m['estado']
    return return_value