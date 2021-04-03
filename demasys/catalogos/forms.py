# coding: utf-8
from django import forms
from django.db.models import Q

from models import Economico, ModeloEconomico, Operador,ExcelViaje,Imagen, Aseguradoras, Archivos
from catalogos.models import Caseta, ConceptoFacturacion, GastoViaje, Documentos
from models import MARCAS
from models import movimientosUnidad
from transportes import settings 
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
    (u'215 / 70 R16',u'215 / 70 R16'),
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
    ('0 KG', '0KG'),
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




class ModeloEconomicoForm(forms.ModelForm):

    capacidad_volumen = forms.DecimalField (max_digits = 7, decimal_places = 2, required = False)
    capacidad_kilos = forms.DecimalField(max_digits = 7, decimal_places = 2, required = False)	    

    class Meta:
        model = ModeloEconomico
        fields = [
		'modelo',
		'capacidad',
		'capacidad_kilos',
		'capacidad_volumen',
		'largo',
		'ancho',
		'alto',		
		]

    def __init__(self, *args, **kwargs):
        super(ModeloEconomicoForm, self).__init__(*args, **kwargs)
        self.fields['modelo'].widget.attrs['class'] = 'form-control'
        self.fields['capacidad'].widget.attrs['class'] = 'form-control'        
        self.fields['capacidad_kilos'].widget.attrs['class'] = 'form-control'     	       
        self.fields['capacidad_volumen'].widget.attrs['class'] = 'form-control'    
        self.fields['largo'].widget.attrs['class'] = 'form-control'    
        self.fields['ancho'].widget.attrs['class'] = 'form-control'    
        self.fields['alto'].widget.attrs['class'] = 'form-control'    

class EconomicoForm(forms.ModelForm):
	
    color =  forms.ChoiceField(choices = COLORES_CHOICES, required = False)
    modelo = forms.ModelChoiceField(queryset = ModeloEconomico.objects.all(), required = False)
    placas = forms.CharField (max_length = 10, required = False) 
    pasa_como = forms.ChoiceField(choices = PASA_CASETA, required = False)
    marca = forms.ChoiceField (choices = MARCAS, required = False)
    submarca = forms.ChoiceField (choices = SUBMARCAS, required = False)
    tipoPlaca = forms.ChoiceField (choices = TIPO_PLACAS, required = False)
    caja = forms.ChoiceField (choices = TIPO_CAJA, required = False )
    medidasllantas = forms.ChoiceField (choices = MEDIDAS, required = False)
    tipollantas = forms.ChoiceField (choices = TIPO_LLANTAS, required = False)
    carga = forms.ChoiceField (choices = CARGAS, required = False )
    aseguradora = forms.ModelChoiceField(queryset = Aseguradoras.objects.all(), required = False)
    poliza = forms.CharField (max_length = 20, required = False)
    fecha_vencimiento = forms.DateField (required = False)
    iave = forms.CharField (max_length = 30, required = False)
    cerradura = forms.BooleanField(required = False)
    operador = forms.ModelChoiceField(queryset = Operador.objects.all(),required = False)
    ultimoKilometraje = forms.IntegerField (required = False) 
    kilometrajeServicio = forms.IntegerField (required = False)
    activo = forms.BooleanField (required = False)
    combustible = forms.ChoiceField (choices = COMBUSTIBLE, required = False )
    cilindros = forms.ChoiceField (choices = CILINDROS, required = False)
    psi = forms.IntegerField (required = False)
    filtro = forms.CharField (max_length = 20, required = False)
    tipo_aceite = forms.CharField (max_length = 20, required = False)
    litros = forms.DecimalField (max_digits = 2, decimal_places = 0, required = False)
    rendimiento = forms.DecimalField (max_digits = 6, decimal_places = 2, required = False)
    antijamer = forms.NullBooleanField(required = False)
    fecha_antijamer = forms.DateField (required = False)
    boton_panico = forms.NullBooleanField (required = False)
    camara_int = forms.NullBooleanField (required = False)
    camara_ext = forms.NullBooleanField (required = False )
    lugar_camara_int = forms.CharField (max_length =30, required = False)
    lugar_camara_ext = forms.CharField (max_length = 30, required = False)
    clave = forms.CharField (max_length= 4, required = True)
    ns = forms.CharField (max_length = 20, required = False)
    anio = forms.CharField (max_length = 4, required = False)
    filtro_aceite = forms.CharField(max_length = 20, required = False)
    filtro_aire = forms.CharField(max_length = 20, required = False)
    filtro_gas = forms.CharField(max_length = 20, required = False)
    filtro_airea = forms.CharField(max_length = 20, required = False)

    class Meta:

        model = Economico
	fields = [
		'color',
		'modelo',
		'placas',
		'pasa_como',
		'marca',
		'submarca',
		'tipoPlaca',
		'caja',
		'medidallantas',
		'tipollantas',
		'carga',
		'aseguradora',
		'poliza',
		'fecha_vencimiento',
		'iave',
		'cerradura',
		'operador',
		'ultimoKilometraje',
		'kilometrajeServicio',
		'activo',
		'combustible',
		'cilindros',
		'psi',
		'filtro',
		'tipo_aceite',
		'litros',
		'rendimiento',
		'antijamer',
		'fecha_antijamer',
		'boton_panico',
		'camara_int',
		'camara_ext',
		'lugar_camara_int',
		'lugar_camara_ext',
                'clave',
                'ns',
                'anio',
		'filtro_aceite',
		'filtro_aire',
		'filtro_gas',
		'filtro_airea',
]


    def __init__(self, *args, **kwargs):
        super(EconomicoForm, self).__init__(*args, **kwargs)
