import os
from django.db import models
from audit_log.models.managers import AuditLog
from cuentas.models import Perfil 
from catalogos.models import Operador, Economico
from viajes.models import Viaje, Ruta
from beneficiarios.models import Benefi
from empleados.models import empleado

TIPO_STATUS = (
	(1, 'Pendiente'),
	(2, 'Aprobado'),
	(3, 'Rechazado'),
	(4, 'Pagado'),
	(5, 'Cancelado'),
	(6, 'Vencida'),
	(7, 'Completa'),
)

OPCIONES_CONCEPTO = (
	(1, 'Mantenimientos'),
	(2, u'Compra de Piezas'),
	(3, 'Prestamos'),
	(4, 'Retrabajos'),
	(5, u'Viaje (Carta Porte)'),
	(6, 'Viaticos'),
	(7, 'Maniobras'),
	(8, 'Comprobada'),
) 

FORMAS_D_PAGO = (
	(1, ''),
	(2, 'Transferencia'),
	(3, u'Deposito en Efectivo'),
	(4, 'Cheque'),
	(5, 'Vales'),
)

DOCUMENTOS=(
	(1, u'Factura Fiscal'),
	(2, u'Remision o Nota'),
	(3, u'Vale Gasolina'),
	(4, u'Vale de Caja'),
	)

class Solicitudes(models.Model):
	solicitante = models.ForeignKey (Perfil) 
	beneficiario = models.ForeignKey (empleado, null = True) ## cambio de nombre del campo de beneficiario por operador.
	fecha = models.DateField ()
	importe = models.DecimalField(max_digits = 10, decimal_places = 2)
	status = models.IntegerField(choices=TIPO_STATUS, default = 1)
	importe_asig = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
	fecha_asig = models.DateField(null = True)
	#concepto = models.IntegerField(choices =OPCIONES_CONCEPTO, null = True, default = 1)
	sol_bill = models.ForeignKey (Viaje, null = True)
	refer = models.CharField(max_length= 200)
	forma_pago = models.IntegerField(choices = FORMAS_D_PAGO, null = True, default = 1)
	motivo_rech = models.CharField(max_length = 100)
	fecha_aut = models.DateField()
	saldo = models.DecimalField(max_digits = 8, decimal_places = 2, null = True)
	fecha_canc = models.DateField(null = True)
	cancelado = models.NullBooleanField(null = True) 
	destino = models.ForeignKey (Ruta,null =True)
	concepts = models.ForeignKey ('conceptos', null = True)
	benef_otros = models.ForeignKey(Benefi, null = True)
	cliente_paga = models.DecimalField(max_digits  = 10, decimal_places = 2, null = True)
	kilometraje = models.DecimalField(max_digits = 10, decimal_places = 2, null = True)
	id_unidad = models.ForeignKey (Economico, null = True)
	documento = models.IntegerField(choices = DOCUMENTOS, null = False, default= 1)
	fecha_vencimiento = models.DateField(null=False)
	archivo_pdf = models.CharField(max_length= 2)
	archivo_xml = models.CharField(max_length= 2)
	archivo_jpg = models.CharField(max_length= 2)
	#archivo_pdf = models.ImageField(upload_to='imgEconomicos/files', blank=True, null=True)
	#archivo_xml = models.ImageField(upload_to='imgEconomicos/files', blank=True, null=True)
	#archivo_jpg = models.ImageField(upload_to='imgEconomicos/files', blank=True, null=True)
	
	def __unicode__(self):
		return str (self.pk).zfill(4)
	
	def __refer__(self):
		return str (self.refer)

	class Meta: 
		ordering = ["fecha"]

class conceptos (models.Model):
	nombre_conc = models.CharField(max_length = 50, null= False)
	afecta_cp = models.BooleanField(null = False, default = 0)
	economico = models.BooleanField()
	carta_porte = models.BooleanField()
	comprobante_fiscal = models.BooleanField()
	comprobante_no_fiscal = models.BooleanField()

	
	def __unicode__(self):
		return self.nombre_conc
	class Meta:
		ordering = ["nombre_conc"]

def get_file_path(instance, filename):
    filename = "%s_%s_%s" % (instance.idSolicitud, instance.tipo, filename)
    return os.path.join('pendientes', filename)

class ArchivoPendiente(models.Model):
    idSolicitud = models.IntegerField()
    tipo = models.CharField(max_length = 3, null= False)
    archivo = models.FileField(upload_to=get_file_path, max_length=100)
    #desc = models.CharField(max_length=255, null = False)
    #archivo = models.FileField(upload_to='pendientes')



    #def __unicode__(self):
    #    return self.pk
	#class Meta:
    #    ordering = ["id"]

