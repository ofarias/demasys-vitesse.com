# coding: utf-8
from django import forms
from models import Solicitudes, conceptos, FORMAS_D_PAGO
from catalogos.models import Economico
from empleados.models import empleado
from cuentas.models import Perfil
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from viajes.models import Ruta, Viaje, Destino
from transportes import settings 
from beneficiarios.models import Benefi
from contable.models import Partidas, Area
from inventario.models import Productos
from django.core.validators import MinValueValidator
from decimal import Decimal

CHOICES = (
	(1, 'Pendiente'),
	(2, 'Aprobado'),
	(3, 'Rechazado'),
	(4, 'Pagado'),
	(5, 'Cancelado'),
)

OPCIONES_CONCEPTO = (
	(1, 'Mantenimientos'),
	(2, u'Compra de Piezas'),
	(3, 'Prestamos'),
	(4, 'Retrabajos'),
	(5, u'Viaje (Carta Porte)'),
	(6, 'Viaticos'),
	(7, 'Maniobras'),
) 

CAMPOS = (
    ('pk', u'Folio'),
    ('solicitante_id',u'Solicitante'),
    ('beneficiario_id',u'Operador'),
    ('benef_otros_id',u'Beneficiario'),
    ('fecha',u'Fecha'),
    ('status',u'Estado'),
    ('importe_asig',u'Importe Asignado'),
    ('fecha_asig',u'Fecha de Asignación'),
    ('sol_bill_id',u'Carta Porte'),
    ('refer',u'Referencia'),
    ('forma_pago',u'Forma de Pago'),
    ('motivo_rech',u'Motivo de Rechazo'),
    ('fecha_aut',u'Fecha de Autorización'),
    ('fecha_canc',u'Fecha de Cancelación'),
    ('cancelado',u'Cancelado'),
    ('concepts_id',u'Conceptos'),
    ('kilometraje', u'Kilometraje'),
    ('cliente_paga', u'Paga Cliente'),
    ('id_unidad',u'Unidad')


)
class SearchForm(forms.Form): ###index

	pk = forms.IntegerField(required = False)
	solicitante = forms.ModelChoiceField(queryset = Perfil.objects.all(),required = False)
	beneficiario = forms.ModelChoiceField(queryset = empleado.objects.filter(puesto=10),required = False) ##Cambio para llamar solo los operadores Activos.
	fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = False)
	importe_asig = forms.IntegerField(required=False)
	status = forms.MultipleChoiceField(choices = CHOICES, required = False)
	refer = forms.CharField (max_length = 50, required= False)
	sol_bill = forms.ModelChoiceField(queryset = Viaje.objects.all(),required = False)
	concepts = forms.ModelChoiceField(queryset = conceptos.objects.all(), required = False)
	fecha_aut = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS,required = False)
	motivo_rech = forms.CharField (max_length = 25, required = False)
	benef_otros = forms.ModelChoiceField(queryset= Benefi.objects.all(),required=False)
	cancelado = forms.NullBooleanField(required = False)	
	destino = forms. ModelChoiceField(queryset = Destino.objects.all(),required = False)

	def __init__ (self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['pk'].widget.attrs['class']='form-control form-fiter input-sm'
		self.fields['solicitante'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['beneficiario'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['fecha'].widget.attrs['class']='form-control form-filter input-sm'
		self.fields['importe_asig'].widget.attrs['class']='form-control forms-filter input-sm'
		self.fields['status'].widget.attrs['class']='form-control form-filter input-sm select2 '
		self.fields['refer'].widget.attrs['class']='form-control form-filter input-sm'
		self.fields['sol_bill'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['concepts'].widget.attrs['class']='form-control form-filter input-sm select2-container'
		self.fields['fecha_aut'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['motivo_rech'].widget.attrs['class']='form-control form-filter input-sm'
		self.fields['benef_otros'].widget.attrs['class']='form-control form-filter input-sm'
		self.fields['cancelado'].widget.attrs['class']='form-control form-filter input-sm'
		self.fields['destino'].widget.attrs['class']='form-control form-filter input-sm'


class SolicitudForm (forms.ModelForm):  ###Agregar

	
	
	beneficiario = forms.ModelChoiceField(queryset=empleado.objects.filter(puesto = 10), required = False)###Cambiamos la propiedad de objects para filtrar solo los operadores activos.
	sol_bill = forms.ModelChoiceField(queryset = Viaje.objects.all(), required= False)
	benef_otros = forms.ModelChoiceField(queryset=Benefi.objects.all(), required = False)
	fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = True)
	cliente_paga = forms.DecimalField(max_digits = 10, decimal_places = 2, required = False)
	kilometraje = forms.DecimalField(max_digits = 10, decimal_places = 2, required = False)
	id_unidad = forms.ModelChoiceField(queryset = Economico.objects.all(), required = False)
	producto = forms.ModelChoiceField(queryset = Productos.objects.all(),required = False)
	unidades = forms.DecimalField(max_digits = 8, decimal_places = 2, required =  False, initial= Decimal('0.00'))
	#concepts = forms.ModelChoiceField(queryset = conceptos.objects.all(), required = False)	

		
	class Meta:
		model = Solicitudes
		fields = [
	#		'solicitante',
			'beneficiario',
			'fecha',
			'importe_asig',
			'concepts',
			'sol_bill',
			'refer',
			'benef_otros',
			'cliente_paga',
			'kilometraje',
			'id_unidad',
			'status',
			'producto',
			'unidades',

		]

	def clean_password(self):
		return ''
	def __init__(self, *args, **kwargs):
		super (SolicitudForm,self).__init__(*args, **kwargs)
	#	self.fields['solicitante'].widget.attrs['class']='form-control'
		self.fields['beneficiario'].widget.attrs['class']='form-control'
		self.fields['fecha'].widget.attrs['class']='form-control'
		self.fields['importe_asig'].widget.attrs['class']='form-control'
		self.fields['concepts'].widget.attrs['class']='form-control'
		self.fields['sol_bill'].widget.attrs['class']='form-control'
		self.fields['refer'].widget.attrs['class']='form-control'
		self.fields['benef_otros'].widget.attrs['class']='form-control'
		self.fields['cliente_paga'].widget.attrs['class']='form-control'
		self.fields['kilometraje'].widget.attrs['class']='form-control'
		self.fields['id_unidad'].widget.attrs['class']='form-control'
		self.fields['status'].widget.attrs['class']='form-control'
		self.fields['producto'].widget.attrs['class']='form-control'
		self.fields['unidades'].widget.attrs['class']='form-control'
		#self.fields['sol_bill'].widget.attrs['class']='form-control'
	



class Sol_Edit_1_Form(forms.ModelForm): ##Autorizar
	
	beneficiario = forms.ModelChoiceField(queryset = empleado.objects.filter(puesto = 10 ),required = False)
	sol_bill = forms.ModelChoiceField(queryset = Viaje.objects.all(), required= False)
	benef_otros = forms.ModelChoiceField(queryset=Benefi.objects.all(), required = False)	
	motivo_rech = forms.CharField(required= False)
	fecha = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS, required = True)
	fecha_aut = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS, required  = True)
	cliente_paga = forms.DecimalField(max_digits = 10, decimal_places = 2, required = False)
	kilometraje = forms.DecimalField(max_digits = 10, decimal_places = 2, required = False)
	id_unidad = forms.ModelChoiceField(queryset = Economico.objects.all(), required = False)
	##status = forms.MultipleChoiceField(choices = CHOICES, required = False)
		

	##solicitante = forms.ForeignKey (required= False)    ## forms.CharField(required= False)

	class Meta: 
		model = Solicitudes
		fields = [
			'solicitante',
			'beneficiario',
			'fecha',
			'importe_asig',
			'concepts',
			'sol_bill',
			'status',
			'refer',
			'fecha_aut',
			'motivo_rech',
			'benef_otros',
			'cliente_paga',
			'kilometraje',
			'id_unidad',
		]
	
	def __init__(self, *args, **kwargs):
		super (Sol_Edit_1_Form,self).__init__(*args,**kwargs)
		instance = getattr(self, 'instance', None)
		if instance and instance.id:
			self.fields['solicitante'].widget.attrs['class']='form-control'
			self.fields['beneficiario'].widget.attrs['class']='form-control'
			self.fields['fecha'].widget.attrs['class']='form.control'
			self.fields['fecha'].widget.attrs['readonly'] = 'readonly'  ###['class']='form-control'
			self.fields['importe_asig'].widget.attrs['class']='form-control'
			self.fields['concepts'].widget.attrs['class']='form-control'
			self.fields['sol_bill'].widget.attrs['class']='form-control'
			self.fields['refer'].widget.attrs['class']='form-control'
			self.fields['fecha_aut'].widget.attrs['class']='form-control'
			self.fields['motivo_rech'].widget.attrs['class']='form-control'
			self.fields['benef_otros'].widget.attrs['class']='form-control'
			self.fields['cliente_paga'].widget.attrs['class']='form-control'
			self.fields['kilometraje'].widget.attrs['class']='form-control'
			self.fields['id_unidad'].widget.attrs['class']='form-control'

	
	def clean_fields(self):
		instance = getattr(self,'instance',None)
		if instance:
			return instance.solicitante
		else:
			return self.cleaned_data.get('solicitante',None)
	

class Sol_Edit_2_Form(forms.ModelForm): ###Asignar

	beneficiario = forms.ModelChoiceField(queryset = empleado.objects.filter(puesto = 10),required = False)
	sol_bill = forms.ModelChoiceField(queryset = Viaje.objects.all(), required= False)
	benef_otros = forms.ModelChoiceField(queryset=Benefi.objects.all(), required = False)
	saldo = forms.DecimalField(max_digits = 8, decimal_places = 2, required =  False)
	status = forms.MultipleChoiceField(choices = CHOICES, required = False)
	motivo_rech = forms.CharField(required= False)
	fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = False)
	fecha_aut = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = False)
	fecha_asig = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = False)
	cliente_paga = forms.DecimalField(max_digits = 10, decimal_places = 2, required = False)
	kilometraje = forms.DecimalField(max_digits = 10, decimal_places = 2, required = False)
	id_unidad = forms.ModelChoiceField(queryset = Economico.objects.all(), required = False)
	partida = forms.ModelChoiceField(queryset = Partidas.objects.filter(activo=True),required = True)
	areas = forms.ModelChoiceField(queryset = Area.objects.filter(activo=True),required = True)





	class Meta: 
		model = Solicitudes
		fields = [
			'id',
			'solicitante',
			'beneficiario',
			'fecha',
			'importe_asig',
			'concepts',
			'sol_bill',
			'status',
			'refer',
			'fecha_aut',
			'motivo_rech',
			'fecha_asig',
			'importe_asig',
			'forma_pago',
			'partida',
			'areas',
			'saldo',
			'benef_otros',
			'cliente_paga',
			'kilometraje',
			'id_unidad',
		]


	def __init__(self, *args, **kwargs):
		super (Sol_Edit_2_Form,self).__init__(*args,**kwargs)
		self.fields['solicitante'].widget.attrs['class']='form-control'
		self.fields['beneficiario'].widget.attrs['class']='form-control'
		self.fields['fecha'].widget.attrs['class']='form-control'
		self.fields['importe_asig'].widget.attrs['class']='form-control'
		self.fields['concepts'].widget.attrs['class']='form-control'
		self.fields['sol_bill'].widget.attrs['class']='form-control'
		self.fields['refer'].widget.attrs['class']='form-control'
		self.fields['fecha_aut'].widget.attrs['class']='form-control'
		self.fields['motivo_rech'].widget.attrs['class']='form-control'
		self.fields['fecha_asig'].widget.attrs['class']='form-control'
		self.fields['importe_asig'].widget.attrs['class']='form-control'
		self.fields['forma_pago'].widget.attrs['class']='form-control'
		self.fields['partida'].widget.attrs['class']='form-control'
		self.fields['areas'].widget.attrs['class']='form-control'
		self.fields['benef_otros'].widget.attrs['class']='form-control'
		self.fields['cliente_paga'].widget.attrs['class']='form-control'
		self.fields['kilometraje'].widget.attrs['class']='form-control'
		self.fields['id_unidad'].widget.attrs['class']='form-control'
	