#	self.fields['id'].widget.atts['class'] = 'forms-control'
        self.fields['color'].widget.attrs['class'] = 'form-control' ##7
        self.fields['modelo'].widget.attrs['class'] = 'form-control' ##4
        self.fields['placas'].widget.attrs['class'] = 'form-control' ## 8
        self.fields['pasa_como'].widget.attrs['class'] = 'form-control'##9
        self.fields['marca'].widget.attrs['class'] = 'form-control' ##ok 2
        self.fields['submarca'].widget.attrs['class'] = 'form-control'  ##ok 3
        self.fields['tipoPlaca'].widget.attrs['class'] = 'form-control' ##11
        self.fields['caja'].widget.attrs['class'] = 'form-control'  ##12
        self.fields['medidallantas'].widget.attrs['class'] = 'form-control' ##18
        self.fields['tipollantas'].widget.attrs['class'] = 'form-control' ## 19
        self.fields['carga'].widget.attrs['class'] = 'form-control' ##13
        self.fields['aseguradora'].widget.attrs['class'] = 'form-control' ##21
        self.fields['poliza'].widget.attrs['class'] = 'form-control'  ##22
        self.fields['fecha_vencimiento'].widget.attrs['class'] = 'form-control'  ##23
        self.fields['iave'].widget.attrs['class'] = 'form-control' ##10
        self.fields['cerradura'].widget.attrs['class'] = 'form-control' ##28
        self.fields['operador'].widget.attrs['class'] = 'form-control'  ##ok 1
        #self.fields['cctv'].widget.attrs['class'] = 'form-control'
        self.fields['ultimoKilometraje'].widget.attrs['class'] = 'form-control'##32
        self.fields['kilometrajeServicio'].widget.attrs['class'] = 'form-control'##33
        #self.fields['saldo'].widget.attrs['class'] = 'form-control'
        #self.fields['saldo_observaciones'].widget.attrs['class'] = 'form-control'
        self.fields['activo'].widget.attrs['class'] = 'form-control' ##34
	self.fields['combustible'].widget.attrs['class'] = 'form-control'  ## 5
	self.fields['cilindros'].widget.attrs['class'] = 'form-control'##6
	self.fields['psi'].widget.attrs['class'] = 'form-control' ##20
	self.fields['filtro'].widget.attrs['class'] = 'form-control' ##14
	self.fields['tipo_aceite'].widget.attrs['class'] = 'form-control' ##15
	self.fields['litros'].widget.attrs['class'] = 'form-control'  ## 16
	self.fields['rendimiento'].widget.attrs['class'] = 'form-control' #17
	self.fields['antijamer'].widget.attrs['class'] = 'form-control' ##29
	self.fields['fecha_antijamer'].widget.attrs['class'] = 'form-control'  ##30
	self.fields['boton_panico'].widget.attrs['class'] = 'form-control' ##31
	self.fields['camara_int'].widget.attrs['class'] = 'form-control' ##24
	self.fields['camara_ext'].widget.attrs['class'] = 'form-control' ##26
	self.fields['lugar_camara_int'].widget.attrs['class'] = 'form-control'  ##25
	self.fields['lugar_camara_ext'].widget.attrs['class'] = 'form-control' ##27
        self.fields['clave'].widget.attrs['class']='form-control'
        self.fields['ns'].widget.attrs['class']='form-control'
        self.fields['anio'].widget.attrs['class']='form-control'
        self.fields['filtro_aceite'].widget.attrs['class'] = 'form-control'
        self.fields['filtro_aire'].widget.attrs['class'] = 'form-control'
	self.fields['filtro_gas'].widget.attrs['class'] = 'form-control'
	self.fields['filtro_airea'].widget.attrs['class'] = 'form-control'



