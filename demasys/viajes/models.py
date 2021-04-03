# coding: utf-8
from django.db import models
from django.db.models import Sum
from django.conf import settings
from audit_log.models.managers import AuditLog
from catalogos.models import Caseta, Economico, ModeloEconomico
from empleados.models import empleado
from cuentas.models import Perfil
from random import random


import hashlib
from clientes.models import Departamento, Cliente
from workflow.models import WorkflowActivity, State
import os
from decimal import Decimal
from sepomex.templatetags.sepomex_filters import municipio
from datetime import datetime
import datetime


TIPO_GASTO = (
    (1, 'Salida'),
    (2, 'Regreso'),    
)

CONCEPTO_GASTO = [
    'Combustible',
    'Casetas',
    u'Comisión',
    u'Maniobras Locales',
    u'Maniobras Foraneas',
    u'Maniobras Retrabajos',
    'Hospedaje',
    u'Casetas sin IAVE'    
]    

TIPO_RUTA = (
    (1, 'Local'),
    (2, 'Foraneo en ruta'),
    (3, 'Foraneo directo'),
    (4, 'Regreso'),  
)

CONTENIDOS = (
    (u'Equipo de comunicación', u'Equipo de comunicación',),
    (u'Electrónica', u'Electrónica',),
    (u'Especifique', u'Especifique',),
    (u'Linea Blanca', u'Linea Blanca'),
    (u'Mercancia Segun Factura', u'Mercancia Segun Factura'),
)
    
