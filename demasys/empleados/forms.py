# coding: utf-8
from django import forms
#from catalogos.models import Operador, Economico
#from cuentas.models import Perfil
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
#from viajes.models import Ruta, Viaje, Destino
#from transportes import settings 
from empleados.models import *

#from contable.models import Partidas, Area
#from inventario.models import Productos
from django.core.validators import MinValueValidator
from decimal import Decimal
from transportes import settings

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

STATUS = (
    (1,'Activo'),
    (2,'Inactivo'),
    (3,'Suspendido'),
    (4,'Otro'),
)

CATEGORIAS = (
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
    (5, 'Otra')
)

PARENTESCOS = (
    (1,u'Padre'),
    (2,u'Madre'),
    (3,u'Esposa(o)'),
    (4,u'Hermano (a)'),
    (5,'Pareja'),
    (6,u'Hijo (a)'),
    (7,'Conocido'),
    (8,'Otro Familiar'),
)


HIJOS = (
    (0, '0'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10'),
)

class SearchForm(forms.Form): ###index

    pk = forms.IntegerField(required = False)
    nombre = forms.CharField (max_length = 60, required= False)
    apellidop = forms.CharField (max_length = 50, required= False)
    apellidom = forms.CharField (max_length = 50, required= False)
    sexo = forms.MultipleChoiceField (choices = SEXO, required = False)
    estadocivil = forms.MultipleChoiceField(choices = CIVIL, required=False)
    hijos = forms.IntegerField (required= False)
    tipo_lic = forms.MultipleChoiceField(choices = TIPO_LIC,required = False)
    escolaridad = forms.MultipleChoiceField(choices = CAT_ESCOLARIDAD, required = False)


    def __init__ (self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields['pk'].widget.attrs['class']='form-control form-fiter input-sm'
        self.fields['nombre'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['apellidop'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['apellidom'].widget.attrs['class']='form-control form-filter input-sm'
        self.fields['sexo'].widget.attrs['class']='form-control forms-filter input-sm'
        self.fields['estadocivil'].widget.attrs['class']='form-control form-filter input-sm select2 '
        self.fields['hijos'].widget.attrs['class']='form-control form-filter input-sm'
        self.fields['tipo_lic'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['escolaridad'].widget.attrs['class']='form-control form-filter input-sm select2-container'

class empleadoForm (forms.ModelForm):  ###Agregar

    nombre = forms.CharField(max_length = 50, required = True)
    segundo_nombre = forms.CharField(max_length = 50, required = False)
    apellidop = forms.CharField(max_length = 50, required = True)
    apellidom = forms.CharField(max_length = 50, required = True)
    edad = forms.DecimalField (max_digits = 2, decimal_places = 0, required = True)
    fecha_civil = forms.DateField(required = False)
    #hijos = forms.IntegerField (choices = HIJOS, required = False)
    lugar_nacimiento = forms.CharField(max_length = 50, required = True)
    contacto_emergencia_nom = forms.CharField(max_length = 50, required = True)
    contacto_emergencia_tel = forms.CharField(max_length = 50, required = True)
    contacto_emergencia_cel = forms.CharField(max_length = 50, required = True)
    nss = forms.CharField (max_length = 12, required = False)
    ife = forms.DecimalField (max_digits = 16, decimal_places = 0, required = False)
    licencia = forms.CharField (max_length = 20, required = False)
    RFC = forms.CharField (max_length = 15, required = False)
    CURP = forms.CharField (max_length= 18, required = False)
    No_ActaNac= forms.CharField(max_length = 30, required = False)
    Cartilla = forms.CharField (max_length = 20, required = False)
    primaria = forms.CharField(max_length = 100, required = False)
    cer_primaria = forms.CharField(max_length = 30, required = False)
    secundaria = forms.CharField(max_length = 100, required = False)
    cer_secundaria = forms.CharField(max_length = 30, required = False)
    preparatoria = forms.CharField(max_length = 100, required = False)
    cer_preparatoria = forms.CharField(max_length = 30, required = False)
    universidad = forms.CharField(max_length = 100, required = False)
    cer_universidad = forms.CharField(max_length = 30, required = False)
    curso1 = forms.CharField(max_length = 100, required = False)
    nombre_curso1 = forms.CharField(max_length = 30, required = False)
    curso2 = forms.CharField(max_length = 100, required = False)
    nombre_curso2 = forms.CharField(max_length = 30, required = False)
    curso3 = forms.CharField(max_length = 100, required = False)
    nombre_curso3 = forms.CharField(max_length = 30, required = False)
    registro = forms.CharField(max_length = 20, required = False)
    vigencia = forms.CharField(max_length = 20, required = False)
    ingreso = forms.DateField(required = True)
    puesto = forms.ModelChoiceField(queryset = Puestos.objects.all(), required = False)
    lic_vigencia = forms.DateField(required = False)
    lic_fecha_ref= forms.DateField(required = False)
    clave = forms.CharField(max_length = 4, required = True)
    fecha_nac = forms.DateField(required = True)
    fecha_cer_opalo = forms.DateField(required = False)
    fecha_cer_rc = forms.DateField(required = False)
    folio_opalo = forms.CharField (max_length = 30, required = False)
    folio_rc = forms.CharField (max_length = 30, required = False)
    calle = forms.CharField(max_length = 30, required = False)
    exterior = forms.CharField(max_length = 10, required = False)
    interior = forms.CharField(max_length = 10, required = False)
    colonia = forms.CharField(max_length = 30, required = False)
    estado = forms.CharField(max_length = 30, required = False)
    cp = forms.CharField(max_length = 20, required = False)
    tel_casa = forms.CharField(max_length = 14, required = False)
    tel_asig = forms.CharField (max_length = 14, required = False)
    religion = forms.CharField (max_length = 20, required = False)
    cuenta = forms.CharField (max_length = 20, required = False)
    banco = forms.CharField (max_length = 20, required = False)
        


    class Meta:
        model = empleado
        fields = [
            'nombre',
            'segundo_nombre',
            'apellidop',
            'apellidom',
            'sexo',
            'edad',
            'nacion',
            'estadocivil',
            'fecha_civil',
            'hijos',
            'lugar_nacimiento',
            'contacto_emergencia_nom',
            'contacto_emergencia_tel',
            'contacto_emergencia_cel',
            'nss',
            'ife',
            'licencia',
            'tipo_lic',
            'RFC',
            'CURP',
            'No_ActaNac',
            'escolaridad',
            'Cartilla',
            'primaria',
            'cer_primaria',
            'secundaria',
            'cer_secundaria',
            'preparatoria',
            'cer_preparatoria',
            'universidad',
            'cer_universidad',
            'curso1',
            'nombre_curso1',
            'curso2',
            'nombre_curso2',
            'curso3',
            'nombre_curso3',
            #'status',
            'registro',
            'vigencia',
            'ingreso',
            'puesto',
                        'lic_vigencia',
            'clave',
            'fecha_nac',
            'categoria',
            'lic_fecha_ref',
            'parentesco',
            'cer_opalo',
            'fecha_cer_opalo',
            'cer_rc',
            'fecha_cer_rc',
            'folio_opalo',
            'folio_rc',
            'calle',
            'exterior',
            'interior',
            'colonia',
            'estado',
            'cp',
            'tel_casa',
            'tel_asig',
            'religion',
            'cuenta',
            'banco',
        ]

    def __init__(self, *args, **kwargs):
        super (empleadoForm,self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class']='form-control'
        self.fields['segundo_nombre'].widget.attrs['class']='form-control'
        self.fields['apellidop'].widget.attrs['class']='form-control'
        self.fields['apellidom'].widget.attrs['class']='form-control'
        self.fields['sexo'].widget.attrs['class']='form-control'
        self.fields['edad'].widget.attrs['class']='form-control'
        self.fields['nacion'].widget.attrs['class']='form-control'
        self.fields['estadocivil'].widget.attrs['class']='form-control'
        self.fields['fecha_civil'].widget.attrs['class']='form-control'
        self.fields['hijos'].widget.attrs['class']='form-control'
        self.fields['lugar_nacimiento'].widget.attrs['class']='form-control'
        self.fields['contacto_emergencia_nom'].widget.attrs['class']='form-control'
        self.fields['contacto_emergencia_tel'].widget.attrs['class']='form-control'
        self.fields['contacto_emergencia_cel'].widget.attrs['class']='form-control'
        self.fields['nss'].widget.attrs['class']='form-control'
        self.fields['ife'].widget.attrs['class']='form-control'
        self.fields['licencia'].widget.attrs['class']='form-control'
        self.fields['tipo_lic'].widget.attrs['class']='form-control'
        self.fields['RFC'].widget.attrs['class']='form-control'
        self.fields['CURP'].widget.attrs['class']='form-control'
        self.fields['No_ActaNac'].widget.attrs['class']='form-control'
        self.fields['escolaridad'].widget.attrs['class']='form-control'
        self.fields['Cartilla'].widget.attrs['class']='form-control'
        self.fields['primaria'].widget.attrs['class']='form-control'
        self.fields['cer_primaria'].widget.attrs['class']='form-control'
        self.fields['secundaria'].widget.attrs['class']='form-control'
        self.fields['cer_secundaria'].widget.attrs['class']='form-control'
        self.fields['preparatoria'].widget.attrs['class']='form-control'
        self.fields['cer_preparatoria'].widget.attrs['class']='form-control'
        self.fields['universidad'].widget.attrs['class']='form-control'
        self.fields['cer_universidad'].widget.attrs['class']='form-control'
        self.fields['curso1'].widget.attrs['class']='form-control'
        self.fields['nombre_curso1'].widget.attrs['class']='form-control'
        self.fields['curso2'].widget.attrs['class']='form-control'
        self.fields['nombre_curso2'].widget.attrs['class']='form-control'
        self.fields['curso3'].widget.attrs['class']='form-control'
        self.fields['nombre_curso3'].widget.attrs['class']='form-control'
        #self.fields['status'].widget.attrs['class']='form-control'
        self.fields['registro'].widget.attrs['class']='form-control'
        self.fields['vigencia'].widget.attrs['class']='form-control'
        self.fields['ingreso'].widget.attrs['class']='form-control'
        self.fields['puesto'].widget.attrs['class']='form-control'
        self.fields['lic_vigencia'].widget.attrs['class']='form-control'
        self.fields['clave'].widget.attrs['class']='form-control'
        self.fields['fecha_nac'].widget.attrs['class']='form-control'
        self.fields['categoria'].widget.attrs['class']='form-control'
        self.fields['lic_fecha_ref'].widget.attrs['class']='form-control'
        self.fields['parentesco'].widget.attrs['class']='form-control'
        self.fields['cer_opalo'].widget.attrs['class']='form-control'
        self.fields['fecha_cer_opalo'].widget.attrs['class']='form-control'
        self.fields['folio_opalo'].widget.attrs['class']='form-control'
        self.fields['cer_rc'].widget.attrs['class']='form-control'
        self.fields['fecha_cer_rc'].widget.attrs['class']='form-control'
        self.fields['folio_rc'].widget.attrs['class']='form-control'
        self.fields['calle'].widget.attrs['class']='form-control'
        self.fields['exterior'].widget.attrs['class']='form-control'
        self.fields['interior'].widget.attrs['class']='form-control'
        self.fields['colonia'].widget.attrs['class']='form-control'
        self.fields['estado'].widget.attrs['class']='form-control'
        self.fields['cp'].widget.attrs['class']='form-control'
        self.fields['tel_casa'].widget.attrs['class']='form-control'
        self.fields['tel_asig'].widget.attrs['class']='form-control'
        self.fields['religion'].widget.attrs['class']='form-control'
        self.fields['cuenta'].widget.attrs['class']='form-control'
        self.fields['banco'].widget.attrs['class']='form-control'


##SOLICITUD EMPLEO

class empleadoSolicitudForm (forms.ModelForm):  ###Agregar

    nombreCompleto = forms.CharField(max_length = 150, required = True)
    fechaSol = forms.DateField(required = False)
    puestoSol = forms.CharField(max_length = 50, required = True)
    sueldo = forms.DecimalField(max_digits=7, decimal_places=2)
    edad = forms.IntegerField()
    domicilio = forms.CharField(max_length = 100, required = True)
    colonia = forms.CharField(max_length = 100, required = True)
    cp = forms.IntegerField(required = True)
    telefono = forms.CharField(max_length = 15, required = True)
    celular = forms.CharField(max_length = 15, required = True)
    lugarNacimiento = forms.CharField(max_length = 100, required = True)
    fechaNacimiento = forms.DateField(required = False)
    #estatura = forms.DecimalField (max_digits = 4, decimal_places = 2, required = True)
    # peso = forms.DecimalField (max_digits = 4, decimal_places = 2, required = True)
    email = forms.CharField(max_length = 50, required = True)



    class Meta:
        model = Datos
        fields = (
            'nombreCompleto',
            'fechaSol',
            'puestoSol',
            'sueldo',
            'edad',
            'domicilio',
            'colonia',
            'cp',
            'telefono',
            'celular',
            'lugarNacimiento',
            'fechaNacimiento',
            'nacionalidad',
            'viveCon',
            'dependientes',
            #'estatura',
            #'peso',
            'sexo',
            'email',
            'estadoCivil',
        )


    def __init__(self, *args, **kwargs):


        super (empleadoSolicitudForm,self).__init__(*args, **kwargs)
        self.fields['nombreCompleto'].widget.attrs['class']='form-control'
        self.fields['fechaSol'].widget.attrs['class']='form-control'
        self.fields['puestoSol'].widget.attrs['class']='form-control'
        self.fields['sueldo'].widget.attrs['class']='form-control'
        self.fields['sueldo'].localize=True
        #self.fields['sueldo'].widget.attrs['forms']='NumberInput'
        self.fields['edad'].widget.attrs['class']='form-control'
        self.fields['edad'].widget.attrs['size']=2
        self.fields['domicilio'].widget.attrs['class']='form-control'
        self.fields['colonia'].widget.attrs['class']='form-control'
        self.fields['cp'].widget.attrs['class']='form-control'
        self.fields['telefono'].widget.attrs['class']='form-control'
        self.fields['celular'].widget.attrs['class']='form-control'
        self.fields['lugarNacimiento'].widget.attrs['class']='form-control'
        self.fields['fechaNacimiento'].widget.attrs['class']='form-control'
        self.fields['nacionalidad'].widget.attrs['class']='form-control'
        self.fields['viveCon'].widget.attrs['class']='form-control'
        self.fields['dependientes'].widget.attrs['class']='form-control'
        #self.fields['estatura'].widget.attrs['class']='form-control'
        #self.fields['peso'].widget.attrs['class']='form-control'
        self.fields['sexo'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['estadoCivil'].widget.attrs['class']='form-control'


######DOCUMENTACION

class DocumentacionForm (forms.ModelForm):  ###Agregar

    rfc = forms.CharField(max_length = 15, required = True)
    nss = forms.CharField(max_length = 20, required = True)
    numCartilla = forms.CharField(max_length = 20, required = True)
    pasaporte = forms.CharField(max_length = 20, required = True)
    numLicencia = forms.CharField(max_length = 20, required = True)
    curp = forms.CharField(max_length = 20, required = True)



    class Meta:
        model = Documentacion
        fields = [
            'idsolicitante',
            'rfc',
            'nss',
            'numCartilla',
            'pasaporte',
            'tieneLicencia',
            'tipoLicencia',
            'numLicencia',
            'curp',
            'afore',
        ]

    def __init__(self, *args, **kwargs):
        super (DocumentacionForm,self).__init__(*args, **kwargs)
        self.fields['rfc'].widget.attrs['class']='form-control'
        self.fields['nss'].widget.attrs['class']='form-control'
        self.fields['numCartilla'].widget.attrs['class']='form-control'
        self.fields['pasaporte'].widget.attrs['class']='form-control'
        self.fields['tieneLicencia'].widget.attrs['class']='form-control'
        self.fields['tipoLicencia'].widget.attrs['class']='form-control'
        self.fields['numLicencia'].widget.attrs['class']='form-control'
        self.fields['curp'].widget.attrs['class']='form-control'
        self.fields['afore'].widget.attrs['class']='form-control'

#### SALUD HABITOS PERSONALES


class SalhabForm (forms.ModelForm):  ###Agregar

    descripcion = forms.CharField(max_length = 60, required = True)
    hobbie = forms.CharField(max_length = 60, required = True)
    meta = forms.CharField(max_length = 60, required = True)


    class Meta:
        model = Salhab
        fields = [
            'idsolicitante',
            'salud',
            'cronico',
            'descripcion',
            'deporte',
            'club',
            'hobbie',
            'meta',
        ]

    def __init__(self, *args, **kwargs):
        super (SalhabForm,self).__init__(*args, **kwargs)
        self.fields['salud'].widget.attrs['class']='form-control'
        self.fields['cronico'].widget.attrs['class']='form-control'
        self.fields['descripcion'].widget.attrs['class']='form-control'
        self.fields['deporte'].widget.attrs['class']='form-control'
        self.fields['club'].widget.attrs['class']='form-control'
        self.fields['hobbie'].widget.attrs['class']='form-control'
        self.fields['meta'].widget.attrs['class']='form-control'





###ESCOLARIDAD

class EscolaridadForm (forms.ModelForm):

    nombreEscuela = forms.CharField(max_length = 255, required = True)
    domicilioEscuela = forms.CharField(max_length = 255, required = True)
    inicial = forms.CharField(max_length = 25, required = True)
    final = forms.CharField(max_length = 25, required = True)
    anios = forms.IntegerField(required = True)
    titulo = forms.CharField(max_length = 255, required = True)


    class Meta:
        model = Escolaridad
        fields = [
            'idsolicitante',
            'nombreEscuela',
            'domicilioEscuela',
            'inicial',
            'final',
            'anios',
            'titulo',
            'nivel',

        ]

    def __init__(self, *args, **kwargs):
        super (EscolaridadForm,self).__init__(*args, **kwargs)
        self.fields['nombreEscuela'].widget.attrs['class']='form-control'
        self.fields['domicilioEscuela'].widget.attrs['class']='form-control'
        self.fields['inicial'].widget.attrs['class']='form-control'
        self.fields['final'].widget.attrs['class']='form-control'
        self.fields['anios'].widget.attrs['class']='form-control'
        self.fields['titulo'].widget.attrs['class']='form-control'
        self.fields['nivel'].widget.attrs['class']='form-control'


###CONOCIMIENTOS GENERALES

class ConocimientosForm (forms.ModelForm):

    idiomas = forms.CharField(max_length = 100, required = True)
    equipo = forms.CharField(max_length = 100, required = True)
    funciones = forms.CharField(max_length = 25, required = True)
    otros = forms.CharField(max_length = 255, required = True)


    class Meta:
        model = Conocimientos
        fields = [
            'idsolicitante',
            'idiomas',
            'equipo',
            'funciones',
            'otros',


        ]

    def __init__(self, *args, **kwargs):
        super (ConocimientosForm,self).__init__(*args, **kwargs)
        self.fields['idiomas'].widget.attrs['class']='form-control'
        self.fields['equipo'].widget.attrs['class']='form-control'
        self.fields['funciones'].widget.attrs['class']='form-control'
        self.fields['otros'].widget.attrs['class']='form-control'

###EMPLEO ACTUAL Y ANTERIORES

class EmpleosForm (forms.ModelForm):

    nombreEmp = forms.CharField(max_length = 255, required = True)
    domicilio = forms.CharField(max_length = 200, required = True)
    telefono = forms.CharField(max_length = 30, required = True)
    tiempo = forms.CharField(max_length = 150, required = True)
    puestoIni = forms.CharField (max_length =30, required = True)
    puestoFin = forms.CharField (max_length =30, required = True)
    sueldoIni = forms.CharField (max_length =30, required = True)
    sueldoFin = forms.CharField (max_length =30, required = True)
    motivo = forms.CharField (max_length =255, required = True)
    jefe = forms.CharField (max_length =255, required = True)
    actividad = forms.CharField (max_length =255, required = True)

    class Meta:
        model = Empleos
        fields = [
            'idsolicitante',
            'nombreEmp',
            'domicilio',
            'telefono',
            'tiempo',
            'puestoIni',
            'puestoFin',
            'sueldoIni',
            'sueldoFin',
            'motivo',
            'jefe',
            'actividad',
            #'noRazon',


        ]

    def __init__(self, *args, **kwargs):
        super (EmpleosForm,self).__init__(*args, **kwargs)
        self.fields['nombreEmp'].widget.attrs['class']='form-control'
        self.fields['domicilio'].widget.attrs['class']='form-control'
        self.fields['telefono'].widget.attrs['class']='form-control'
        self.fields['tiempo'].widget.attrs['class']='form-control'
        self.fields['puestoIni'].widget.attrs['class']='form-control'
        self.fields['puestoFin'].widget.attrs['class']='form-control'
        self.fields['sueldoIni'].widget.attrs['class']='form-control'
        self.fields['sueldoFin'].widget.attrs['class']='form-control'
        self.fields['motivo'].widget.attrs['class']='form-control'
        self.fields['jefe'].widget.attrs['class']='form-control'
        self.fields['actividad'].widget.attrs['class']='form-control'
        #self.fields['noRazon'].widget.attrs['class']='form-control'


########REFERENCIAS PERSONALES

class ReferenciasForm (forms.ModelForm):

    nombre = forms.CharField(max_length = 100, required = True)
    domicilio = forms.CharField(max_length = 100, required = True)
    telefono = forms.CharField(max_length = 30, required = True)
    ocupacion = forms.CharField(max_length = 30, required = True)
    tiempo = forms.CharField(max_length = 10, required = True)



    class Meta:
        model = Referencias
        fields = [
            'idsolicitante',
            'nombre',
            'domicilio',
            'telefono',
            'ocupacion',
            'tiempo',


        ]

    def __init__(self, *args, **kwargs):
        super (ReferenciasForm,self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class']='form-control'
        self.fields['domicilio'].widget.attrs['class']='form-control'
        self.fields['telefono'].widget.attrs['class']='form-control'
        self.fields['ocupacion'].widget.attrs['class']='form-control'
        self.fields['tiempo'].widget.attrs['class']='form-control'


#######GENERALES

class GeneralesForm (forms.ModelForm):  

    ciaFianza = forms.CharField(max_length = 255, required = True)
    ciaSeguro = forms.CharField(max_length = 255, required = True)
    razonReside = forms.CharField(max_length = 255, required = True)
    nombres = forms.CharField(max_length = 100, required = True)
    nombreSin = forms.CharField(max_length = 60, required = True)
    razonViaje = forms.CharField(max_length = 60, required = True)
    presentar = forms.CharField(max_length = 60, required = True)



    class Meta:
        model = Generales
        fields = [
            'idsolicitante',
            'medio',
            'afianzado',
            'ciaFianza',
            'seguro',
            'ciaSeguro',
            'residencia',
            'razonReside',
            'familiares',
            'nombres',
            'sindicato',
            'nombreSin',
            'viajar',
            'razonViaje',
            'presentar',
        ]

    def __init__(self, *args, **kwargs):
        super (GeneralesForm,self).__init__(*args, **kwargs)
        self.fields['medio'].widget.attrs['class']='form-control'
        self.fields['afianzado'].widget.attrs['class']='form-control'
        self.fields['ciaFianza'].widget.attrs['class']='form-control'
        self.fields['seguro'].widget.attrs['class']='form-control'
        self.fields['ciaSeguro'].widget.attrs['class']='form-control'
        self.fields['residencia'].widget.attrs['class']='form-control'
        self.fields['razonReside'].widget.attrs['class']='form-control'
        self.fields['familiares'].widget.attrs['class']='form-control'
        self.fields['nombres'].widget.attrs['class']='form-control'
        self.fields['sindicato'].widget.attrs['class']='form-control'
        self.fields['nombreSin'].widget.attrs['class']='form-control'
        self.fields['viajar'].widget.attrs['class']='form-control'
        self.fields['razonViaje'].widget.attrs['class']='form-control'
        self.fields['presentar'].widget.attrs['class']='form-control'

########ECONOMICO


class EconomicoForm (forms.ModelForm):  

    modo = forms.CharField(max_length = 20, required = True)
    importe = forms.CharField(max_length = 20, required = True)
    importeCasa = forms.CharField(max_length = 15, required = True)
    placas = forms.CharField(max_length = 10, required = True)
    marca = forms.CharField(max_length = 20, required = True)
    modelo = forms.CharField(max_length = 20, required = True)

    ingresos = forms.CharField(max_length = 10, required = True)
    egresos = forms.CharField(max_length = 10, required = True)
    ahorros = forms.CharField(max_length = 10, required = True)
    total = forms.CharField(max_length = 10, required = True)
    ingresoCony = forms.CharField(max_length = 10, required = True)
    rentaMensual = forms.CharField(max_length = 10, required = True)
    clase = forms.CharField(max_length = 10, required = True)
    impDeuda = forms.CharField(max_length = 10, required = True)
    abonoMensual = forms.CharField(max_length = 10, required = True)





    class Meta:
        model = Economico
        fields = [
            'idsolicitante',
            'ingreso',
            'modo',
            'importe',
            'casa',
            'importeCasa',
            'auto',
            'placas',
            'marca',
            'modelo',
            'ingresos',
            'egresos',
            'ahorros',
            'total',
            'conyuge',
            'ingresoCony',
            'renta',
            'rentaMensual',
            'deudas',
            'clase',
            'impDeuda',
            'deudas',
        ]

    def __init__(self, *args, **kwargs):
        super (EconomicoForm,self).__init__(*args, **kwargs)
        self.fields['ingreso'].widget.attrs['class']='form-control'
        self.fields['modo'].widget.attrs['class']='form-control'
        self.fields['importe'].widget.attrs['class']='form-control'
        self.fields['casa'].widget.attrs['class']='form-control'
        self.fields['importeCasa'].widget.attrs['class']='form-control'
        self.fields['auto'].widget.attrs['class']='form-control'
        self.fields['placas'].widget.attrs['class']='form-control'
        self.fields['marca'].widget.attrs['class']='form-control'
        self.fields['modelo'].widget.attrs['class']='form-control'
        self.fields['ingresos'].widget.attrs['class']='form-control'
        self.fields['egresos'].widget.attrs['class']='form-control'
        self.fields['ahorros'].widget.attrs['class']='form-control'
        self.fields['total'].widget.attrs['class']='form-control'
        self.fields['conyuge'].widget.attrs['class']='form-control'
        self.fields['ingresoCony'].widget.attrs['class']='form-control'
        self.fields['renta'].widget.attrs['class']='form-control'
        self.fields['rentaMensual'].widget.attrs['class']='form-control'
        self.fields['deudas'].widget.attrs['class']='form-control'
        self.fields['clase'].widget.attrs['class']='form-control'
        self.fields['impDeuda'].widget.attrs['class']='form-control'
        self.fields['abonoMensual'].widget.attrs['class']='form-control'




class ArchivosForm(forms.ModelForm):

    class Meta:
        model = Archivos


class UploadForm(forms.ModelForm):
    class Meta:
        model = Imagen
    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['imagen1'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen2'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen3'].widget.attrs['class'] = 'btn btn-info'
        self.fields['imagen4'].widget.attrs['class'] = 'btn btn-info'

#### Documentos de Empleados

class SearchDocsForm (forms.Form):
      class Meta:
          model = Catdoc
      def __init__(self, *arg, **kwargs):
            super (SearchDocsForm, self).__init__(*arg, **kwargs)

class documentosForm(forms.ModelForm):
    class Meta:
            model = Catdoc
            fields = [
                    'nombreDoc',
                    'observacionesDoc',
                     ]

    def __init__(self, *arg, **kwargs):
            super (documentosForm, self).__init__(*arg, **kwargs)
            self.fields['nombreDoc'].widget.attrs['class']='form-control'
            self.fields['observacionesDoc'].widget.attrs['class']='form-control'

#### Puestos de Empleados


class SearchPuestosForm (forms.Form):
      class Meta:
           model = Puestos
      def __init__(self, *arg, **kwargs):
          super (SearchPuestosForm, self).__init__(*arg, **kwargs)

class puestoForm (forms.ModelForm):

      class Meta:
           model = Puestos
           fields = [
                  'nombre',
                  'descripcion',
                  'tipo',
                  'sueldo',
                  ]

      def __init__(self, *arg, **kwargs):
          super (puestoForm, self).__init__(*arg, **kwargs)
          self.fields['nombre'].widget.attrs['class']='form-control'
          self.fields['descripcion'].widget.attrs['class']='form-control'
          self.fields['tipo'].widget.attrs['class']='form-control'
          self.fields['sueldo'].widget.attrs['class']='form-control'


class MovEmpForm (forms.ModelForm):

      fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = False)

      class Meta: 
            model = movimientos
            fields = [
            'empleado',
            'tipo',
            'fecha',
            'realiza',
            'motivo',
            ]

      def __init__(self, *arg, **kwargs):
           super (MovEmpForm, self).__init__(*arg, **kwargs)
           self.fields['empleado'].widget.attrs['class']='form-control'
           self.fields['tipo'].widget.attrs['class']= 'form-control'
           self.fields['fecha'].widget.attrs['class']= 'form-control'
           self.fields['realiza'].widget.attrs['class']= 'form-control'
           self.fields['motivo'].widget.attrs['class']= 'form-control'


class InfoGralForm (forms.ModelForm):

    class Meta:
        model = InfoGral
        fields = [
            'idsolicitante',
            'nombreCompleto',
            'telefono',
            'edoCivil',
            'cadadoPor',
            'numHijos',
            'nomEsposa',
            'ocupacionEsp',
            'vivenPadres',
            'ocupacionPadres',
            'ultimaEmp',
            'telEmp',
            'nombreJefe',
            'puestoJefe',
            'razonEmp',
            'explicaEmp',
            'demandas',
            'explicaDem',
            'tieneLic',
            'tipoLic',
            'numeroLic',
            'vigenciaLic',
            'casaPropia',
            'numHabitantes',
        ]

    def __init__(self, *arg, **kwargs):
           super (InfoGralForm, self).__init__(*arg, **kwargs)
           self.fields['nombreCompleto'].widget.attrs['class']='form-control'
           self.fields['telefono'].widget.attrs['class']= 'form-control'
           self.fields['edoCivil'].widget.attrs['class']= 'form-control'
           self.fields['cadadoPor'].widget.attrs['class']= 'form-control'
           self.fields['numHijos'].widget.attrs['class']= 'form-control'
           self.fields['nomEsposa'].widget.attrs['class']='form-control'
           self.fields['ocupacionEsp'].widget.attrs['class']= 'form-control'
           self.fields['vivenPadres'].widget.attrs['class']= 'form-control'
           self.fields['ocupacionPadres'].widget.attrs['class']= 'form-control'
           self.fields['ultimaEmp'].widget.attrs['class']= 'form-control'
           self.fields['telEmp'].widget.attrs['class']='form-control'
           self.fields['nombreJefe'].widget.attrs['class']= 'form-control'
           self.fields['puestoJefe'].widget.attrs['class']= 'form-control'
           self.fields['razonEmp'].widget.attrs['class']= 'form-control'
           self.fields['explicaEmp'].widget.attrs['class']= 'form-control'
           self.fields['demandas'].widget.attrs['class']='form-control'
           self.fields['explicaDem'].widget.attrs['class']= 'form-control'
           self.fields['tieneLic'].widget.attrs['class']= 'form-control'
           self.fields['tipoLic'].widget.attrs['class']= 'form-control'
           self.fields['numeroLic'].widget.attrs['class']= 'form-control'
           self.fields['vigenciaLic'].widget.attrs['class']= 'form-control'
           self.fields['casaPropia'].widget.attrs['class']= 'form-control'
           self.fields['numHabitantes'].widget.attrs['class']= 'form-control'

class CuestionarioForm (forms.ModelForm):

    class Meta:
        model = Cuestionario
        fields = [
            'idsolicitante',
            'bebida',
            'freBebida',
            'fuma',
            'freFuma',
            'drog',
            'tiempoDrog',
            'actividad',
            'escolaridad',
            'auto',
            'oportunidad',
            'compromiso',
            'pretenciones',
            'gastos',
            'futuro',
            'recomienda',
            'beneficiosVit',
            'firma',
            'opinionRef',
            'opinionMer',
            'suvenir',
            'razonSuvenir',
            'ganarGente',
            'reaccion',
            'correr',
            'velocidad',
            'ciudad',
            'razonCiudad',
            'metaVida',
            'familiaIdent',
            'sitPais',
            'futuroHijo',
            'finesSemana',
            'apodo',
        ]

    def __init__(self, *arg, **kwargs):
           super (CuestionarioForm, self).__init__(*arg, **kwargs)
           self.fields['bebida'].widget.attrs['class']='form-control'
           self.fields['freBebida'].widget.attrs['class']= 'form-control'
           self.fields['fuma'].widget.attrs['class']= 'form-control'
           self.fields['freFuma'].widget.attrs['class']= 'form-control'
           self.fields['drog'].widget.attrs['class']= 'form-control'
           self.fields['tiempoDrog'].widget.attrs['class']='form-control'
           self.fields['actividad'].widget.attrs['class']= 'form-control'
           self.fields['escolaridad'].widget.attrs['class']= 'form-control'
           self.fields['auto'].widget.attrs['class']= 'form-control'
           self.fields['oportunidad'].widget.attrs['class']= 'form-control'
           self.fields['compromiso'].widget.attrs['class']='form-control'
           self.fields['pretenciones'].widget.attrs['class']= 'form-control'
           self.fields['gastos'].widget.attrs['class']= 'form-control'
           self.fields['futuro'].widget.attrs['class']= 'form-control'
           self.fields['recomienda'].widget.attrs['class']= 'form-control'
           self.fields['beneficiosVit'].widget.attrs['class']='form-control'
           self.fields['firma'].widget.attrs['class']= 'form-control'
           self.fields['opinionRef'].widget.attrs['class']= 'form-control'
           self.fields['opinionMer'].widget.attrs['class']= 'form-control'
           self.fields['suvenir'].widget.attrs['class']= 'form-control'
           self.fields['razonSuvenir'].widget.attrs['class']= 'form-control'
           self.fields['ganarGente'].widget.attrs['class']= 'form-control'
           self.fields['reaccion'].widget.attrs['class']= 'form-control'
           self.fields['correr'].widget.attrs['class']= 'form-control'
           self.fields['velocidad'].widget.attrs['class']= 'form-control'
           self.fields['ciudad'].widget.attrs['class']= 'form-control'
           self.fields['razonCiudad'].widget.attrs['class']= 'form-control'
           self.fields['metaVida'].widget.attrs['class']= 'form-control'
           self.fields['familiaIdent'].widget.attrs['class']= 'form-control'
           self.fields['sitPais'].widget.attrs['class']= 'form-control'
           self.fields['futuroHijo'].widget.attrs['class']= 'form-control'
           self.fields['finesSemana'].widget.attrs['class']= 'form-control'
           self.fields['apodo'].widget.attrs['class']= 'form-control'

class InfoHijosForm(forms.ModelForm):

    class Meta:
        model = infohijos
        fields = [
            'idsolicitante',
            'nombre',
            'edad',
            'ocupacion',
        ]

    def __init__(self, *arg, **kwargs):
           super (InfoHijosForm, self).__init__(*arg, **kwargs)
           self.fields['nombre'].widget.attrs['class']='form-control'
           self.fields['edad'].widget.attrs['class']= 'form-control'
           self.fields['ocupacion'].widget.attrs['class']= 'form-control'



class solicitudForm (forms.ModelForm):
    meta = forms.CharField(widget=forms.Textarea, required=True)
    nombreCompleto=forms.CharField(max_length=100, required = False)
    numCartilla=forms.CharField(max_length=100, required=False)
    pasaporte=forms.CharField(max_length=100, required=False)
    nss=forms.CharField(max_length=20, required=False)
    numLicencia=forms.CharField(max_length=20, required=False)
    segundoNombre=forms.CharField(max_length =100, required=False)

    class Meta:
        model = Solicitud

    def __init__(self, *args, **kwargs):
        super (solicitudForm,self).__init__(*args, **kwargs)
        #### Generales
        self.fields['nombreCompleto'].widget.attrs['class']='form-control'
        self.fields['nombre'].widget.attrs['class']='form-control'
        self.fields['segundoNombre'].widget.attrs['class']='form-control'
        self.fields['paterno'].widget.attrs['class']='form-control'
        self.fields['materno'].widget.attrs['class']='form-control'
        self.fields['fechaSol'].widget.attrs['class']='form-control'
        self.fields['puestoSol'].widget.attrs['class']='form-control'
        self.fields['sueldo'].widget.attrs['class']='form-control'
        self.fields['sueldo'].localize=True
        self.fields['edad'].widget.attrs['class']='form-control'
        self.fields['edad'].widget.attrs['size']=2
        self.fields['domicilio'].widget.attrs['class']='form-control'
        self.fields['colonia'].widget.attrs['class']='form-control'
        self.fields['cp'].widget.attrs['class']='form-control'
        self.fields['telefono'].widget.attrs['class']='form-control'
        self.fields['celular'].widget.attrs['class']='form-control'
        self.fields['lugarNacimiento'].widget.attrs['class']='form-control'
        self.fields['fechaNacimiento'].widget.attrs['class']='form-control'
        self.fields['nacionalidad'].widget.attrs['class']='form-control'
        self.fields['viveCon'].widget.attrs['class']='form-control'
        self.fields['dependientes'].widget.attrs['class']='form-control'
        self.fields['sexo'].widget.attrs['class']='form-control'
        self.fields['email'].widget.attrs['class']='form-control'
        self.fields['estadoCivil'].widget.attrs['class']='form-control'
        #Documentacion
        self.fields['rfc'].widget.attrs['class']='form-control'
        self.fields['nss'].widget.attrs['class']='form-control'
        self.fields['numCartilla'].widget.attrs['class']='form-control'
        self.fields['pasaporte'].widget.attrs['class']='form-control'
        self.fields['tieneLicencia'].widget.attrs['class']='form-control'
        #self.fields['tipoLicencia'].widget.attrs['class']='form-control'
        self.fields['numLicencia'].widget.attrs['class']='form-control'
        self.fields['curp'].widget.attrs['class']='form-control'
        self.fields['afore'].widget.attrs['class']='form-control'
        #Salud y habitos
        self.fields['salud'].widget.attrs['class']='form-control'
        self.fields['cronico'].widget.attrs['class']='form-control'
        self.fields['descripcion'].widget.attrs['class']='form-control'
        self.fields['deporte'].widget.attrs['class']='form-control'
        self.fields['club'].widget.attrs['class']='form-control'
        self.fields['hobbie'].widget.attrs['class']='form-control'
        self.fields['meta'].widget.attrs['class']='form-control'
        #Familiares
        #self.fields['nombreFamiliar'].widget.attrs['class']='form-control'
        #self.fields['parentesco'].widget.attrs['class']='form-control'
        #self.fields['viveFinado'].widget.attrs['class']='form-control'
        #self.fields['domicilioFam'].widget.attrs['class']='form-control'
        #self.fields['ocupacion'].widget.attrs['class']='form-control'
        #self.fields['edad'].widget.attrs['class']='form-control'
        #Escolaridad
        #self.fields['nombreEscuela'].widget.attrs['class']='form-control'
        #self.fields['domicilioEscuela'].widget.attrs['class']='form-control'
        #self.fields['inicial'].widget.attrs['class']='form-control'
        #self.fields['final'].widget.attrs['class']='form-control'
        #self.fields['anios'].widget.attrs['class']='form-control'
        #self.fields['titulo'].widget.attrs['class']='form-control'
        #self.fields['nivel'].widget.attrs['class']='form-control'
        #Conocimientos
        self.fields['idiomas'].widget.attrs['class']='form-control'
        self.fields['equipo'].widget.attrs['class']='form-control'
        self.fields['funciones'].widget.attrs['class']='form-control'
        self.fields['otros'].widget.attrs['class']='form-control'
        #Empleos
        #self.fields['nombreEmp'].widget.attrs['class']='form-control'
        #self.fields['domicilioEmp'].widget.attrs['class']='form-control'
        #self.fields['telefonoEmp'].widget.attrs['class']='form-control'
        #self.fields['tiempo'].widget.attrs['class']='form-control'
        #self.fields['puestoIni'].widget.attrs['class']='form-control'
        #self.fields['puestoFin'].widget.attrs['class']='form-control'
        #self.fields['sueldoIni'].widget.attrs['class']='form-control'
        #self.fields['sueldoFin'].widget.attrs['class']='form-control'
        #self.fields['motivo'].widget.attrs['class']='form-control'
        #self.fields['jefe'].widget.attrs['class']='form-control'
        #self.fields['actividad'].widget.attrs['class']='form-control'
        #Referencias
        #self.fields['nombreRef'].widget.attrs['class']='form-control'
        #self.fields['domicilioRef'].widget.attrs['class']='form-control'
        #self.fields['telefonoRef'].widget.attrs['class']='form-control'
        #self.fields['ocupacionRef'].widget.attrs['class']='form-control'
        #self.fields['tiempoRef'].widget.attrs['class']='form-control'
        #Datos generales
        self.fields['medio'].widget.attrs['class']='form-control'
        self.fields['afianzado'].widget.attrs['class']='form-control'
        self.fields['ciaFianza'].widget.attrs['class']='form-control'
        self.fields['seguro'].widget.attrs['class']='form-control'
        self.fields['ciaSeguro'].widget.attrs['class']='form-control'
        self.fields['residencia'].widget.attrs['class']='form-control'
        self.fields['razonReside'].widget.attrs['class']='form-control'
        self.fields['familiaresT'].widget.attrs['class']='form-control'
        self.fields['nombres'].widget.attrs['class']='form-control'
        self.fields['sindicato'].widget.attrs['class']='form-control'
        self.fields['nombreSin'].widget.attrs['class']='form-control'
        self.fields['viajar'].widget.attrs['class']='form-control'
        self.fields['razonViaje'].widget.attrs['class']='form-control'
        self.fields['presentar'].widget.attrs['class']='form-control'
        #Datos Economicos
        self.fields['ingreso'].widget.attrs['class']='form-control'
        self.fields['modo'].widget.attrs['class']='form-control'
        self.fields['importe'].widget.attrs['class']='form-control'
        self.fields['casa'].widget.attrs['class']='form-control'
        self.fields['importeCasa'].widget.attrs['class']='form-control'
        self.fields['auto'].widget.attrs['class']='form-control'
        self.fields['placas'].widget.attrs['class']='form-control'
        self.fields['marca'].widget.attrs['class']='form-control'
        self.fields['modelo'].widget.attrs['class']='form-control'
        self.fields['ingresos'].widget.attrs['class']='form-control'
        self.fields['egresos'].widget.attrs['class']='form-control'
        self.fields['ahorros'].widget.attrs['class']='form-control'
        self.fields['total'].widget.attrs['class']='form-control'
        self.fields['conyuge'].widget.attrs['class']='form-control'
        self.fields['ingresoCony'].widget.attrs['class']='form-control'
        self.fields['renta'].widget.attrs['class']='form-control'
        self.fields['rentaMensual'].widget.attrs['class']='form-control'
        self.fields['deudas'].widget.attrs['class']='form-control'
        #self.fields['clase'].widget.attrs['class']='form-control'
        self.fields['impDeuda'].widget.attrs['class']='form-control'
        self.fields['abonoMensual'].widget.attrs['class']='form-control'

###FAMILIARES

class FamiliaresForm (forms.ModelForm):

    class Meta:
        model = Familiares
        #exclude = ('idsolicitante',)
        #fields = ['idsolicitante','nombreFamiliar','parentesco','viveFinado','domicilioFam','ocupacion','edadFam',]


    def __init__(self, *args, **kwargs):
        super (FamiliaresForm,self).__init__(*args, **kwargs)
        self.fields['nombreFamiliar'].widget.attrs['class']='form-control'
        self.fields['parentesco'].widget.attrs['class']='form-control'
        self.fields['viveFinado'].widget.attrs['class']='form-control'
        self.fields['domicilioFam'].widget.attrs['class']='form-control'
        self.fields['ocupacion'].widget.attrs['class']='form-control'
        self.fields['edadFam'].widget.attrs['class']='form-control'


class EscolaridadForm (forms.ModelForm):

    class Meta:
        model = Escolaridad


    def __init__(self, *args, **kwargs):
        super (EscolaridadForm,self).__init__(*args, **kwargs)
        self.fields['nombreEscuela'].widget.attrs['class']='form-control'
        self.fields['domicilioEscuela'].widget.attrs['class']='form-control'
        self.fields['inicial'].widget.attrs['class']='form-control'
        self.fields['final'].widget.attrs['class']='form-control'
        self.fields['anios'].widget.attrs['class']='form-control'
        self.fields['titulo'].widget.attrs['class']='form-control'
        self.fields['nivel'].widget.attrs['class']='form-control'

###EMPLEO ACTUAL Y ANTERIORES

class EmpleosForm (forms.ModelForm):

    class Meta:
        model = Empleos

    def __init__(self, *args, **kwargs):
        super (EmpleosForm,self).__init__(*args, **kwargs)
        self.fields['nombreEmp'].widget.attrs['class']='form-control'
        self.fields['domicilioEmp'].widget.attrs['class']='form-control'
        self.fields['telefonoEmp'].widget.attrs['class']='form-control'
        self.fields['tiempo'].widget.attrs['class']='form-control'
        self.fields['puestoIni'].widget.attrs['class']='form-control'
        self.fields['puestoFin'].widget.attrs['class']='form-control'
        self.fields['sueldoIni'].widget.attrs['class']='form-control'
        self.fields['sueldoFin'].widget.attrs['class']='form-control'
        self.fields['motivo'].widget.attrs['class']='form-control'
        self.fields['jefe'].widget.attrs['class']='form-control'
        self.fields['actividad'].widget.attrs['class']='form-control'
        self.fields['permiso'].widget.attrs['class']='form-control'
        self.fields['noRazon'].widget.attrs['class']='form-control'


########REFERENCIAS PERSONALES

class ReferenciasForm (forms.ModelForm):

    class Meta:
        model = Referencias

    def __init__(self, *args, **kwargs):
        super (ReferenciasForm,self).__init__(*args, **kwargs)
        self.fields['nombreRef'].widget.attrs['class']='form-control'
        self.fields['domicilioRef'].widget.attrs['class']='form-control'
        self.fields['telefonoRef'].widget.attrs['class']='form-control'
        self.fields['ocupacionRef'].widget.attrs['class']='form-control'
        self.fields['tiempoRef'].widget.attrs['class']='form-control'
