from django.db import models
from audit_log.models.managers import AuditLog

from datetime import datetime
from django.contrib.auth.models import User
from cuentas.models import Perfil
from decimal import Decimal
import os

OPCION = (
    ('SI', 'SI'),
    ('NO', 'NO'),
)

OPCIONN = (
    (1, 'SI'),
    (2, 'NO'),
)

TIPO_LIC = (
    (1,u'Sin Licencia'),
    (2,u'Estatal'),
    (3,u'Federal'),
    (4,u'Particular'),
    (5,u'Chofer'),
)

SEXO = (
    (1,''),
    (2,'Masculino'),
    (3,'Femenino'),

)

NACIONALIDAD = (
    (1,''),
    (2,'Mexicana'),
    (3,'Extranjero'),
)

VIVECON = (
    (0,''),
    (1,u'Sus Padres'),
    (2,u'Su Familia'),
    (3,'Parientes'),
    (4,'Solo'),
)

DEPENDIENTES = (
    (0,''),
    (1,u'Hijos'),
    (2,u'Conyuge'),
    (3,'Padres'),
    (4,'Otros'),
)

CIVIL = (
    (1,''),
    (2,'Soltero(a)'),
    (3,'Casado(a)'),
    (4,'Divorciado(a)'),
    (5,u'Union Libre'),
    (6,u'Padre o Madre Soltera'),
)

CAT_ESCOLARIDAD = (
    (1,u'SIN ESCOLARIDAD'),
    (2,'Primaria'),
    (3,'Secundaria'),
    (4,u'Preparatoria / Bachillerato'),
    (5,u'Universidad (Trunca)'),
    (6,u'Licenciatura / Ingenieria'),
    (7,u'Maestria'),
    (8,'Otro'),
)

CAT_MEDIO = (
    (1,'Anuncio'),
    (2,'Cartel'),
    (3,'Otro'),
)


STATUS = (
    (1, 'Alta'),
    (2, 'Baja'),
    (3, 'Reingreso'),
    (4, 'Incapacidad'),
    (5, u'Ausentismo-Permiso'),
    (6, u'Ausentismo-NO AVISO'),
    (7, 'Renuncia'),
    (8, 'Despido'),
    (9, u'Pendiente'),
)

SALUD = (
    (1,'Bueno'),
    (2,'Regular'),
    (3,'Malo'),
)

CRONICO = (
    (1,'Si'),
    (0,'No'),

)

PARENTESCO = (
    (1,'Padre'),
    (2,'Madre'),
    (3,'Esposa'),
    (4,'Esposo'),
    (5,'Hija'),
    (6,'Hijo'),

)

VF = (
    (1,'Vive'),
    (2,'Finado'),

)


PUESTOS = (
    (1, 'Eventual'),
    (2, 'Contrato'),
    (3, 'Confianza'),
    (4, 'Otro'),
)
CATEGORIAS = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
    (5, 'Otra'),
    (6, 'Solicitud'),
)

PARENTESCOS = (
    (1,u'Padre'),
    (2,u'Madre'),
    (3,u'Esposa(o)'),
    (4,u'Hermano (a)'),
    (5,'Pareja'),
    (6,u'Hijo (a)'),
    (7,'Conocido'),
    (8,u'Otro Familiar'),
    (9,u'Desde Solicitud'),
)

HIJOS = (
    (1, '0'),
    (2, '1'),
    (3, '2'),
    (4, '3'),
    (5, '4'),
    (6, '5'),
    (7, '6'),
    (8, '7'),
    (9, '8'),
    (10, '9'),
    (11, '10'),
)


T_MOVIMIENTO = (
    (1, 'Alta'),
    (2, 'Baja'),
    (3, 'Reingreso'),
    (4, 'Incapacidad'),
    (5, u'Ausentismo-Permiso'),
    (6, u'Ausentismo-NO AVISO'),
    (7, 'Renuncia'),
    (8, 'Despido'),
)

ESTATUS = (
    (1, 'Pendiente'),
    (2, 'Reprobado'),
    (3, 'Rechazado'),
    (4, 'Contratado'),
)