VALORES = (
    (True, 'Vale'),
    (False, 'Efectivo')
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

INCIDENTE =(
    (1, 'Reportado'),
    (2, 'Solicitado'),
    (3, 'Mantenimiento'),
    (4, 'Autorizado'),
    (5, 'Cerrado'),
    (6, 'Rechazado'),
    (7, 'Revisado'),
    )

INCIDENTE2=(
    (1, 'Autorizar'),
    (2, 'Rechazar'),
    (3, 'Revisar'),
    )

ARCHIVOS=(
    (1, u'Imagen JPG'),
    (2, u'Imagen PNG'),
    (3, u'Presentacion Power Point'),
    (4, u'Hoja de Calculo Excel'),
    (5, u'Archivo PDF'),
    (6, u'Documento Word'),
    (7, u'Desconocido'),
    )
SEG_DOCS=(
    (1, u'Salida'),
    (2, u'Chofer'),
    (3, u'Cliente1'),
    (4, u'Cliente2'),
    (5, u'Facturar'),
    (6, u'Sabana'),
    (11, u'S_Pendiente'),
    (12, u'C_Pendinete'),
    (13, u'Cl_Pendiente'),
    (14, u'Cl2_Pendiente'),
    (15, u'F_Pendiente'),
    (16, u'S_Pendiente'),
    )


STATUS_SOLICITUD=(
    (1, u'Nuevo'),
    (2, u'Atendido')
    )


def get_comprobante_path(instance, filename):
    """
    Devuelve un path generado mediante el hash del nombre del archivo.
    
    @param filename: Referencia al archivo
    @type filename: file
    
    @rtype: string
    @return: Cadena con el path donde quedará almacenado el archivo
    """
    params = (
        instance.viaje.pk, 
        hashlib.sha1("%s-%f" % (filename.encode('utf-8'), random())).hexdigest(), 
        filename.split('.')[-1]
    )
    return "comprobantes/%s/%s.%s" % params

def get_comprobante_gasto_path(instance, filename):
    """
    Devuelve un path generado mediante el hash del nombre del archivo.
    
    @param filename: Referencia al archivo
    @type filename: file
    
    @rtype: string
    @return: Cadena con el path donde quedará almacenado el archivo
    """
    params = (
        instance.gasto.pk, 
        hashlib.sha1("%s-%f" % (filename.encode('utf-8'), random())).hexdigest(), 
        filename.split('.')[-1]
    )
    return "comprobantes/%s/%s.%s" % params

class Ruta(models.Model):
    nombre = models.CharField(max_length=250)  
    casetas_salida = models.ManyToManyField(Caseta, related_name="salida")
    casetas_regreso = models.ManyToManyField(Caseta, related_name="regreso", blank=True, null=True) 
    activo = models.BooleanField(default=True) 
    
    def salida_total_auto(self):
        q = self.casetas_salida.aggregate(total=Sum('autos'))
        return q['total'] or 0
        
    def salida_total_camioneta(self):
        q = self.casetas_salida.aggregate(total=Sum('autobus_2_ejes'))
        return q['total'] or 0
    
    def regreso_total_auto(self):
        q = self.casetas_regreso.aggregate(total=Sum('autos'))
        return q['total'] or 0
        
    def regreso_total_camioneta(self):
        q = self.casetas_regreso.aggregate(total=Sum('autobus_2_ejes'))
        return q['total'] or 0
    
    def __unicode__(self):
        return self.nombre
    
    class Meta:
        ordering = ["nombre"] 

class Viaje(models.Model):
    cliente = models.ForeignKey(Cliente)
    departamento = models.ForeignKey(Departamento)
    economico = models.ForeignKey(Economico)
    operador = models.ForeignKey(empleado)
    ruta = models.ForeignKey(Ruta)
    tipo_ruta = models.IntegerField(choices=TIPO_RUTA, default=3)
    referencia = models.CharField('Shipment/Bill/Load', max_length=150, blank=True, null=True)
    contiene = models.CharField(max_length=200)
    fecha_salida = models.DateField()    
    origen_clave_municipio = models.CharField(max_length = 100)    
    origen_colonia = models.CharField(max_length=150)
    origen_calle = models.CharField(max_length=150)
    origen_numero = models.CharField(max_length=100)
    origen_cp = models.CharField(max_length=5)
    factura = models.CharField(max_length=150, blank=True, null=True)
    facturacion_forma_pago = models.CharField(max_length=120, blank=True, null=True)
    facturacion_banco = models.CharField(max_length=120, blank=True, null=True)
    facturacion_documento = models.CharField(max_length=120, blank=True, null=True)
    facturacion_casetas = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    facturacion_flete = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    facturacion_maniobra = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    facturacion_reparto = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    facturacion_desvio = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    facturacion_ferri = models.DecimalField(max_digits=9, decimal_places=2, default=0)   
    facturacion_otros = models.DecimalField(max_digits=9, decimal_places=2, default=0) 
    observaciones = models.TextField(blank=True, null=True)
    facturacion_fecha_fac = models.DateField()
    maniobras_locales = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    maniobras_foraneas = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    maniobras_retrabajos = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    casetas_lg =models.DecimalField(max_digits=9, decimal_places=2, default=0)
    fecha_ent=models.DateField(blank=True, null=True)
    fecha_entmcia=models.DateField(blank=True, null=True)
    evidencia=models.FileField(upload_to='imgEvidencia', blank=True, null=True)
    factura_subtotal=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    factura_iva= models.DecimalField(max_digits=9, decimal_places=2, default=0)
    factura_retenciones=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    factura_total=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    factura_fecha_pago = models.DateField(blank = True, null = True)        
    flujo = models.ForeignKey(WorkflowActivity, null=True, blank=True, unique=True)
    facturacion_incentivo=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    facturacion_penalizacion=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    facturacion_detencion=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    facturacion_fecha_pago = models.DateField()
    status_doc = models.IntegerField(choices=SEG_DOCS, null = False, default=1)
    libera_chofer = models.DateTimeField()
    u_libera_chofer = models.CharField(max_length=100, null = True)
    liberado_cliente = models.DateTimeField()
    u_liberado_cliente = models.CharField(max_length=100, null = True)
    entrego_cliente = models.DateTimeField()
    u_entrego_cliente = models.CharField(max_length=100, null=True)
    recibido_facturacion = models.DateTimeField()
    u_recibido_facturacion = models.CharField(max_length=100, null = True)
    sabana = models.DateTimeField()
    u_sabana=models.CharField(max_length=100, null= True)
    factura_pendiente = models.IntegerField(null= True)
    


    def _get_subtotal(self):
        return self.importe()
    subtotal = property(_get_subtotal)
        
    def _get_iva(self):        
        return self.subtotal * Decimal(0.16)  
    iva = property(_get_iva)
    
    def _get_retencion(self):
        return self.facturacion_flete * Decimal(0.04)
    retencion = property(_get_retencion)
    
    def _get_total(self):
        return self.subtotal + self.iva - self.retencion
    total = property(_get_total)
    
    def gastos_maniobras(self):
        gastos = self.gasto_set.filter(concepto='Maniobras', tipo=2)
        maniobras = 0
        for gasto in gastos:
            maniobras += gasto.total_pagado
        
        return maniobras
    
    def gastos_casetas(self):
        gastos = self.gasto_set.filter(concepto='Casetas', tipo=2)
        casetas = 0
        for gasto in gastos:
            casetas += gasto.total_pagado
        
        return casetas
    
    def gastos_otros(self):
        gastos = self.gasto_set.exclude(concepto__in=['Casetas', 'Maniobras'], tipo=2)
        otros = 0
        for gasto in gastos:
            otros += gasto.total_pagado
        
        return otros
    
    def importe(self):
        return self.facturacion_flete + self.facturacion_maniobra + self.facturacion_reparto + self.facturacion_desvio + self.facturacion_ferri + self.facturacion_otros + self.facturacion_casetas
        
    def gastos_salida(self):
        return self.gasto_set.filter(tipo=1)
    
    def gastos_regreso(self):
        return self.gasto_set.filter(tipo=2)
    
    def gastos_salida_total(self):
        gastos = self.gastos_salida()
        total = 0
        for gasto in gastos:
            total += gasto.total_pagado
            
        return total
    
    def gastos_regreso_total(self):
        gastos = self.gastos_regreso()
        total = 0
        for gasto in gastos:
            total += gasto.total_pagado
            
        return total 
    
    def get_destinos(self):
        destinos = []
        for destino in self.destino_set.all():
            destinos.append(municipio(destino.destino_clave_municipio))
        return ', '.join(destinos)       
    destinos = property(get_destinos)
    
    def __unicode__(self):
        return str(self.pk).zfill(4)
    
    class Meta:
        ordering = ["-fecha_salida"] 

class Destino(models.Model):
    viaje = models.ForeignKey(Viaje)
    destino_clave_municipio = models.CharField(max_length = 100)    
    destino_nombre = models.CharField(max_length=150, blank=True, null=True)    
    destino_colonia = models.CharField(max_length=150, blank=True, null=True)
    destino_calle = models.CharField(max_length=150, blank=True, null=True)
    destino_numero = models.CharField(max_length=100, blank=True, null=True)
    destino_cp = models.CharField(max_length=5, blank=True, null=True) 
    fecha_entrega = models.DateField(blank=True, null=True)
    comprobante_entrega = models.FileField(upload_to=get_comprobante_path, blank=True, null=True)
    comprobante_entrega_otro = models.FileField(upload_to=get_comprobante_path, blank=True, null=True)
    
    def __unicode__(self):
        return self.destino_clave_municipio
    
    
 
class Gasto(models.Model):
    tipo = models.IntegerField(choices=TIPO_GASTO)
    concepto = models.CharField(max_length=150)
    comentarios = models.TextField(null=True, blank=True)
    viaje = models.ForeignKey(Viaje)
    calculado = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pagado_operaciones = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    pagado_contabilidad = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    vale_operaciones = models.BooleanField(choices=VALORES) #salida
    vale_contabilidad = models.BooleanField(choices=VALORES) #salida
    efectivo_operaciones = models.BooleanField(choices=VALORES) #rebgreso
    efectivo_contabilidad = models.BooleanField(choices=VALORES) #regreso

    def _get_total_pagado(self):
        if self.pagado_operaciones is None and self.pagado_contabilidad is not None:
            return self.pagado_contabilidad
        elif self.pagado_contabilidad is None and self.pagado_operaciones is not None:
            return self.pagado_operaciones
        elif self.pagado_contabilidad is not None and self.pagado_operaciones is not None:
            return self.pagado_contabilidad + self.pagado_operaciones
        else:
            return 0    
    total_pagado = property(_get_total_pagado)
    
    def _get_diferencia(self):
        if self.total_pagado is not None and self.calculado is not None:
            return self.total_pagado - self.calculado
        else:
            return False
    diferencia = property(_get_diferencia)
    
    def __unicode__(self):
        return self.concepto
    

class Comprobante(models.Model): 
    gasto = models.ForeignKey(Gasto)
    archivo = models.FileField(upload_to=get_comprobante_gasto_path)
    
    def filename(self):
        return os.path.basename(self.archivo.name)

    def __unicode__(self):
        return self.gasto
    
class ViajeStatus(models.Model):
    workflowactivity = models.OneToOneField(Viaje, to_field='flujo', primary_key=True)
    state = models.ForeignKey(State)
    created_on = models.DateTimeField()
    days = models.IntegerField()
    
    def __unicode__(self):
        return unicode(self.workflowactivity)
    
    class Meta:
        db_table = 'workflow_stats'
        managed = False    


#Modificaciones carga excel
class ExcelViaje(models.Model):
    docfile = models.FileField(upload_to='upload')
    usuario = models.CharField(max_length = 100, null = True)
    facturas= models.CharField(max_length=100, null = True)
    bill = models.CharField(max_length=45, null = True)
    fecha_upload=models.DateTimeField(null= True)

    class Meta:
        permissions = (
            ( "read_excelViaje", "Can read Car" ),
        )
#CARGA PDF 
class CargaPdf(models.Model):
    id   = models.AutoField(primary_key = True)
    docfile = models.CharField(max_length=250)
    fecha = models.DateField(default=datetime.date.today)
    activo = models.BooleanField(default=True)
    idCliente = models.ForeignKey(Cliente, db_column='idcliente')
    viaje = models.IntegerField(null = True)
    bill = models.CharField(max_length=100, null = True)
    fecha_ts=models.DateTimeField(null=True)

    def __unicode__(self):
        return self.docfile

class Movimiento(models.Model):
    nombre=models.CharField(max_length=250)
    observaciones=models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre

class MovUnidad(models.Model):
    tipo=models.IntegerField(choices= STATUS, null =True)
    obs=models.CharField(max_length=200, null=True)
    fechai=models.DateField(null=True, blank=True )
    fechaf=models.DateField(null=True, blank= True)
    fechamcia=models.DateField(null= True, blank = True) 
    operador=models.ForeignKey(empleado, null=True)
    unidad=models.ForeignKey(Economico, null=True)
    estatus=models.IntegerField(choices=STATUS, null=True)
    usuario=models.ForeignKey(Perfil, null=True)
    ts=models.DateField( null = True)
    modelo=models.ForeignKey(ModeloEconomico, null=True)
    destino=models.CharField(max_length =200, null=True)
    destino2=models.CharField(max_length=200, null=True)
    cliente=models.ForeignKey(Cliente, null=True)
    tiempo=models.DateField(null=True)
    departamento=models.ForeignKey(Departamento, null=True)
    enviaje= models.IntegerField(null= True)
    email = models.IntegerField(null=True, default = 0) 
    #cmuni=models.CharField(null = True)
    #asenta= models.CharField(null= True)

    #def destino(self):
    #   municipios = Sepomex.objects.filter(clave_municipio= cmuni, id_asenta_cpcons= asenta)
    #    for muni in municipios:
    #        return muni.municipio  ###clave_municipio y id_asenta_cpcons

class ReporteUnidad(models.Model):
    usuario=models.CharField(max_length='100', null = True)
    reporta=models.ForeignKey(Economico, null=True)
    dano=models.CharField(max_length=200, null= True)
    imagen1 = models.ImageField(upload_to='imgEconomicos', blank=True, null=True)
    imagen2 = models.ImageField(upload_to='imgEconomicos', blank=True, null=True)
    imagen3 = models.ImageField(upload_to='imgEconomicos', blank=True, null=True)
    imagen4 = models.ImageField(upload_to='imgEconomicos', blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True, null=True)
    obs = models.TextField(null= True)
    status=models.IntegerField(choices=INCIDENTE, null = True, default = 1)
    status2=models.IntegerField(choices=INCIDENTE2, null=True, default=0)
    motivo=models.TextField(max_length=250, null=True)
    fecha_AR=models.DateTimeField(null= True )
    fecha_rev=models.DateTimeField(null= True)
    obsrevision=models.TextField(max_length=255, null=True)
    urevision=models.CharField(max_length=100, null=True)


    def __unicode__(self):
        return str(self.pk)

    class Meta:
        ordering=["-fecha"]

class Archivos(models.Model):
    nombre = models.CharField(max_length=200, null = False)
    fecha = models.DateTimeField(null= False)
    tipo = models.IntegerField(choices = ARCHIVOS, null=False)
    desc = models.CharField(max_length=255, null = False)
    archivo = models.ImageField(upload_to='imgEconomicos/files', blank=True, null= False)

    def __unicode__(self):
        return str(nombre)

    class Meta:
        ordering=["-fecha"]

class Facturas(models.Model):
    factura=models.CharField(max_length=20, null = False)
    monto = models.DecimalField(max_digits=9, decimal_places=2, null = False)
    fecha_emision = models.DateField(null = True)
    fecha_pago = models.DateField(null =True)
    pagado = models.DecimalField(max_digits=9, decimal_places=2, null = True)
    saldo = models.DecimalField(max_digits=9, decimal_places=2, null = True)
    banco = models.CharField(max_length=45, null= True)
    cuenta = models.CharField(max_length=45, null = True)

    def __unicode__(self):
        return str(self.factura)
    class Meta:
        ordering=["-fecha_emision"]

class Pagos(models.Model):
    factura = models.CharField(max_length=20, null = False)
    fecha_factura= models.DateField(null = False)
    fecha_pago = models.DateField(null = False)
    monto = models.DecimalField(max_digits=9, decimal_places=2, null = False)
    banco = models.CharField(max_length=45, null= True)
    cuenta = models.CharField(max_length=45, null = True)

    def __unicode__(self):
        return(self.pk)

        class Meta:
            ordering=["-pk"]

class SolicitudesViaje(models.Model):
    cliente = models.ForeignKey(Cliente, db_column='cliente')
    departamento = models.ForeignKey(Departamento, db_column='departamento')
    economico = models.ForeignKey(Economico, db_column='economico')
    operador = models.ForeignKey(empleado, db_column='operador')
    ruta = models.ForeignKey(Ruta, db_column='ruta')
    tipo_ruta = models.IntegerField(choices=TIPO_RUTA)
    referencia = models.CharField(max_length=150, blank=True, null=True)
    contiene = models.CharField(max_length=200)
    fecha_salida = models.DateField()
    origen_clave_municipio = models.CharField(max_length = 100)
    origen_colonia = models.CharField(max_length=150)
    origen_calle = models.CharField(max_length=150)
    origen_numero = models.CharField(max_length=100)
    origen_cp = models.CharField(max_length=5)
    observaciones = models.TextField(blank=True, null=True)
    estatus =  models.IntegerField(choices = STATUS_SOLICITUD, null=False)

    def __unicode__(self):
        return self.pk

    class Meta:
        ordering=["-fecha_salida"]

class Prefacturas(models.Model):
    tc = models.CharField(max_length = 4)
    viaje = models.IntegerField(null = True)
    cuenta = models.CharField(max_length = 10)
    descripcion = models.CharField(max_length = 50)
    cv = models.CharField(max_length = 100)
    fte = models.CharField(max_length = 10)
    flete = models.CharField(max_length = 30)
    maniobras = models.CharField(max_length = 30)
    estadias = models.CharField(max_length = 30)
    cve = models.CharField(max_length = 30)
    otros = models.CharField(max_length = 30)
    cargosImport = models.CharField(max_length = 30)
    subtotalImporte = models.CharField(max_length = 30)
    porcentajeIva = models.CharField(max_length = 30)
    importeIva = models.CharField(max_length = 30)
    porcentaje = models.CharField(max_length = 30)
    retencionImporte = models.CharField(max_length = 30)
    guiaImporte = models.CharField(max_length = 30)
    lineaTransporte = models.CharField(max_length = 30)
    guia = models.CharField(max_length = 30)
    origen = models.CharField(max_length = 30)
    nombreOrigen = models.CharField(max_length = 50)
    fecha = models.CharField(max_length = 30)
    parentInv = models.CharField(max_length = 30)
    fechaCarga = models.CharField(max_length = 15)
    cliente = models.ForeignKey(Cliente)
    casetas= models.CharField(max_length= 20)



class ArchivoPrefacturas(models.Model):
    archivo = models.FileField(upload_to='prefactura', max_length=100)