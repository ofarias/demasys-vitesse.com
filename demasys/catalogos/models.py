# coding: utf-8
from django.db import models
from audit_log.models.managers import AuditLog
import os
from django.conf import settings
from empleados.models import empleado

COLORES_CHOICES = (
    ('Blanco', 'Blanco',),
    ('Rojo', 'Rojo',),
    ('Verde', 'Verde',),
    ('Amarillo', 'Amarillo',),
    ('Gris', 'Gris',),
    ('Azul', 'Azul',),
    ('Arena','Arena',),
    ('Marron','Marron'),
    (u'Blanco Cristal',u'Blanco Cristal'),
    (u'Rojo Veloste',u'Rojo Veloste'),
    ('Beige','Beige'),
)

PASA_CASETA = (
    (1, 'AUTO'),
    (2, u'CAMIONETA SENCILLA'),
    (3, u'CAMIONETA DOBLE RODADA'),
)

### Comienzan los cambios para el control vehicular

MARCAS = (
    ('DODGE', 'DODGE'),
    ('VOLKSWAGEN', 'VOLKSWAGEN'),
    ('FORD', 'FORD'),
    (u'MERCEDEZ BENZ', u'MERCEDEZ BENZ'),
    ('TOYOTA', 'TOYOTA'),
    ('FREIGHTLINER', 'FREIGHTLINER'),
    ('PEUGEOT', 'PEUGEOT'),
    ('OTRO', 'OTRO'),
)

SUBMARCAS = (
    ('H100', 'H100'),
    ('CRAFFTER', 'CRAFFTER'),
    ('EUROVAN', 'EUROVAN'),
    (u'450 CHASIS CAB.', u'450 CHASIS CAB.'),
    (u'350 CHASIS CAB.', u'350 CHASIS CAB.'),
    ('SPRINTER ', 'SPRINTER '),
    ('IACE', 'IACE'),
    (u'RAM 4000 CHASIS PL', u'RAM 4000 CHASIS PL'),
    (u'BUSINESS CLASS M2', u'BUSINESS CLASS M2'),
    (u'FORD TRANSIT', u'FORD TRANSIT'),
    (u'CRAFFTER CHASIS CABINA', u'CRAFFTER CHASIS CABINA'),
    (u'PARTNER MAXI', u'PARTNER MAXI'),
    (u'RAM PROMASTER PANEL', u'RAM PROMASTER PANEL'),
    (u'ATTITUDE GL 4P', u'ATTITUDE GL 4P'),
    (u'ATOS STD', u'ATOS STD'),
    ('AVANZA', 'AVANZA'),
    (u'ATTITUDE 4PTA (IMP)', u'ATTITUDE 4PTA (IMP)'),
    (u'AVANZA PREMIUM STD',u'AVANZA PREMIUM STD'),
    (u'SONATA',u'SONATA'),
    (u'ATOS',u'ATOS'),
    (u'ATTITUDE MANUAL GL', u'ATTITUDE MANUAL GL'),
    (u'JOURNEY',u'JOURNEY'),
)

TIPO_PLACAS = (
    ('ESTATAL', 'ESTATAL'),
    ('FEDERAL', 'FEDERAL'),
)

TIPO_CAJA = (
    (u'S/C', u'S/C'),
    ('Teckmovil', 'Teckmovil'),
    ('Chicano', 'Chicano'),
    ('Morgan','Morgan'),
)

MEDIDAS = (
    (u'195 / 75 R 16', u'195 / 75 R 16'),
    (u'225 / 70 R 19.5', u'225 / 70 R 19.5'),
    (u'245/ 75 R 17', u'245/ 75 R 17'),
    (u'235 / 80 R 17', u'235 / 80 R 17'),
    (u'295 / 75 R 22.5', u'295 / 75 R 22.5'),
    (u'195 / 75 R 16 - 205 / 75 R 16', u'195 / 75 R 16 - 205 / 75 R 16'),
    (u'205 / 75 R16 - 285 / 65 R 16', u'205 / 75 R16 - 285 / 65 R 16'),
    (u'195 / 70 R15', u'195 / 70 R15'),
    (u'205 / 50 R16', u'205 / 50 R16'),
    (u'175 / 70 R13', u'175 / 70 R13'),
    (u'185 / 70 R14', u'185 / 70 R14'),
    (u'225 / 75 R16', u'225 / 75 R16'),
    (u'215 / 70 R16','215 / 70 R16'),
    (u'215 / 70 R15',u'215 / 70 R15'),
    (u'205 / 75 R16', u'205 / 75 R16'),
    (u'185 / 65 R14',u'185 /65 / R14'),
)

TIPO_LLANTAS = (
    ('SENCILLA', 'SENCILLA'),
    ('DOBLE', 'DOBLE'),
    ('TRASERAS','TRASERAS'),
)