VIAJES = (
    (1, u'En Viaje'),
    (2, u'Disponible'),
)

class Puestos(models.Model):
     nombre = models.CharField(max_length = 50, null = False )
     descripcion = models.CharField(max_length = 200, null = True)
     tipo = models.IntegerField(choices = PUESTOS, null = True)
     sueldo = models.DecimalField(max_digits = 9, decimal_places = 2, null = True)

     def __unicode__(self):
         return str (self.nombre)

     class Meta:
         ordering = ["pk"]

class empleado(models.Model):

    nombre = models.CharField (max_length = 50, null = False)
    segundo_nombre = models.CharField (max_length = 50, null = True)
    apellidop = models.CharField (max_length = 50, null = False)
    apellidom = models.CharField (max_length = 50, null = False)
    sexo = models.IntegerField(choices = SEXO, default = 1, null = False)
    edad = models.DecimalField (max_digits = 2, decimal_places = 0, null = False)
    nacion = models.IntegerField (choices = NACIONALIDAD, default = 1, null = False)
    estadocivil = models.IntegerField (choices = CIVIL, default = 1, null = False)
    fecha_civil = models.DateField(null = True)
    hijos = models.IntegerField (choices = HIJOS,null = True)
    lugar_nacimiento= models.CharField (max_length = 100, null = False)
    contacto_emergencia_nom = models.CharField (max_length = 100, null = False)
    contacto_emergencia_tel = models.CharField (max_length = 100, null = False)
    contacto_emergencia_cel = models.CharField (max_length = 100, null = False)
    nss = models.CharField(max_length = 12, null = True)
    ife = models.DecimalField(max_digits = 20, decimal_places = 0, null = True)
    licencia = models.CharField (max_length = 22, null = False)
    tipo_lic =  models.IntegerField (choices = TIPO_LIC, default = 1, null = False)
    RFC = models.CharField (max_length = 15, null = True)
    CURP = models.CharField (max_length = 18, null = True)
    No_ActaNac= models.CharField(max_length = 30, null = True)
    escolaridad = models.IntegerField (choices = CAT_ESCOLARIDAD,null = False)
    Cartilla = models.CharField(max_length = 20, null = False)
    primaria = models.CharField (max_length = 100, null = True)
    cer_primaria = models.CharField (max_length = 30, null = True)
    secundaria = models.CharField (max_length = 100, null = True)
    cer_secundaria = models.CharField (max_length = 30, null = True)
    preparatoria = models.CharField (max_length = 100, null = True)
    cer_preparatoria = models.CharField (max_length = 30, null = True)
    universidad = models.CharField (max_length = 100, null = True)
    cer_universidad = models.CharField (max_length = 30, null = True)
    curso1 = models.CharField (max_length = 100, null = True)
    nombre_curso1 = models.CharField (max_length = 30, null = True)
    curso2 = models.CharField (max_length = 100, null = True)
    nombre_curso2 = models.CharField (max_length = 30, null = True)
    curso3 = models.CharField (max_length = 100, null = True)
    nombre_curso3 = models.CharField (max_length = 30, null = True)
    status = models.IntegerField (choices = STATUS, null = False)
    registro = models.CharField (max_length = 20, null = True)
    vigencia = models.CharField (max_length = 20, null = True)
    ingreso = models.DateField(null = True)
    puesto = models.ForeignKey(Puestos, null = True)
    lic_vigencia = models.DateField(null = True)
    clave = models.CharField(max_length = 4, null = False)
    fecha_nac = models.DateField(null = False)
    categoria = models.IntegerField(choices = CATEGORIAS, null = False)
    lic_fecha_ref = models.DateField (null = False)
    parentesco = models.IntegerField (choices = PARENTESCOS, null = False)
    cer_opalo = models.BooleanField (default = 0, null = False)
    fecha_cer_opalo = models.DateField(null = True)
    folio_opalo = models.CharField (max_length = 30, null = True)
    cer_rc = models.BooleanField (default = 0, null = False) 
    fecha_cer_rc = models.DateField (null = True)
    folio_rc = models.CharField(max_length = 30, null = True)
    calle = models.CharField(max_length = 30, null = False)
    exterior = models.CharField(max_length = 10, null = False)
    interior = models.CharField(max_length = 10, null = False)
    colonia = models.CharField(max_length = 30, null = False)
    estado = models.CharField(max_length = 30, null = False)
    cp = models.CharField(max_length = 20, null = False)
    tel_casa = models.CharField(max_length = 14, null = True)
    tel_asig = models.CharField (max_length = 14, null = True)
    religion = models.CharField (max_length = 20, null = True)
    cuenta = models.CharField (max_length = 20, null = True)
    banco = models.CharField (max_length = 20, null = True)
    enviaje = models.IntegerField(choices=VIAJES, null = True, default=0)
    servicios = models.IntegerField(null = True, default=0)

    def __unicode__(self):
        ##return str (self.clave) ##(self.pk).zfill(4)
        return u'%s %s %s %s' % (self.nombre, self.segundo_nombre, self.apellidop, self.apellidom)


    class Meta:
        ordering = ["nombre"]

