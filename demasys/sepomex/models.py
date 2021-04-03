from django.db import models

class Sepomex(models.Model):
    " Modelo que contiene los datos de Sepomex"
    codigo = models.CharField(max_length = 5)
    asentamiento = models.CharField(max_length = 255)
    tipo_asentamiento = models.CharField(max_length = 150)
    municipio = models.CharField(max_length = 255)
    estado = models.CharField(max_length = 120)
    ciudad = models.CharField(max_length = 200)
    codigo_postal = models.CharField(max_length = 5)
    clave_estado = models.CharField(max_length = 100)
    clave_oficina = models.CharField(max_length = 100)
    clave_tipo_asenta = models.CharField(max_length = 100)
    clave_municipio = models.CharField(max_length = 100)
    id_asenta_cpcons = models.CharField(max_length = 100)
    d_zona = models.CharField(max_length = 100)
    c_cve_ciudad = models.CharField(max_length = 100)
    c_CP = models.CharField(max_length = 100)