CARGAS = (
    ('750 KG', '750 KG'),
    ('1000 KG', '1000 KG'),
    ('1500 KG', '1500 KG'),
    ('1800 KG', '1800 KG'),
    ('3500 KG', '3500 KG'),
    ('4000 KG', '4000 KG'),
    ('4500 KG', '4500 KG'),
    ('12000 KG', '12000 KG'),
    ('0 KG','0 KG'),
)

COMBUSTIBLE = (
    (1,'Gasolina'),
    (2,'Diesel'),
    (3,'Gas'),
)

CILINDROS = (
    (1,'4'),
    (2,'5'),
    (3,'6'),
    (4,'8'),
)

STATUS = (
     (1, 'Activo'),
     (2, 'Mantenimiento'),
     (3, u'Taller (Mecanica)'),
     (4, u'Taller (Hojalateria / Pintura)'),
     (5, u'Corralon'),
     (6, 'Descompuesto'),
     (7, 'Siniestro (Aseguradora)'),
     (8, 'Otro'),
     (9, 'Viaje'),
     (10, 'Disponible'),
)

VIAJES = (
    (1, u'En Viaje'),
    (2, 'Disponible'),
    )

class ModeloEconomico(models.Model):
    modelo = models.CharField('Modelo', max_length=100)    
    capacidad = models.IntegerField('Capacidad', help_text='Capacidad en tarimas')
    capacidad_kilos = models.IntegerField(null = True)
    capacidad_volumen = models.DecimalField (max_digits = 7, decimal_places = 2, null = True)
    largo = models.DecimalField (max_digits = 7, decimal_places = 2, null = True)
    ancho = models.DecimalField (max_digits = 7, decimal_places = 2, null = True)
    alto = models.DecimalField (max_digits = 7, decimal_places = 2, null = True)
    
    audit_log = AuditLog()
    
    def __unicode__(self):
        return u'%s - %s tarimas' % (self.modelo, self.capacidad)
    
    class Meta:
        ordering = ["modelo"]

class Aseguradoras(models.Model):
    
    nombre = models.CharField (max_length = 100)
    direccion = models.CharField (max_length = 50)
    telefono_siniestros = models.CharField(max_length = 50)
    
    def __unicode__ (self):
        return self.nombre

    class Meta:
        ordering = ["nombre"]   