class Datos(models.Model):

    nombreCompleto = models.CharField (max_length =150)
    edad = models.IntegerField(blank=False, null = False)
    domicilio = models.CharField (max_length =100)
    colonia	= models.CharField (max_length =100)
    cp = models.IntegerField()
    telefono = models.CharField (max_length =15)
    celular	= models.CharField (max_length =15)
    lugarNacimiento = models.CharField (max_length =100)
    email = models.CharField (max_length =60)
    fechaNacimiento	= models.DateField()
    #nacionalidad = models.CharField (max_length =20) #combo
    nacionalidad = models.IntegerField (choices = NACIONALIDAD, default = 1, null = False)
    #viveCon	= models.CharField (max_length =30) #combo
    viveCon = models.IntegerField (choices = VIVECON, default = 0, null = False)
    #dependientes = models.CharField (max_length =30) #combo
    dependientes = models.IntegerField (choices = DEPENDIENTES, default = 0, null = False)
    #estatura = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    #peso = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    #sexo = models.CharField (max_length =10) #combo
    sexo = models.IntegerField(choices = SEXO, default = 1, null = False)
    #estadoCivil = models.CharField (max_length =10) #combo
    estadoCivil = models.IntegerField (choices = CIVIL, default = 1, null = False)

    casadoPor = models.CharField (max_length =20)
    fechaSol = models.DateField()
    puestoSol = models.CharField (max_length =30)
    sueldo = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]

class Documentacion(models.Model):
    idsolicitante = models.ForeignKey(Datos, db_column='idsolicitante')
    rfc = models.CharField (max_length =15)
    nss	= models.CharField (max_length =20)
    numCartilla = models.CharField (max_length =20)
    pasaporte = models.CharField (max_length =20)
    tieneLicencia = models.CharField (max_length =2, choices = OPCION)
    tipoLicencia = models.CharField (max_length =20)
    numLicencia = models.CharField (max_length =20)
    #vigLicencia = models.CharField (max_length =20) no esta agregado en el form aque se refiere
    curp = models.CharField (max_length =20)
    afore = models.CharField (max_length =20)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]


class Salhab(models.Model):
    idsolicitante = models.ForeignKey(Datos, db_column='idsolicitante')
    #salud = models.CharField (max_length =15)#combo
    salud = models.IntegerField(choices = SALUD, default = 1, null = False)
    cronico = models.IntegerField(choices = CRONICO, default = 1, null = False)
    #cronico = models.CharField(max_length = 2, choices = OPCION)
    descripcion = models.CharField (max_length =60)
    deporte	 = models.CharField(max_length = 2, choices = OPCION)
    club = models.CharField(max_length = 2, choices = OPCION)
    hobbie = models.CharField (max_length =60)
    meta = models.CharField (max_length =60)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]



class Conocimientos(models.Model):
    idsolicitante = models.ForeignKey(Datos, db_column='idsolicitante')
    idiomas	= models.CharField (max_length =100)
    equipo	= models.CharField (max_length =100)
    funciones	= models.CharField (max_length =100)
    otros	= models.CharField (max_length =100)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]



