# coding: utf-8
from django.db import models
from audit_log.models.managers import AuditLog

STATE_CHOICES = (
    ('AGU', 'Aguascalientes'),
    ('BCN', 'Baja California'),
    ('BCS', 'Baja California Sur'),
    ('CAM', 'Campeche'),
    ('CHH', 'Chihuahua'),
    ('CHP', 'Chiapas'),
    ('COA', 'Coahuila'),
    ('COL', 'Colima'),
    ('DIF', 'Distrito Federal'),
    ('DUR', 'Durango'),
    ('GRO', 'Guerrero'),
    ('GUA', 'Guanajuato'),
    ('HID', 'Hidalgo'),
    ('JAL', 'Jalisco'),
    ('MEX', 'Estado de México'),
    ('MIC', 'Michoacán'),
    ('MOR', 'Morelos'),
    ('NAY', 'Nayarit'),
    ('NLE', 'Nuevo León'),
    ('OAX', 'Oaxaca'),
    ('PUE', 'Puebla'),
    ('QUE', 'Querétaro'),
    ('ROO', 'Quintana Roo'),
    ('SIN', 'Sinaloa'),
    ('SLP', 'San Luis Potosí'),
    ('SON', 'Sonora'),
    ('TAB', 'Tabasco'),
    ('TAM', 'Tamaulipas'),
    ('TLA', 'Tlaxcala'),
    ('VER', 'Veracruz'),
    ('YUC', 'Yucatán'),
    ('ZAC', 'Zacatecas'),
)


class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=100)
    nombre_corto = models.CharField(max_length=10)
    rfc = models.CharField(max_length=13, blank=True, null=True)
    facturacion_clave_municipio = models.CharField(max_length = 100)
    facturacion_colonia = models.CharField('Colonia', max_length=150)
    facturacion_calle = models.CharField('Calle', max_length=150)
    facturacion_numero = models.CharField(u'Número', max_length=100)
    facturacion_cp = models.CharField(max_length=5, blank=True, null=True)
    recoleccion_clave_municipio = models.CharField(max_length = 100)
    recoleccion_colonia = models.CharField('Colonia', max_length=150)
    recoleccion_calle = models.CharField('Calle', max_length=150)
    recoleccion_numero = models.CharField(u'Número', max_length=100)
    recoleccion_cp = models.CharField(max_length=5, blank=True, null=True)
    activo = models.BooleanField(default=True)
    correo = models.CharField(max_length=255, db_column='correo', null = True)
    contacto = models.CharField(max_length = 100, null = True)
    telefono = models.CharField(max_length = 100, null = True)
    datos_bancarios = models.CharField(max_length = 100, null = True)
    ##claveSAE = models.CharField(max_length=20, null = True)


    audit_log = AuditLog()
    
    def __unicode__(self):
        return self.nombre_corto
    
    class Meta:
        ordering = ["nombre_corto"]   
    
class Departamento(models.Model):
    departamento = models.CharField(max_length=200)
    cliente = models.ForeignKey(Cliente)
    activo = models.BooleanField(default=True)
    #claveSAE = models.CharField(max_length= 20, null = True, blank = True, default = '') 
    
    audit_log = AuditLog()
    
    def __unicode__(self):
        return self.departamento
    
    class Meta:
        ordering = ["departamento"]  