class OperadorForm(forms.ModelForm):    
    class Meta:
        model = Operador      
        
    def __init__(self, *args, **kwargs):
        super(OperadorForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['apellido_paterno'].widget.attrs['class'] = 'form-control'
        self.fields['apellido_materno'].widget.attrs['class'] = 'form-control'
        self.fields['telefono'].widget.attrs['class'] = 'form-control'    
        self.fields['saldo'].widget.attrs['class'] = 'form-control'
        self.fields['saldo_observaciones'].widget.attrs['class'] = 'form-control'                              
        
class CasetaForm(forms.ModelForm):    
    class Meta:
        model = Caseta      
        
    def __init__(self, *args, **kwargs):
        super(CasetaForm, self).__init__(*args, **kwargs)
        self.fields['via'].widget.attrs['class'] = 'form-control'        
        self.fields['autos'].widget.attrs['class'] = 'form-control'
        self.fields['autobus_2_ejes'].widget.attrs['class'] = 'form-control'     

class GastoViajeForm(forms.ModelForm):    
    class Meta:
        model = GastoViaje    
        
    def __init__(self, *args, **kwargs):
        super(GastoViajeForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        
class ConceptoFacturacionForm(forms.ModelForm):    
    class Meta:
        model = ConceptoFacturacion      
        
    def __init__(self, *args, **kwargs):
        super(ConceptoFacturacionForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'        
        
class UploadEconomicoForm(forms.Form):
    docfile = forms.FileField(
        label='Selecciona un archivo'
        )

class UploadExcelForm(forms.Form):
    class Meta:
        model = ExcelViaje      
        
    def __init__(self, *args, **kwargs):
        super(UploadExcelForm, self).__init__(*args, **kwargs)


####################################################################
class UploadForm(forms.ModelForm):    
    class Meta:
        model = Imagen        
    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['imagen1'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen2'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen3'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen4'].widget.attrs['class'] = 'btn btn-info'
        

class AseguradoraForm(forms.ModelForm):
    class Meta:
        model = Aseguradoras

    def __init__(self, *args, **kwargs):
        super(AseguradoraForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['direccion'].widget.attrs['class'] = 'form-control'
        self.fields['telefono_siniestros'].widget.attrs['class'] = 'form-control'    

class ArchivosForm(forms.ModelForm):

	class Meta:
		model = Archivos

class movUnidadForm(forms.ModelForm):

    operador = forms.ModelChoiceField(queryset=empleado.objects.filter(Q(puesto =8)|Q(puesto =9)|Q(puesto=10)|Q(puesto=11)|Q(puesto=12)), required = False)
    kmen = forms.IntegerField (required = False)
    kmsa = forms.IntegerField (required = False)
    fecha = forms.DateField (input_formats=settings.DATE_INPUT_FORMATS,required = False)
    tiemporep=forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required=False)
    alternativa=forms.CharField(max_length=250, required=False)


    class Meta:
         model = movimientosUnidad
         fields = [
                'unidad',
                'fecha',
                'tipo',
                'obs',
                'operador',
                'kmen',
                'kmsa',
                'tiemporep',
                'alternativa',
                  ]



    def __init__(self, *args, **kwargs):
        super (movUnidadForm, self).__init__(*args, **kwargs)
        self.fields['unidad'].widget.attrs['class']='form-control'
        self.fields['fecha'].widget.attrs['class']='form-control'
        self.fields['tipo'].widget.attrs['class']='form-control'
        self.fields['obs'].widget.attrs['class']='form-control'
        self.fields['operador'].widget.attrs['class']='form-control'
        self.fields['kmen'].widget.attrs['class']='form-control'
        self.fields['kmsa'].widget.attrs['class']='form-control'
        self.fields['tiemporep'].widget.attrs['class']='form-control'
        self.fields['alternativa'].widget.attrs['class']='form-control'


### Documentos de las unidades

class SearchDocsForm (forms.Form):
      class Meta:
          model = Documentos
      def __init__(self, *arg, **kwargs):
            super (SearchDocsForm, self).__init__(*arg, **kwargs)

class documentosForm(forms.ModelForm):
	class Meta:
            model = Documentos
            fields = [
                    'nombreDoc',
                    'descripcion',
                     ]

	def __init__(self, *arg, **kwargs):
            super (documentosForm, self).__init__(*arg, **kwargs)
            self.fields['nombreDoc'].widget.attrs['class']='form-control'
            self.fields['descripcion'].widget.attrs['class']='form-control'



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