class Generales(models.Model):
    idsolicitante = models.ForeignKey(Datos, db_column='idsolicitante')
    #medio = models.CharField (max_length =60)
    medio = models.IntegerField(choices = CAT_MEDIO, default = 1, null = False)
    #afianzado = models.CharField (max_length =2)
    afianzado = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    ciaFianza = models.CharField (max_length =50)
    #seguro = models.CharField (max_length =2)
    seguro = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    ciaSeguro = models.CharField (max_length =50)

    #residencia = models.CharField (max_length =2)
    residencia = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    razonReside	 = models.CharField (max_length =50)

    #familiares = models.CharField (max_length =2)
    familiares = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    nombres = models.CharField (max_length =100)

    #sindicato = models.CharField (max_length =2)
    sindicato = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    nombreSin = models.CharField (max_length =60)

    #viajar = models.CharField (max_length =2)
    viajar = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    razonViaje = models.CharField (max_length =60)

    presentar = models.CharField (max_length =60)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]




class Economico(models.Model):
    idsolicitante = models.ForeignKey(Datos, db_column='idsolicitante')
    #ingreso = models.CharField (max_length =2)

    ingreso = models.IntegerField(choices = OPCIONN, default = 1, null = False)

    modo = models.CharField (max_length =20)
    importe = models.CharField (max_length =20)

    #casa = models.CharField (max_length =2)
    casa = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    importeCasa = models.CharField (max_length =15)

    #habitantes = models.IntegerField()
    #auto = models.CharField (max_length =2)
    auto = models.IntegerField(choices = OPCIONN, default = 1, null = False)

    placas = models.CharField (max_length =10)
    marca = models.CharField (max_length =20)
    modelo = models.CharField (max_length =20)


    ingresos = models.CharField (max_length =10)
    egresos = models.CharField (max_length =10)
    ahorros = models.CharField (max_length =10)
    total = models.CharField (max_length =10)

    #conyuge = models.CharField (max_length =2)
    conyuge = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    ingresoCony = models.CharField (max_length =10)
    renta = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    #renta = models.CharField (max_length =2)
    rentaMensual = models.CharField (max_length =10)

    #deudas = models.CharField (max_length =2)
    deudas = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    clase = models.CharField (max_length =10)
    impDeuda = models.CharField (max_length =10)
    abonoMensual = models.CharField (max_length =10)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]
# Create your models here.

# Create your models here.

def get_file_path(instance, filename):
    filename = "%s_%s" % (instance.idsolicitante, filename)
    return os.path.join('documentosEmp', filename)

class Documentos(models.Model):
    doc1 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc2 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc3 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc4 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc5 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc6 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc7 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc8 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc9 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc10 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc11 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc12 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc13 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc14 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc15 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc16 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc17 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc18 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc19 = models.FileField(upload_to=get_file_path,blank=True, null=True)
    doc20 = models.FileField(upload_to=get_file_path,blank=True, null=True)

class Catdoc(models.Model):
    nombreDoc = models.CharField (max_length =100)
    observacionesDoc = models.CharField (max_length = 200, null = True)


    def __unicode__(self):
        return self.nombreDoc

    class Meta:
        ordering = ["id"]

class Archivos(models.Model):
     idsolicitante = models.IntegerField()
     idDoc = models.ForeignKey(Catdoc)
     nombreDoc = models.FileField(upload_to=get_file_path, max_length=100)

     def __unicode__(self):
        return self.pk
     class Meta:
        ordering = ["id"]

def get_file_path(instance, filename):
    print "instancia=",instance
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.nombre, ext)
    return os.path.join('imgEmpleados', filename)

class Imagen(models.Model):
    imagen1 = models.ImageField(upload_to='imgEmpleados',  blank=True, null=True)
    imagen2 = models.ImageField(upload_to='imgEmpleados', blank=True, null=True)
    imagen3 = models.ImageField(upload_to='imgEmpleados', blank=True, null=True)
    imagen4 = models.ImageField(upload_to='imgEmpleados', blank=True, null=True)