class Operador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=40)
    apellido_materno = models.CharField(max_length=40, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    activo = models.BooleanField(default=True)
    saldo = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    saldo_observaciones = models.TextField(blank=True, null=True)
    
    audit_log = AuditLog()
    
    def __unicode__(self):
        return u'%s %s %s' % (self.nombre, self.apellido_paterno, self.apellido_materno)
    
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Operadores"
        
    
class Economico(models.Model):
    id = models.AutoField(primary_key = True)
    color = models.CharField(max_length=100, choices=COLORES_CHOICES) # ok
    modelo = models.ForeignKey(ModeloEconomico) # ok
    placas = models.CharField(max_length=10) # ok
    activo = models.BooleanField(default=True)
    pasa_como = models.IntegerField(choices=PASA_CASETA, default=1)
    saldo = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    saldo_observaciones = models.TextField(blank=True, null=True)
    marca = models.CharField(max_length = 50, choices = MARCAS)
    submarca = models.CharField(max_length = 30, choices = SUBMARCAS)
    tipoPlaca = models.CharField(max_length = 10, choices = TIPO_PLACAS )
    caja = models.CharField(max_length = 10, choices = TIPO_CAJA)
    medidallantas = models.CharField(max_length = 50, choices = MEDIDAS)
    tipollantas = models.CharField(max_length = 20, choices = TIPO_LLANTAS)
    carga = models.CharField(max_length = 10, choices = CARGAS)
    aseguradora = models.ForeignKey(Aseguradoras)
    poliza = models.CharField (max_length = 30, null = True)
    fecha_vencimiento = models.DateField()
    iave = models.CharField (max_length = 30, null = True)
    cerradura = models.NullBooleanField(null = True)
    operador = models.ForeignKey (Operador, null = True)
    cctv = models.NullBooleanField(null = True)
    ultimoKilometraje = models.IntegerField(null = True)
    kilometrajeServicio = models.IntegerField(null = True)
    combustible = models.IntegerField(max_length= 20, choices = COMBUSTIBLE)
    cilindros = models.IntegerField (max_length = 2, choices = CILINDROS)
    psi = models.DecimalField (max_digits= 3, decimal_places = 0)
    filtro = models.CharField (max_length = 20)
    tipo_aceite = models.CharField (max_length = 20)
    litros = models.DecimalField(max_digits= 2, decimal_places = 0)
    rendimiento = models.DecimalField(max_digits = 6, decimal_places = 2)
    antijamer = models.NullBooleanField(null = True)
    fecha_antijamer = models.DateField (null = True)
    boton_panico = models.NullBooleanField (null = True )
    camara_int = models.NullBooleanField (null = True)
    camara_ext = models.NullBooleanField (null = True)
    lugar_camara_int = models.CharField(max_length = 30, null = True)
    lugar_camara_ext = models.CharField(max_length = 30, null = True)
    clave = models.CharField(max_length = 4, null = True)
    ns = models.CharField (max_length = 20, null = True)
    anio = models.CharField (max_length = 4, null = True)
    status = models.IntegerField (choices = STATUS, null = False)
    filtro_aire = models.CharField(max_length = 20, null = True)
    filtro_aceite = models.CharField(max_length = 20, null = True)
    filtro_gas = models.CharField(max_length = 20, null = True)
    filtro_airea = models.CharField(max_length = 20, null = True)
    enviaje = models.IntegerField(choices = VIAJES, null = True, default = 2)
 

    
    #imagen = models.FileField(upload_to='upload')


    #audit_log = AuditLog()
    
    def __unicode__(self):
        return u'ECO. %d %s, PLACAS: %s' % (self.pk, self.modelo, self.placas)
    
    class Meta:
        ordering = ["pk"]
        verbose_name_plural = "Economicos"
    
        
class Caseta(models.Model):
    via = models.CharField(max_length=255)
    #longitud = models.FloatField()
    #motos = models.FloatField()
    autos = models.FloatField()
    autobus_2_ejes = models.FloatField()
    #autobus_3_ejes = models.FloatField()
    #autobus_4_ejes = models.FloatField()
    #camion_2_ejes = models.FloatField()
    #camion_3_ejes = models.FloatField()
    #camion_4_ejes = models.FloatField()
    #camion_5_ejes = models.FloatField()
    #camion_6_ejes = models.FloatField()
    #camion_7_ejes = models.FloatField()
    #camion_8_ejes = models.FloatField()
    #camion_9_ejes = models.FloatField()
    
    audit_log = AuditLog()
    
    def __unicode__(self):
        return self.via
    
    class Meta:
        ordering = ["via"]
        verbose_name_plural = "Casetas"   
        
     
class GastoViaje(models.Model):
    nombre = models.CharField(max_length=100)
    audit_log = AuditLog()
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Gastos"
        
class ConceptoFacturacion(models.Model):
    nombre = models.CharField(max_length=100)
    audit_log = AuditLog()
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ["nombre"]
        verbose_name_plural = "Conceptos de Facturacion"

class ExcelEconomico(models.Model):
    docfile = models.FileField(upload_to='upload')

#Modificaciones carga excel
class ExcelViaje(models.Model):
    docfile = models.ImageField(upload_to='upload')

###############################################################
def get_file_path(instance, filename):
    print "instancia=",instance 
    ext = filename.split('.')[-1] 
    filename = "%s.%s" % (instance.nombre, ext) 
    return os.path.join('imgEconomicos', filename)
class Imagen(models.Model):
    imagen1 = models.ImageField(upload_to='imgEconomicos',  blank=True, null=True)
    imagen2 = models.ImageField(upload_to='imgEconomicos', blank=True, null=True)
    imagen3 = models.ImageField(upload_to='imgEconomicos', blank=True, null=True)
    imagen4 = models.ImageField(upload_to='imgEconomicos', blank=True, null=True)


class movimientosUnidad(models.Model):

    unidad = models.ForeignKey(Economico, null = False)
    fecha = models.DateField (null = False)
    tipo = models.IntegerField(choices = STATUS, null = False)
    obs = models.CharField(max_length = 400, null = False)
    operador = models.ForeignKey(empleado, null = True)
    kmen = models.IntegerField (null = True)
    kmsa = models.IntegerField (null = True)
    tiemporep=models.DateField(null=True)
    alternativa=models.CharField(max_length=250, null=True)


def get_file_path(instance, filename):
    filename = "%s_%s" % (instance.idEconomico.pk, filename)
    return os.path.join('documentosEconomico', filename)

class Documentos(models.Model):
    nombreDoc = models.CharField (max_length =100)
    descripcion = models.CharField (max_length = 100, null = True)

    def __unicode__(self):
        return self.nombreDoc

    class Meta:
        ordering = ["id"]

class Archivos(models.Model):
     idEconomico = models.ForeignKey(Economico, db_column='idEconomico')
     idDoc = models.ForeignKey(Documentos, db_column='idDoc')
     nombreDoc = models.FileField(upload_to=get_file_path, max_length=100)

     def __unicode__(self):
        return self.pk
     class Meta:
        ordering = ["id"]


  