class Sol_Edit_3_Form(forms.ModelForm): ### Cancelar

	##saldo = forms.DecimalField(max_digits = 8, decimal_places = 2, required =  False)	
	##motivo_rech = forms.CharField(required= False)
	fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = False)
	beneficiario = forms.ModelChoiceField(queryset = empleado.objects.filter(puesto = 10),required = False)


	class Meta: 
		model = Solicitudes
		fields = [
			'solicitante',
			'beneficiario',
			'fecha',
			'importe_asig',
			'status',
			'cancelado',
		]

	def __init__(self, *args, **kwargs):
		super (Sol_Edit_3_Form,self).__init__(*args,**kwargs)
		self.fields['solicitante'].widget.attrs['class']='form-control'
		self.fields['beneficiario'].widget.attrs['class']='form-control'
		self.fields['fecha'].widget.attrs['class']='form-control'
		self.fields['importe_asig'].widget.attrs['class']='form-control'
		self.fields['status'].widget.attrs['class']='form-control'
		self.fields['cancelado'].widget.attrs['class']='form-control'

class Report_solForm(forms.Form):
    	
	pk = forms.IntegerField(required=False)
	campos = forms.MultipleChoiceField(choices = CAMPOS, required=False)
	solicitante = forms.ModelChoiceField(queryset = Perfil.objects.all(),required = False)
	operador = forms.ModelChoiceField(queryset = empleado.objects.filter(puesto = 10),required = False)
	benef_otros = forms.ModelChoiceField(queryset= Benefi.objects.all(),required=False)
	fecha_from = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
	fecha_to = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
	status = forms.MultipleChoiceField(choices = CHOICES, required = False)
	sol_bill = forms.ModelChoiceField(queryset = Viaje.objects.all(),required = False)
	forma_pago = forms.MultipleChoiceField(choices = FORMAS_D_PAGO,required = False)
	concepts =forms.ModelChoiceField(queryset = conceptos.objects.all(), required = False)

	def __init__(self, *args, **kwargs):
        	super(Report_solForm, self).__init__(*args, **kwargs)
		self.fields['pk'].widget.attrs['class']='form-control form-filter input-sm'
		self.fields['solicitante'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['operador'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['benef_otros'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['fecha_from'].widget.attrs['class'] = 'form-control form-filter input-sm'
		self.fields['fecha_to'].widget.attrs['class'] = 'form-control form-filter input-sm'        
		self.fields['status'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['sol_bill'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['forma_pago'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['concepts'].widget.attrs['class']='form-control form-filter input-sm select2'

	##def __unicode__(self, *args, **kwargs):
		


class Search_Form_Con(forms.Form):

	nombre_conc = forms.models.ModelChoiceField(queryset = conceptos.objects.all(), required = True)

	def __init__(self, *args, **kwargs):
		super(Search_Form_Con, self).__init__(*args, **kwargs)

		self.fields['nombre_conc'].widget.attrs['class']='form-control form-filter input-sm'

class conceptos_form(forms.ModelForm):
	class Meta:
		model = conceptos
		fields=[
			'nombre_conc',
			'economico',
			'carta_porte',
			'afecta_cp',
		]
	def __init__(self, *args, **kwargs):
		super (conceptos_form,self).__init__(*args,**kwargs)
		self.fields['nombre_conc'].widget.attrs['class']='form-control'
		self.fields['afecta_cp'].widget.attrs['class']='form-control'

class reporteForm(forms.Form):
	id_viaje = forms.CharField(required= False)
	operador = forms.ModelChoiceField(queryset = empleado.objects.filter(puesto = 10),required = False)
	fecha_from = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
	fecha_to = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)

	def __init__(self, *args, **kwargs):
		super(reporteForm, self).__init__(*args, **kwargs)
		self.fields['id_viaje'].widget.attrs['class'] = 'form-control'
		self.fields['operador'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['fecha_from'].widget.attrs['class'] = 'form-control form-filter input-sm '
		self.fields['fecha_from'].widget.attrs['readonly'] = 'readonly'
		self.fields['fecha_to'].widget.attrs['class'] = 'form-control form-filter input-sm'
		self.fields['fecha_to'].widget.attrs['readonly'] = 'readonly'