class movimientos (models.Model):

   empleado = models.ForeignKey(empleado, null = False)
   tipo = models.IntegerField(choices = T_MOVIMIENTO, null = False)
   fecha = models.DateField (null = False)
   realiza = models.ForeignKey (Perfil, null = False)
   motivo = models.CharField (max_length = 400, null = False)

   def __unicode__(self):
       return self.pk 
   class Meta: 
       ordering = ["id"]



class Solicitud(models.Model):
    ##Datos Generales
    nombreCompleto = models.CharField (max_length =150)
    nombre = models.CharField(max_length=100)
    segundoNombre = models.CharField(max_length=100, null=True)
    paterno = models.CharField(max_length=100)
    materno = models.CharField(max_length=100)
    edad = models.IntegerField(blank=False, null = False)
    domicilio = models.CharField (max_length =100)
    colonia	= models.CharField (max_length =100)
    cp = models.IntegerField()
    telefono = models.CharField (max_length =15)
    celular	= models.CharField (max_length =15)
    lugarNacimiento = models.CharField (max_length =100)
    email = models.CharField (max_length =60)
    fechaNacimiento	= models.DateField()
    nacionalidad = models.IntegerField (choices = NACIONALIDAD, default = 1, null = False)
    viveCon = models.IntegerField (choices = VIVECON, default = 0, null = False)
    dependientes = models.IntegerField (choices = DEPENDIENTES, default = 0, null = False)
    sexo = models.IntegerField(choices = SEXO, default = 1, null = False)
    estadoCivil = models.IntegerField (choices = CIVIL, default = 1, null = False)
    fechaSol = models.DateField()
    puestoSol = models.CharField (max_length =30)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    #Seccion de Documentacion
    rfc = models.CharField (max_length =15)
    nss	= models.CharField (max_length =20)
    numCartilla = models.CharField (max_length =20)
    pasaporte = models.CharField (max_length =20)
    tieneLicencia = models.CharField (max_length =2, choices = OPCION)
    #tipoLicencia = models.CharField (max_length =20)
    numLicencia = models.CharField (max_length =20)
    curp = models.CharField (max_length =20)
    afore = models.CharField (max_length =20)

    #Salud y habitos
    salud = models.IntegerField(choices = SALUD, default = 1, null = False)
    cronico = models.IntegerField(choices = CRONICO, default = 1, null = False)
    descripcion = models.CharField (max_length =60)
    deporte	 = models.CharField(max_length = 2, choices = OPCION)
    club = models.CharField(max_length = 2, choices = OPCION)
    hobbie = models.CharField (max_length =160)
    meta = models.CharField(max_length =255)

    #Familiares
    #nombreFamiliar = models.CharField (max_length =255)
    #parentesco = models.IntegerField(choices = PARENTESCO, default = 1, null = False)
    #domicilioFam = models.CharField (max_length =255)
    #ocupacion = models.CharField (max_length =255)
    #edadFam = models.IntegerField()
    #viveFinado = models.IntegerField(choices = VF, default = 1, null = False)

    #Escolaridad
    #nombreEscuela = models.CharField (max_length =255)
    #domicilioEscuela = models.CharField (max_length =255)
    #inicial = models.CharField (max_length =25)
    #final = models.CharField (max_length =25)
    #anios = models.IntegerField()
    #titulo = models.CharField (max_length =25)
    #nivel = models.IntegerField(choices = CAT_ESCOLARIDAD, default = 1, null = False)

    #Conocimientos
    idiomas	= models.CharField (max_length =100)
    equipo	= models.CharField (max_length =200)
    funciones	= models.CharField (max_length =200)
    otros	= models.CharField (max_length =200)

    #Empleos
    #tiempo	= models.CharField (max_length =150)
    #nombreEmp = models.CharField (max_length =150)
    #domicilioEmp = models.CharField (max_length =200)
    #telefonoEmp = models.CharField (max_length =30)
    #puestoIni = models.CharField (max_length =30)
    #puestoFin = models.CharField (max_length =30)
    #sueldoIni = models.CharField (max_length =30)
    #sueldoFin = models.CharField (max_length =30)
    #motivo	= models.CharField (max_length =100)
    #jefe = models.CharField (max_length =80)
    #puestoJefe = models.CharField (max_length =20)
    #actividad = models.CharField (max_length =60)
    #permiso  = models.CharField (max_length =2)
    #noRazon = models.CharField(max_length = 2, choices = OPCION)

    #Referencias personales
    #nombreRef = models.CharField (max_length =100)
    #domicilioRef = models.CharField (max_length =100)
    #telefonoRef = models.CharField (max_length =30)
    #ocupacionRef = models.CharField (max_length =30)
    #tiempoRef = models.CharField (max_length =10)

    #Datos Generales
    medio = models.IntegerField(choices = CAT_MEDIO, default = 1, null = False)
    afianzado = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    ciaFianza = models.CharField (max_length =255)
    seguro = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    ciaSeguro = models.CharField (max_length =255)
    residencia = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    razonReside	 = models.CharField (max_length =255)
    familiaresT = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    nombres = models.CharField (max_length =255)
    sindicato = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    nombreSin = models.CharField (max_length =60)
    viajar = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    razonViaje = models.CharField (max_length =60)
    presentar = models.CharField (max_length =60)

    #Datos Economicos
    ingreso = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    modo = models.CharField (max_length =20)
    importe = models.CharField (max_length =20)
    casa = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    importeCasa = models.CharField (max_length =15)
    auto = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    placas = models.CharField (max_length =10)
    marca = models.CharField (max_length =20)
    modelo = models.CharField (max_length =20)
    ingresos = models.CharField (max_length =10)
    egresos = models.CharField (max_length =10)
    ahorros = models.CharField (max_length =10)
    total = models.CharField (max_length =10)
    conyuge = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    ingresoCony = models.CharField (max_length =10)
    renta = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    rentaMensual = models.CharField (max_length =10)
    deudas = models.IntegerField(choices = OPCIONN, default = 1, null = False)
    #clase = models.CharField (max_length =10)
    impDeuda = models.CharField (max_length =10)
    abonoMensual = models.CharField (max_length =10)
    #Estatus
    estatus = models.IntegerField(choices = ESTATUS, default = 1, null = True)


    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]


