# coding: utf-8
from django import forms
from django.forms import ModelForm,Form,FileField
from models import Viaje, ReporteUnidad
from django.db.models import Q

from transportes import settings
from viajes.models import Ruta, Gasto, Destino, Comprobante, CargaPdf, Movimiento, MovUnidad, Archivos, SolicitudesViaje, ArchivoPrefacturas, Prefacturas
from viajes.widgets import MetronicFileInput
from clientes.models import Cliente, Departamento
from catalogos.models import Economico, Operador
from empleados.models import empleado
from workflow.models import State

CAMPOS = (
    ('workflowactivity__pk',u'Carta Porte'),
    ('state',u'Status'),    
    ('workflowactivity__cliente',u'Cliente'),
    ('workflowactivity__departamento',u'Departamento'),
    ('workflowactivity__economico',u'Económico'),
    ('workflowactivity__operador',u'Operador'),
    ('workflowactivity__ruta',u'Ruta'),
    ('workflowactivity__tipo_ruta',u'Tipo de Ruta'),
    ('workflowactivity__referencia',u'Bill/Load'),
    ('workflowactivity__contiene',u'Contenido'),
    ('workflowactivity__fecha_salida',u'Fecha de Salida'),
    ('workflowactivity__origen_colonia',u'Origen Colonia'),
    ('workflowactivity__origen_calle',u'Origen Calle'),
    ('workflowactivity__origen_numero',u'Origen Número'),
    ('workflowactivity__origen_cp',u'Origen CP'),
    ('workflowactivity__destinos',u'Destino'),
    ('workflowactivity__factura',u'Factura'),
    ('workflowactivity__facturacion_forma_pago',u'Forma de Pago (Facturación)'),
    ('workflowactivity__facturacion_banco',u'Banco (Facturación)'),
    ('workflowactivity__facturacion_documento',u'Documento (Facturación)'),
    ('workflowactivity__facturacion_casetas',u'Casetas (Facturación)'),
    ('workflowactivity__casetas_lg',u'Casetas LG (Facturación)'),
    ('workflowactivity__facturacion_flete',u'Flete (Facturación)'),
    ('workflowactivity__facturacion_maniobra',u'Maniobra (Facturación)'),
    ('workflowactivity__facturacion_reparto',u'Reparto (Facturación)'),
    ('workflowactivity__facturacion_desvio',u'Desvio (Facturación)'),
    ('workflowactivity__facturacion_ferri',u'Ferri (Facturación)'),
    ('workflowactivity__facturacion_otros',u'Otros (Facturación)'),    
    ('workflowactivity__subtotal',u'Subtotal (Facturación)'),
    ('workflowactivity__iva',u'IVA (Facturación)'),
    ('workflowactivity__retencion',u'Retención (Facturación)'),
    ('workflowactivity__total',u'Total (Facturación)'),
    ('workflowactivity__observaciones',u'Observaciones'),
    ('workflowactivity__facturacion_fecha_fac', u'Fecha de Factura'),
    ('workflowactivity__facturacion_fecha_pago', u'Fecha de Pago'),
    ('workflowactivity__fecha_ent',u'Fecha Entrega'),
    ('workflowactivity__fecha_entmcia',u'Fecha Entrega Mercancia'),
)

ESTATUS = (
     (1, 'Activo'),
     (2, 'Mantenimiento'),
     (3, u'Taller (Mecanica)'),
     (4, u'Taller (Hojalateria / Pintura)'),
     (5, u'Corralon'),
     (6, 'Descompuesto'),
     (7, 'Siniestro (Aseguradora)'),
     (8, 'Otro'),
)

INCSTATUS=(
    (1, 'AUTORIZAR'),
    (2, 'RECHAZAR'),
)


