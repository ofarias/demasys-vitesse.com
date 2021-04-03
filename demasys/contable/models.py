from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from cuentas.models import Perfil

# Create your models here.

class Partidas(models.Model):
    descripcion = models.CharField(max_length = 100)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.pk

    def __unicode__(self):
        return u'%s' % (self.descripcion)

    class Meta:
        ordering = ["id"]

class Area(models.Model):
    descripcion = models.CharField(max_length = 100)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.pk

    def __unicode__(self):
        return u'%s' % (self.descripcion)

    class Meta:
        ordering = ["id"]

class Movimientos(models.Model):
    id_auth_user = models.ForeignKey(User, db_column='id_auth_user')
    idPartida = models.ForeignKey(Partidas, db_column='idPartida')
    idArea = models.ForeignKey(Area, db_column='idArea')
    fecha = models.DateTimeField(default=datetime.now)
    importe =  models.DecimalField(max_digits = 12, decimal_places = 2)
    tipo = models.CharField(max_length = 1)
    concepto = models.CharField(max_length=160)
    comentarios = models.CharField(max_length=160)
    ref_viaje = models.IntegerField()
    ref_solicitud = models.IntegerField()
    montoPartida =  models.DecimalField(max_digits = 12, decimal_places = 2)
    maniobras_locales = models.DecimalField(max_digits = 12, decimal_places = 2)
    maniobras_foraneas = models.DecimalField(max_digits = 12, decimal_places = 2)
    maniobras_retrabajos = models.DecimalField(max_digits = 12, decimal_places = 2)
    casetas_lg = models.DecimalField(max_digits = 12, decimal_places = 2)
    cliente_paga = models.DecimalField(max_digits = 12, decimal_places = 2)
   

    def __unicode__(self):
        return u'%s %s %s %s' % (self.idPartida, self.fecha, self.importe, self.tipo)


    class Meta:
        ordering = ["fecha"]