class Familiares(models.Model):
    idsolicitante = models.ForeignKey(Solicitud, db_column='idsolicitante')
    nombreFamiliar = models.CharField (max_length =255, blank=True)
    #parentesco = models.CharField (max_length =15)#combo
    parentesco = models.IntegerField(choices = PARENTESCO, default = 1, null = False)
    domicilioFam = models.CharField (max_length =255,blank=True)
    ocupacion = models.CharField (max_length =255,blank=True)
    edadFam = models.IntegerField(blank=True)
    #viveFinado = models.CharField (max_length =15)#combo
    viveFinado = models.IntegerField(choices = VF, default = 1, null = False, blank=True)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]


class Escolaridad(models.Model):
    idsolicitante = models.ForeignKey(Solicitud, db_column='idsolicitante')
    nombreEscuela = models.CharField (max_length =255, blank=True)
    domicilioEscuela = models.CharField (max_length =255, blank=True)
    inicial = models.CharField (max_length =25, blank=True)
    final = models.CharField (max_length =25, blank=True)
    anios = models.IntegerField(blank=True)
    titulo = models.CharField (max_length =255, blank=True)
    nivel = models.IntegerField(choices = CAT_ESCOLARIDAD, default = 1, null = False, blank=True)


    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]


class Empleos(models.Model):
    idsolicitante = models.ForeignKey(Solicitud, db_column='idsolicitante')
    tiempo	= models.CharField (max_length =150, blank=True)
    nombreEmp = models.CharField (max_length =255, blank=True)
    domicilioEmp = models.CharField (max_length =200, blank=True)
    telefonoEmp = models.CharField (max_length =30, blank=True)
    puestoIni = models.CharField (max_length =30, blank=True)
    puestoFin = models.CharField (max_length =30, blank=True)
    sueldoIni = models.CharField (max_length =30, blank=True)
    sueldoFin = models.CharField (max_length =30, blank=True)
    motivo	= models.CharField (max_length =255, blank=True)
    jefe = models.CharField (max_length =255, blank=True)
    #puestoJefe = models.CharField (max_length =20)
    actividad = models.CharField (max_length =60, blank=True)
    permiso  = models.CharField (max_length =2, choices = OPCION, blank=True)
    noRazon = models.CharField(max_length = 160, blank=True)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]