class SearchForm(forms.Form):
    pk = forms.IntegerField(required=False)
    status = forms.ModelChoiceField(queryset=State.objects.filter(workflow__pk=1),required=False)
    fecha_from = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    fecha_to = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(activo=True), required=False)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.filter(activo=True), required=False)
    destino = forms.CharField(max_length=150, required=False, widget=forms.HiddenInput)
    referencia = forms.CharField(max_length=20, required=False)
    economico = forms.ModelChoiceField(queryset=Economico.objects.filter(activo=True), required=False)
    operador = forms.ModelChoiceField(queryset=empleado.objects.filter(Q(puesto =8)|Q(puesto =9)|Q(puesto=10)|Q(puesto=11)|Q(puesto=12)), required = False)
    
    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['pk'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['status'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['fecha_from'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['fecha_from'].widget.attrs['placeholder'] = 'Del'
        self.fields['fecha_to'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['fecha_to'].widget.attrs['placeholder'] = 'Al'
        self.fields['cliente'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['departamento'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['destino'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['referencia'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['economico'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['operador'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        
class ReportForm(forms.Form):
    pk = forms.IntegerField(required=False)
    campos = forms.MultipleChoiceField(choices=CAMPOS, required=False)
    status = forms.ModelChoiceField(queryset=State.objects.filter(workflow__pk=1),required=False)
    fecha_from = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    fecha_to = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(activo=True), required=False)
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.filter(activo=True), required=False)
    destino = forms.CharField(max_length=150, required=False, widget=forms.HiddenInput)
    referencia = forms.CharField(max_length=20, required=False)
    economico = forms.ModelChoiceField(queryset=Economico.objects.filter(activo=True), required=False)
    operador = forms.ModelChoiceField(queryset=empleado.objects.filter(Q(puesto =8)|Q(puesto =9)|Q(puesto=10)|Q(puesto=11)|Q(puesto=12)), required = False)
    
    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.fields['pk'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['status'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['fecha_from'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['fecha_from'].widget.attrs['placeholder'] = 'Del'
        self.fields['fecha_to'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['fecha_to'].widget.attrs['placeholder'] = 'Al'
        self.fields['cliente'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['departamento'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['destino'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['referencia'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['economico'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['operador'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['campos'].widget.attrs['class'] = 'form-control form-filter input-sm'        

class NuevoViajeForm(forms.ModelForm):    
    destinos = forms.CharField(widget=forms.HiddenInput, required = False)
    fecha_salida = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    origen_clave_municipio = forms.CharField(widget=forms.HiddenInput)
    
    class Meta:
        model = Viaje
        fields = [
            'cliente', 
            'departamento', 
            'economico', 
            'operador', 
            'ruta', 
            'tipo_ruta',
            'contiene',
            'referencia',
            'fecha_salida',
            'origen_clave_municipio',            
            'origen_colonia',
            'origen_calle',
            'origen_numero',
            'origen_cp',
            'observaciones',
        ]
        
    def __init__(self, *args, **kwargs):
        super(NuevoViajeForm, self).__init__(*args, **kwargs)
        self.fields['cliente'].widget.attrs['class'] = 'form-control select2'
        self.fields['departamento'].widget.attrs['class'] = 'form-control select2'
        self.fields['economico'].widget.attrs['class'] = 'form-control select2'
        self.fields['operador'].widget.attrs['class'] = 'form-control select2'
        self.fields['ruta'].widget.attrs['class'] = 'form-control select2'
        self.fields['tipo_ruta'].widget.attrs['class'] = 'form-control select2'
        self.fields['contiene'].widget.attrs['class'] = 'form-control'
        self.fields['referencia'].widget.attrs['class'] = 'form-control'       
        self.fields['fecha_salida'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_salida'].widget.attrs['readonly'] = 'readonly'
        self.fields['origen_clave_municipio'].widget.attrs['class'] = 'form-control'        
        self.fields['origen_colonia'].widget.attrs['class'] = 'form-control'
        self.fields['origen_calle'].widget.attrs['class'] = 'form-control'
        self.fields['origen_numero'].widget.attrs['class'] = 'form-control'
        self.fields['origen_cp'].widget.attrs['class'] = 'form-control'  
        self.fields['destinos'].widget.attrs['class'] = 'form-control'
        self.fields['observaciones'].widget.attrs['class'] = 'form-control'   
        
class AutorizarViajeForm(forms.ModelForm):    
    destinos = forms.CharField(widget=forms.HiddenInput)
    fecha_salida = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
    origen_clave_municipio = forms.CharField(widget=forms.HiddenInput)
    status = forms.IntegerField(widget=forms.HiddenInput)
    nota = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Viaje
        fields = [       
            'referencia',
            'economico', 
            'operador', 
            'ruta', 
            'tipo_ruta',
            'contiene',
            'fecha_salida',
            'origen_clave_municipio',            
            'origen_colonia',
            'origen_calle',
            'origen_numero',
            'origen_cp',
            'observaciones',  
        ]
        
    def __init__(self, *args, **kwargs):
        super(AutorizarViajeForm, self).__init__(*args, **kwargs)
        self.fields['referencia'].widget.attrs['class'] = 'form-control'
        self.fields['economico'].widget.attrs['class'] = 'form-control select2'
        self.fields['operador'].widget.attrs['class'] = 'form-control select2'
        self.fields['ruta'].widget.attrs['class'] = 'form-control select2'
        self.fields['tipo_ruta'].widget.attrs['class'] = 'form-control select2'        
        self.fields['contiene'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_salida'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_salida'].widget.attrs['readonly'] = 'readonly'
        self.fields['origen_clave_municipio'].widget.attrs['class'] = 'form-control'        
        self.fields['origen_colonia'].widget.attrs['class'] = 'form-control'
        self.fields['origen_calle'].widget.attrs['class'] = 'form-control'
        self.fields['origen_numero'].widget.attrs['class'] = 'form-control'
        self.fields['origen_cp'].widget.attrs['class'] = 'form-control'  
        self.fields['destinos'].widget.attrs['class'] = 'form-control'   
        self.fields['observaciones'].widget.attrs['class'] = 'form-control' 
        
class EntregadoForm(forms.ModelForm):        
    fecha_entrega = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    comprobante_entrega = forms.FileField(required=False, widget=MetronicFileInput)
    comprobante_entrega_otro = forms.FileField(required=False, widget=MetronicFileInput)
    destino_clave_municipio = forms.CharField(required = False,widget=forms.HiddenInput)
    
    class Meta:
        model = Destino
        fields = [             
           'fecha_entrega',
           'destino_clave_municipio',
           'comprobante_entrega',
           'comprobante_entrega_otro',
        ]
        
    def __init__(self, *args, **kwargs):
        super(EntregadoForm, self).__init__(*args, **kwargs)
        self.fields['destino_clave_municipio'].widget.attrs['class'] = 'form-control destinos'
        self.fields['fecha_entrega'].widget.attrs['class'] = 'form-control'

        #self.fields['fecha_entrega'].widget.attrs['readonly'] = 'readonly'   
        
class ComprobanteForm(forms.ModelForm):
    comprobante_entrega = forms.FileField(required=True, widget=MetronicFileInput)
    comprobante_entrega_otro = forms.FileField(required=False, widget=MetronicFileInput)
    
    class Meta:
        model = Destino
        fields = [             
           'fecha_entrega',
           'destino_clave_municipio',           
           'comprobante_entrega',
           'comprobante_entrega_otro',
        ]                
        
class FacturadoForm(forms.ModelForm): 
    factura = forms.CharField(max_length=150)
    facturacion_forma_pago = forms.CharField(max_length=120)
    facturacion_banco = forms.CharField(max_length=120)
    facturacion_documento = forms.CharField(max_length=120)
    facturacion_flete = forms.DecimalField(max_digits=9, decimal_places=2)    
    status = forms.IntegerField(widget=forms.HiddenInput)
    nota = forms.CharField(widget=forms.HiddenInput(), required=False)
                   
    class Meta:
        model = Viaje
        fields = [             
           'factura',  
           'facturacion_forma_pago',
           'facturacion_banco',
           'facturacion_documento',
           'facturacion_casetas',
           'facturacion_flete',
           'facturacion_maniobra',
           'facturacion_reparto',
           'facturacion_desvio',
           'facturacion_ferri',
           'facturacion_otros',
           'observaciones',      
        ]
        
    def __init__(self, *args, **kwargs):
        super(FacturadoForm, self).__init__(*args, **kwargs)
        self.fields['factura'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_forma_pago'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_banco'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_documento'].widget.attrs['class'] = 'form-control'   
        self.fields['facturacion_casetas'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_flete'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_maniobra'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_reparto'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_desvio'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_ferri'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_otros'].widget.attrs['class'] = 'form-control importe'  
        self.fields['observaciones'].widget.attrs['class'] = 'form-control'   
         

class SalidaForm(forms.ModelForm):
    status = forms.IntegerField(widget=forms.HiddenInput)
    nota = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Viaje
        fields = [
            'observaciones',
            'economico', 
            'operador', 
        ]
    
    def clean(self):
        cleaned_data = super(SalidaForm, self).clean()
        status = forms.IntegerField(widget=forms.HiddenInput, required = False)##cleaned_data.get("status")
        nota = cleaned_data.get("nota")
        if status in [8,9] and not nota :
            self._errors["nota"] = self.error_class(['Para cancelar debe especificar un motivo.'])
            del cleaned_data["nota"]
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super(SalidaForm, self).__init__(*args, **kwargs)
        self.fields['observaciones'].widget.attrs['class'] = 'form-control'        
        self.fields['economico'].widget.attrs['class'] = 'form-control'
        self.fields['operador'].widget.attrs['class'] = 'form-control'
        
class CambioForm(forms.ModelForm):
    status = forms.IntegerField(widget=forms.HiddenInput)
    nota = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Viaje
        fields = [
            'observaciones',
            'referencia',
        ]
    
    def clean(self):
        cleaned_data = super(CambioForm, self).clean()
        status = cleaned_data.get("status")
        nota = cleaned_data.get("nota")
        if status in [8,9] and not nota :
            self._errors["nota"] = self.error_class(['Para cancelar debe especificar un motivo.'])
            del cleaned_data["nota"]
        return cleaned_data
    
    def __init__(self, *args, **kwargs):
        super(CambioForm, self).__init__(*args, **kwargs)
        self.fields['observaciones'].widget.attrs['class'] = 'form-control'
        self.fields['referencia'].widget.attrs['class'] = 'form-control'
        
class RutaForm(forms.ModelForm):          
    class Meta:
        model = Ruta  
        
    def __init__(self, *args, **kwargs):
        super(RutaForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'  
        self.fields['casetas_salida'].widget.attrs['class'] = 'form-control select2'
        self.fields['casetas_regreso'].widget.attrs['class'] = 'form-control select2'
        
class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        
    def __init__(self, *args, **kwargs):
        super(GastoForm, self).__init__(*args, **kwargs)
        self.fields['concepto'].widget.attrs['class'] = 'form-control input-small select2 concepto'  
        self.fields['comentarios'].widget.attrs['class'] = 'form-control input-small'
        self.fields['comentarios'].widget.attrs['rows'] = 1
        self.fields['pagado_operaciones'].widget.attrs['class'] = 'form-control input-small'
        self.fields['pagado_contabilidad'].widget.attrs['class'] = 'form-control input-small'
        
class ComprobanteGastoForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        
class CargaViajeForm(forms.ModelForm):    #### caratula de datos de Editar Gastos.
    id = forms.IntegerField(widget=forms.TextInput)    
    destinos = forms.CharField(widget=forms.HiddenInput, required = False)
    fecha_salida = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required = False)
    origen_clave_municipio = forms.CharField(widget=forms.HiddenInput, required = False)
    factura = forms.CharField(max_length=150, required = False)
    facturacion_flete = forms.DecimalField(max_digits=9, decimal_places=2, required = False)
    facturacion_forma_pago = forms.CharField(max_length=120, required = False)
    facturacion_banco = forms.CharField(max_length=120, required = False)
    facturacion_documento = forms.CharField(max_length=120, required = False)
    facturacion_casetas = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    facturacion_maniobra = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    facturacion_reparto = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    facturacion_desvio = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    facturacion_ferri = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    facturacion_otros = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    observaciones = forms.CharField(max_length = 150, required = False)
    origen_colonia = forms.CharField (max_length = 150, required = False)
    origen_calle = forms.CharField (max_length = 100, required = False)
    origen_numero = forms.CharField (max_length = 100, required = False)
    origen_cp = forms.CharField (max_length = 5, required = False)
    referencia = forms.CharField (max_length = 50, required = False)
    fecha_entmcia = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required= False)
    evidencia = forms.FileField(required = False)
    fecha_ent = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)

    class Meta:
        model = Viaje
        fields = [
                'id',
                'cliente',
                'departamento',
                'economico',
                'operador',
                'ruta',
                'tipo_ruta',
                'contiene',
                'referencia',
                'fecha_salida',
                'origen_clave_municipio',
                'origen_colonia',
                'origen_calle',
                'origen_numero',
                'origen_cp',
                'fecha_entmcia',
                'evidencia',
                'fecha_ent',
        		'observaciones',
#		'facturacion_maniobra',	
        ]
   
        exclude = [
            'flujo'
        ] 
        
    def __init__(self, *args, **kwargs):
        super(CargaViajeForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['class'] = 'form-control'
        self.fields['cliente'].widget.attrs['class'] = 'form-control select2'
        self.fields['departamento'].widget.attrs['class'] = 'form-control select2'
        self.fields['economico'].widget.attrs['class'] = 'form-control select2'
        self.fields['operador'].widget.attrs['class'] = 'form-control select2'
        self.fields['ruta'].widget.attrs['class'] = 'form-control select2'
        self.fields['tipo_ruta'].widget.attrs['class'] = 'form-control select2'
        self.fields['contiene'].widget.attrs['class'] = 'form-control'
        self.fields['referencia'].widget.attrs['class'] = 'form-control'       
        self.fields['fecha_salida'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_salida'].widget.attrs['readonly'] = 'readonly'
        self.fields['origen_clave_municipio'].widget.attrs['class'] = 'form-control'        
        self.fields['origen_colonia'].widget.attrs['class'] = 'form-control'
        self.fields['origen_calle'].widget.attrs['class'] = 'form-control'
        self.fields['origen_numero'].widget.attrs['class'] = 'form-control'
        self.fields['origen_cp'].widget.attrs['class'] = 'form-control'          
        self.fields['observaciones'].widget.attrs['class'] = 'form-control'###
        self.fields['factura'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_forma_pago'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_banco'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_documento'].widget.attrs['class'] = 'form-control'   
        self.fields['facturacion_casetas'].widget.attrs['class'] = 'form-control importe'   
        self.fields['facturacion_flete'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_maniobra'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_reparto'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_desvio'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_ferri'].widget.attrs['class'] = 'form-control importe'
        self.fields['facturacion_otros'].widget.attrs['class'] = 'form-control importe'
        self.fields['fecha_entmcia'].widget.attrs['class']='form-control' 
        self.fields['evidencia'].widget.attrs['class']='form-control' 
        self.fields['fecha_ent'].widget.attrs['class'] = 'form-control'
        self.fields['destinos'].widget.attrs['class'] = 'form-control'  


        
class GastoHistoricoForm(forms.ModelForm):      
    class Meta:
        model = Gasto
        exclude = ('viaje',)
        
    def __init__(self, *args, **kwargs):
        super(GastoHistoricoForm, self).__init__(*args, **kwargs)
        self.fields['concepto'].widget.attrs['class'] = 'form-control input-small select2 concepto'  
        self.fields['comentarios'].widget.attrs['class'] = 'form-control input-small'
        self.fields['comentarios'].widget.attrs['rows'] = 1
        self.fields['pagado_operaciones'].widget.attrs['class'] = 'form-control input-small'
        self.fields['pagado_contabilidad'].widget.attrs['class'] = 'form-control input-small'        
class UploadExcelForm(forms.Form):
    docfile = forms.FileField(
        label='Selecciona un archivo'
        )


class SearchFormFact(forms.Form):
    pk = forms.IntegerField(required=False)
    status = forms.ModelChoiceField(queryset=State.objects.filter(workflow__pk=1),required=False)
    fecha_from = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    fecha_to = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    cliente = forms.ModelChoiceField(queryset=Cliente.objects.filter(activo=True), required=False)
    factura = forms.CharField(max_length = 100, required= False)
    facturacion_flete = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    facturacion_maniobra = forms.DecimalField(max_digits = 9, required = False )
    facturacion_reparto = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    facturacion_desvio = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    facturacion_otros = forms.DecimalField(max_digits = 9, decimal_places = 2, required = False)
    destino = forms.CharField(max_length=150, required=False, widget=forms.HiddenInput)
    referencia = forms.CharField(max_length=20, required=False)
    economico = forms.ModelChoiceField(queryset=Economico.objects.filter(activo=True), required=False)
    operador = forms.ModelChoiceField(queryset=empleado.objects.filter(Q(puesto =8)|Q(puesto =9)|Q(puesto=10)|Q(puesto=11)|Q(puesto=12)), required = False)
    
    def __init__(self, *args, **kwargs):
        super(SearchFormFact, self).__init__(*args, **kwargs)
        self.fields['pk'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['status'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['fecha_from'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['fecha_from'].widget.attrs['placeholder'] = 'Del'
        self.fields['fecha_to'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['fecha_to'].widget.attrs['placeholder'] = 'Al'
        self.fields['cliente'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['factura'].widget.attrs['class']= 'form-control form-filter input-sm'
        self.fields['facturacion_flete'].widget.attrs['class']= 'form-control form-filter input-sm'
        self.fields['facturacion_maniobra'].widget.attrs['class']= 'form-control form-filter input-sm'
        self.fields['facturacion_reparto'].widget.attrs['class']= 'form-control form-filter input-sm'
        self.fields['facturacion_desvio'].widget.attrs['class']= 'form-control form-filter input-sm'
        self.fields['facturacion_otros'].widget.attrs['class']= 'form-control form-filter input-sm'
        self.fields['destino'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['referencia'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['economico'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
        self.fields['operador'].widget.attrs['class'] = 'form-control form-filter input-sm select2'   


#PDF MAsivo
class DocumentoForma(Form):
    id = forms.IntegerField(required=False)
    docfile1 = forms.ModelChoiceField(queryset = CargaPdf.objects.all().filter(activo=True).order_by('id'),required = False)
    docfile = forms.FileField(
        label='Seleccion un archivo PDF'
        )
    def __init__(self, *args, **kwargs):
        super(DocumentoForma, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['docfile'].widget.attrs['class'] = 'form-control form-filter input-sm select2'
class CargaViaje_Edit_GastosForm(forms.ModelForm):    #### caratula de datos de Editar Gastos.
    id = forms.IntegerField(widget=forms.TextInput)    
    fecha_salida = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS)
   # origen_clave_municipio = forms.CharField(widget=forms.HiddenInput)
    #facturacion_flete = forms.DecimalField(max_digits=9, decimal_places=2)
        
    class Meta:
        model = Viaje

    fields = [
        'id',
            'fecha_salida',
        #'fecha_entrega'
            'cliente',
            'departamento',
            'referencia',
            'operador',
            'economico',
            'tipo_ruta',
            'contiene',
            'ruta',
            'economico',		
    ]
   
    exclude = [
            'flujo'
        ] 
        
    def __init__(self, *args, **kwargs):
        super(CargaViaje_Edit_GastosForm, self).__init__(*args, **kwargs)
        self.fields['id'].widget.attrs['class'] = 'form-control'
        self.fields['cliente'].widget.attrs['class'] = 'form-control select2'
        self.fields['departamento'].widget.attrs['class'] = 'form-control select2'
        self.fields['economico'].widget.attrs['class'] = 'form-control select2'
        self.fields['operador'].widget.attrs['class'] = 'form-control select2'
        self.fields['ruta'].widget.attrs['class'] = 'form-control select2'
        self.fields['tipo_ruta'].widget.attrs['class'] = 'form-control select2'
        self.fields['contiene'].widget.attrs['class'] = 'form-control'
        self.fields['referencia'].widget.attrs['class'] = 'form-control'       
        self.fields['fecha_salida'].widget.attrs['class'] = 'form-control'
 #       self.fields['fecha_salida'].widget.attrs['readonly'] = 'readonly'
 #      self.fields['origen_clave_municipio'].widget.attrs['class'] = 'form-control'        
 #       self.fields['origen_colonia'].widget.attrs['class'] = 'form-control'
 #       self.fields['origen_calle'].widget.attrs['class'] = 'form-control'
 #       self.fields['origen_numero'].widget.attrs['class'] = 'form-control'
 #       self.fields['origen_cp'].widget.attrs['class'] = 'form-control'          
 #       self.fields['observaciones'].widget.attrs['class'] = 'form-control'###
 #       self.fields['factura'].widget.attrs['class'] = 'form-control'
 #       self.fields['facturacion_forma_pago'].widget.attrs['class'] = 'form-control'
 #       self.fields['facturacion_banco'].widget.attrs['class'] = 'form-control'
 #       self.fields['facturacion_documento'].widget.attrs['class'] = 'form-control'   
#        self.fields['facturacion_casetas'].widget.attrs['class'] = 'form-control importe'   
 #       self.fields['facturacion_flete'].widget.attrs['class'] = 'form-control importe'
  #      self.fields['facturacion_maniobra'].widget.attrs['class'] = 'form-control importe'
    #    self.fields['facturacion_reparto'].widget.attrs['class'] = 'form-control importe'
   #     self.fields['facturacion_desvio'].widget.attrs['class'] = 'form-control importe'
  #      self.fields['facturacion_ferri'].widget.attrs['class'] = 'form-control importe'
 #       self.fields['facturacion_otros'].widget.attrs['class'] = 'form-control importe'  
        
#

class MensajeCorreoForm(forms.Form):
    destinatario = forms.CharField()
    archivoAdjunto = forms.CharField()
    mensaje = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(MensajeCorreoForm, self).__init__(*args, **kwargs)
        self.fields['destinatario'].widget.attrs['class']='form-control'
        self.fields['destinatario'].widget.attrs['readonly'] = True
        self.fields['archivoAdjunto'].widget.attrs['class']='form-control'
        self.fields['archivoAdjunto'].widget.attrs['readonly'] = True
        self.fields['mensaje'].widget.attrs['class'] = 'form-control'



class reporteForm(forms.Form):
    id_viaje = forms.CharField(required= False)
    concepto = forms.CharField(max_length=100, required= False)
    fecha_ini = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    fecha_fin = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)

    def __init__(self, *args, **kwargs):
        super(reporteForm, self).__init__(*args, **kwargs)
        self.fields['id_viaje'].widget.attrs['class'] = 'form-control'
        self.fields['concepto'].widget.attrs['class'] = 'form-control input-small select2 concepto'
        self.fields['fecha_ini'].widget.attrs['class'] = 'form-control form-filter input-sm '
        self.fields['fecha_ini'].widget.attrs['readonly'] = 'readonly'
        self.fields['fecha_fin'].widget.attrs['class'] = 'form-control form-filter input-sm '
        self.fields['fecha_fin'].widget.attrs['readonly'] = 'readonly'


class movimientoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=200, required=True)
    observaciones= forms.CharField(max_length=200, required=True)
    class Meta:
        model = Movimiento

    def __init__(self, *args, **kwargs):
        super(movimientoForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class']='form-control'
        self.fields['observaciones'].widget.attrs['class']='form-control'


class movunidadForm(forms.ModelForm):

    fechai=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    fechaf=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    usuario=forms.CharField(max_length=200, required = False)
    ts=forms.DateField(required=False)


    class Meta:
        model = MovUnidad

    def __init__(self,*args, **kwargs):
        super(movunidadForm, self).__init__(*args, **kwargs)
        self.fields['tipo'].widget.attrs['class']='form-control'
        self.fields['obs'].widget.attrs['class']='form-control'
        self.fields['fechai'].widget.attrs['class']='form-control'
        self.fields['fechaf'].widget.attrs['class']='form-control'
        self.fields['operador'].widget.attrs['class']='form-control'
        self.fields['unidad'].widget.attrs['class']='form-contorl'
        self.fields['estatus'].widget.attrs['class']='form-control'

class repUnidad(forms.ModelForm):

    usuario=forms.CharField(max_length=100, required=False)
    status=forms.IntegerField(required=False)
    motivo = forms.CharField(max_length=100, required=False)
    fecha_AR=forms.DateField(required=False)
    status2=forms.IntegerField(required=False)
    fecha_rev=forms.DateField(required=False)
    obsrevision=forms.CharField(max_length=255, required=False)
    urevision=forms.CharField(max_length=100, required=False)

    class Meta:
        model = ReporteUnidad

    def __init__(self,*args, **kwargs):
        super(repUnidad, self).__init__(*args, **kwargs)
        self.fields['usuario'].widget.attrs['class']='form-control'
        self.fields['reporta'].widget.attrs['class']='form-control'
        self.fields['dano'].widget.attrs['class']='form-control'
        self.fields['imagen1'].widget.attrs['class']='form-control'
        self.fields['imagen2'].widget.attrs['class']='form-control'
        self.fields['imagen3'].widget.attrs['class']='form-control'
        self.fields['imagen4'].widget.attrs['class']='form-control'        
        self.fields['obs'].widget.attrs['class']='form-control'
        self.fields['status'].widget.attrs['class']='form-control'
        self.fields['motivo'].widget.attrs['class']='form-contorl'
        self.fields['fecha_AR'].widget.attrs['class']='form-control'
        self.fields['status2'].widget.attrs['class']='form-contorl'

class UploadForm(forms.ModelForm):    
    
    class Meta:
        model = ReporteUnidad
        fields = [
                    'imagen1',
                    'imagen2',
                    'imagen3',
                    'imagen4',
                ]

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['imagen1'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen2'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen3'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen4'].widget.attrs['class'] = 'btn btn-info'

class libviajeForm(forms.Form):
    pk = forms.IntegerField(required=True)

    class Meta:
        model = Viaje
        fields=[
                'pk',
                ]

    def __init__(self, *args, **kwargs):
        super(libviajeForm, self).__init__(*args, **kwargs)
        self.fields['pk'].widget.attrs['class'] = 'form-control'
        
class repIncidenteForm(forms.Form):

    fecha_ini = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    fecha_fin = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)

    def __init__(self, *args, **kwargs):
        super(repIncidenteForm, self).__init__(*args, **kwargs)
        self.fields['fecha_ini'].widget.attrs['class'] = 'form-control form-filter input-sm '
        self.fields['fecha_ini'].widget.attrs['readonly'] = 'readonly'
        self.fields['fecha_fin'].widget.attrs['class'] = 'form-control form-filter input-sm '
        self.fields['fecha_fin'].widget.attrs['readonly'] = 'readonly'


class editarMovForm(forms.ModelForm):

    class Meta:
        model= ReporteUnidad
        fields=[
                'motivo',
                'status2',
            ]

    def __init__(self, *args, **kwargs):
        super(editarMovForm, self).__init__(*args, **kwargs)
        self.fields['motivo'].widget.attrs['class']='form-control'
        self.fields['status2'].widget.attrs['class']='form-control'

class revisarMovForm(forms.ModelForm):
    class Meta:
        model=ReporteUnidad
        fields=[
                'obsrevision',
        ]
    def __init__(self, *args, **kwargs):
        super(revisarMovForm, self).__init__(*args, **kwargs)
        self.fields['obsrevision'].widget.attrs['class']='form-control'

class archivosForm(forms.ModelForm):
    class Meta:
        model= Archivos
        fields=[
            'desc',
            ]

    def __init__(self, *args, **kwargs):
        super(archivosForm, self).__init__(*args, **kwargs)
        self.fields['desc'].widget.attrs['class']='form-control'

class UploadFilesForm(forms.ModelForm):    
    
    class Meta:
        model = Archivos
        fields = [
                    'archivo',
                ]

    def __init__(self, *args, **kwargs):
        super(UploadFilesForm, self).__init__(*args, **kwargs)
        self.fields['archivo'].widget.attrs['class'] = 'btn btn-info'

class SolicitudesViajeForm(forms.ModelForm):

    fecha_salida = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=False)
    class Meta:
        model = SolicitudesViaje
        fields = [
            'cliente',
            'departamento',
            'economico',
            'operador',
            'ruta',
            'tipo_ruta',
            'contiene',
            'referencia',
            'fecha_salida',
            'origen_clave_municipio',
            'origen_colonia',
            'origen_calle',
            'origen_numero',
            'origen_cp',
            'observaciones',
            'estatus',
        ]

    def __init__(self, *args, **kwargs):
        super(SolicitudesViajeForm, self).__init__(*args, **kwargs)
        #self.fields['fecha_salida'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['cliente'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['departamento'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['economico'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['operador'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['ruta'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['tipo_ruta'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['contiene'].widget.attrs['class']='form-control'
        self.fields['referencia'].widget.attrs['class']='form-control'
        self.fields['fecha_salida'].widget.attrs['class'] = 'form-control'
        self.fields['fecha_salida'].widget.attrs['readonly'] = 'readonly'
        self.fields['origen_clave_municipio'].widget.attrs['class']='form-control'
        self.fields['origen_colonia'].widget.attrs['class']='form-control'
        self.fields['origen_calle'].widget.attrs['class']='form-control'
        self.fields['origen_numero'].widget.attrs['class']='form-control'
        self.fields['origen_cp'].widget.attrs['class']='form-control'
        self.fields['observaciones'].widget.attrs['class']='form-control'
        self.fields['estatus'].widget.attrs['class']='form-control form-filter input-sm select2'


class prefacturasFileForm(forms.ModelForm):

    class Meta:
        model= ArchivoPrefacturas

class prefacturasForm(forms.ModelForm):

    class Meta:
        model= Prefacturas
