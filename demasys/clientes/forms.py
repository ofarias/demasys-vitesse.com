# coding: utf-8
from django import forms
from models import Cliente
from clientes.models import Departamento

class ClienteForm(forms.ModelForm):    
    class Meta:
        model = Cliente
        exclude = ('claveSAE',
                    )
        
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['class'] = 'form-control'
        self.fields['nombre_corto'].widget.attrs['class'] = 'form-control'
        self.fields['rfc'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_clave_municipio'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_colonia'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_calle'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_numero'].widget.attrs['class'] = 'form-control'
        self.fields['facturacion_cp'].widget.attrs['class'] = 'form-control'
        self.fields['recoleccion_clave_municipio'].widget.attrs['class'] = 'form-control'    
        self.fields['recoleccion_colonia'].widget.attrs['class'] = 'form-control'
        self.fields['recoleccion_calle'].widget.attrs['class'] = 'form-control'
        self.fields['recoleccion_numero'].widget.attrs['class'] = 'form-control'
        self.fields['recoleccion_cp'].widget.attrs['class'] = 'form-control'
        self.fields['correo'].widget.attrs['class'] = 'form-control'
        self.fields['contacto'].widget.attrs['class'] = 'form-control'
        self.fields['telefono'].widget.attrs['class'] = 'form-control'
        self.fields['datos_bancarios'].widget.attrs['class'] = 'form-control'

	
        
class DepartamentoForm(forms.ModelForm):    
    class Meta:
        model = Departamento
        exclude = ('cliente',
                    #'claveSAE',
                    )
        
    def __init__(self, *args, **kwargs):
        super(DepartamentoForm, self).__init__(*args, **kwargs)
        self.fields['departamento'].widget.attrs['class'] = 'form-control'                 
