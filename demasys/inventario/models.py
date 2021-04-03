from django.db import models
from datetime import datetime
from catalogos.models import Economico
from django.utils.timezone import utc

# Create your models here.
class Productos(models.Model):
    descripcion = models.CharField(max_length=200)
    existencia = models.DecimalField(max_digits = 6, decimal_places = 2)
    costoUnitario = models.DecimalField(max_digits = 8, decimal_places = 2)

    def __unicode__(self):
		return self.descripcion


class Movimientos(models.Model):
    fecha = models.DateField(default=datetime.now())
    costo = models.DecimalField(max_digits = 8, decimal_places = 2)
    factor = models.DecimalField(max_digits = 5, decimal_places = 2)
    unidades = models.DecimalField(max_digits = 6, decimal_places = 2)
    movimiento = models.CharField(max_length = 1)
    idProducto = models.ForeignKey(Productos, db_column='idProducto')
    idSolicitud = models.IntegerField()
   #idEconomico = models.IntegerField()
    idEconomico = models.ForeignKey(Economico, db_column = 'idEconomico', null = True)
   # creado = models.DateTimeField(auto_now_add=True)

class ExcelUpload(models.Model):
    docfile = models.FileField(upload_to='upload')