class Referencias(models.Model):
    idsolicitante = models.ForeignKey(Solicitud, db_column='idsolicitante')
    nombreRef = models.CharField (max_length =100, blank=True)
    domicilioRef = models.CharField (max_length =100, blank=True)
    telefonoRef = models.CharField (max_length =30, blank=True)
    ocupacionRef = models.CharField (max_length =30, blank=True)
    tiempoRef = models.CharField (max_length =10, blank=True)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]

class Cuestionario(models.Model):
    idsolicitante = models.ForeignKey(Solicitud, db_column='idsolicitante')
    bebida = models.CharField (max_length =255)
    freBebida = models.CharField (max_length =255)
    fuma = models.CharField (max_length =255)
    freFuma = models.CharField (max_length =255)
    drog = models.CharField (max_length =255)
    tiempoDrog = models.CharField (max_length =255)
    actividad = models.CharField (max_length =255)
    escolaridad = models.CharField (max_length =255)
    auto = models.CharField (max_length =255)
    oportunidad	 = models.CharField (max_length =255)
    compromiso = models.CharField (max_length =255)
    pretenciones = models.CharField (max_length =255)
    gastos = models.CharField (max_length =255)
    futuro = models.CharField (max_length =255)
    recomienda = models.CharField (max_length =255)
    beneficiosVit = models.CharField (max_length =255)
    firma = models.CharField (max_length =255)
    opinionRef = models.CharField (max_length =255)
    opinionMer = models.CharField (max_length =255)
    suvenir = models.CharField (max_length =100)
    razonSuvenir = models.CharField (max_length =255)
    ganarGente = models.CharField (max_length =255)
    reaccion = models.CharField (max_length =255)
    correr = models.CharField (max_length =255)
    velocidad = models.CharField (max_length =255)
    ciudad = models.CharField (max_length =255)
    razonCiudad = models.CharField (max_length =255)
    metaVida = models.CharField (max_length =255)
    familiaIdent = models.CharField (max_length =255)
    sitPais = models.CharField (max_length =255)
    futuroHijo = models.CharField (max_length =255)
    finesSemana = models.CharField (max_length =255)
    apodo = models.CharField (max_length =255)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering = ["id"]

class InfoGral(models.Model):
    idsolicitante = models.ForeignKey(Solicitud, db_column='idsolicitante')
    nombreCompleto = models.CharField (max_length =60)
    telefono = models.CharField (max_length =30)
    edoCivil = models.CharField (max_length =20)
    cadadoPor = models.CharField (max_length =30)
    numHijos = models.CharField (max_length = 2)
    nomEsposa = models.CharField (max_length =30)
    ocupacionEsp = models.CharField (max_length =40)
    vivenPadres = models.CharField (max_length =10)
    ocupacionPadres = models.CharField (max_length =50)
    ultimaEmp = models.CharField (max_length =40)
    telEmp = models.CharField (max_length =30)
    nombreJefe = models.CharField (max_length =60)
    puestoJefe = models.CharField (max_length =30)
    razonEmp = models.CharField (max_length =80)
    explicaEmp = models.CharField (max_length = 160)
    demandas = models.CharField (max_length =30)
    explicaDem = models.CharField (max_length =160)
    tieneLic = models.CharField (max_length =3)
    tipoLic = models.CharField (max_length =10)
    numeroLic = models.CharField (max_length =20)
    vigenciaLic = models.CharField (max_length =20)
    casaPropia = models.CharField (max_length =5)
    numHabitantes = models.CharField (max_length =3)


class infohijos(models.Model):
    idsolicitante = models.ForeignKey(Solicitud, db_column='idsolicitante')
    nombre = models.CharField (max_length =60, blank=True)
    edad = models.IntegerField(max_length=2, blank=True)
    ocupacion = models.CharField (max_length =40, blank=True)
