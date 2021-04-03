# coding: utf-8
from django import forms
from decimal import Decimal
from reporte.models import *

class IngresosEgresosForm(forms.ModelForm):
    mes =  forms.ChoiceField(choices = MESES, required = False)
    class Meta:
        model = ing_egre
        fields = [
        'mes',
        'egresoChoferes',
        'ingresoChoferes',
        'egresoAdmin',
        'ingresoAdmin',
        'directivo',
        'administrativo',
        'operaciones',
        'mantenimiento',
        'choferes',
        'total',
        'mov',
        'porcentaje'

        ]

    def __init__(self, *args, **kwargs):
        super(IngresosEgresosForm, self).__init__(*args, **kwargs)
        self.fields['mes'].widget.attrs['class'] = 'form-control'
        self.fields['egresoChoferes'].widget.attrs['class'] = 'form-control' 
        self.fields['ingresoChoferes'].widget.attrs['class'] = 'form-control'
        self.fields['egresoAdmin'].widget.attrs['class'] = 'form-control'
        self.fields['ingresoAdmin'].widget.attrs['class'] = 'form-control'
        self.fields['directivo'].widget.attrs['class'] = 'form-control'
        self.fields['administrativo'].widget.attrs['class'] = 'form-control'
        self.fields['operaciones'].widget.attrs['class'] = 'form-control'
        self.fields['mantenimiento'].widget.attrs['class'] = 'form-control'
        self.fields['choferes'].widget.attrs['class'] = 'form-control'
        self.fields['total'].widget.attrs['class'] = 'form-control'
        self.fields['mov'].widget.attrs['class'] = 'form-control'
        self.fields['porcentaje'].widget.attrs['class'] = 'form-control'

class NominaForm(forms.ModelForm):
    mes    =  forms.ChoiceField(choices = MESES, required = False)

    class Meta:
        model = nomina
        fields = [
        'mes',
        'operador',
        'administrativo',
        'total',
        'idRep',
        ]

    def __init__(self, *args, **kwargs):
        super(NominaForm, self).__init__(*args, **kwargs)
        self.fields['mes'].widget.attrs['class'] = 'form-control' 
        self.fields['operador'].widget.attrs['class'] = 'form-control'
        self.fields['administrativo'].widget.attrs['class'] = 'form-control'
        self.fields['total'].widget.attrs['class'] = 'form-control'   


class BrutaForm(forms.ModelForm):
    mes    =  forms.ChoiceField(choices = MESES, required = False)
    cliente=  forms.ChoiceField(choices = CLIENTE, required = False)
    class Meta:
        model = venta_bruta
        fields = [
        'mes',
        'cliente',
        'actual',
        'anterior',
        'deocre',
        'idRep',
        ]

    def __init__(self, *args, **kwargs):
        super(BrutaForm, self).__init__(*args, **kwargs)
        self.fields['mes'].widget.attrs['class'] = 'form-control' 
        self.fields['cliente'].widget.attrs['class'] = 'form-control'
        self.fields['actual'].widget.attrs['class'] = 'form-control'
        self.fields['anterior'].widget.attrs['class'] = 'form-control'
        self.fields['deocre'].widget.attrs['class'] = 'form-control' 


class NetaForm(forms.ModelForm):
    mes    =  forms.ChoiceField(choices = MESES, required = False)
    cliente=  forms.ChoiceField(choices = CLIENTE, required = False)
    class Meta:
        model = venta_neta
        fields = [
        'mes',
        'cliente',
        'actual',
        'anterior',
        'deocre',
        'idRep',
        ]

    def __init__(self, *args, **kwargs):
        super(NetaForm, self).__init__(*args, **kwargs)
        self.fields['mes'].widget.attrs['class'] = 'form-control' 
        self.fields['cliente'].widget.attrs['class'] = 'form-control'
        self.fields['actual'].widget.attrs['class'] = 'form-control'
        self.fields['anterior'].widget.attrs['class'] = 'form-control'
        self.fields['deocre'].widget.attrs['class'] = 'form-control'       

class repMensualForm(forms.ModelForm):

    mes = forms.ChoiceField(choices = MESES, required = True)
    text_nom1 = forms.CharField(max_length = 100, required = False)
    text_nom2 = forms.CharField(max_length = 100, required = False)
    text_nom3 = forms.CharField(max_length = 100, required = False)
    text_nom4 = forms.CharField(max_length = 100, required = False) 
    text_nom5 = forms.CharField(max_length = 100, required = False)
    org_dir = forms.CharField(max_length = 100, required = False)
    org_jft = forms.CharField(max_length = 100, required = False)
    org_jfa = forms.CharField(max_length = 100, required = False)
    org_f = forms.CharField(max_length = 100, required = False)
    org_cli = forms.CharField(max_length = 100, required = False)
    org_clg = forms.CharField(max_length = 100, required = False)
    org_jfo = forms.CharField(max_length = 100, required = False)
    org_choferes = forms.CharField(max_length = 100, required = False)
    text_nom6 = forms.CharField(max_length = 100, required = False)
    text_nom7 = forms.CharField(max_length = 100, required = False)
    text_nom8 = forms.CharField(max_length = 100, required = False)
    text_nom9 = forms.CharField(max_length = 100, required = False)
    text_nom10 = forms.CharField(max_length = 100, required = False)

    class Meta: 
        model = infoMensual
        fields=[
        'mes',
        'text_nom1',
        'text_nom2',
        'text_nom3',
        'text_nom4',
        'text_nom5',
        'org_dir',
        'org_jft',
        'org_jfa',
        'org_f',
        'org_cli',
        'org_clg',
        'org_jfo',
        'org_choferes',
        'text_nom6',
        'text_nom7',
        'text_nom8',
        'text_nom9',
        'text_nom10',
        ]              
    def __init__(self, *args, **kwargs):
        super(repMensualForm, self).__init__(*args, **kwargs)
        self.fields['mes'].widget.attrs['class']='form-control'
        self.fields['text_nom1'].widget.attrs['class']='form-control'
        self.fields['text_nom2'].widget.attrs['class']='form-control'
        self.fields['text_nom3'].widget.attrs['class']='form-control'
        self.fields['text_nom4'].widget.attrs['class']='form-control'
        self.fields['text_nom5'].widget.attrs['class']='form-control'
        self.fields['org_dir'].widget.attrs['class']='form-control'
        self.fields['org_jft'].widget.attrs['class']='form-control'
        self.fields['org_jfa'].widget.attrs['class']='form-control'
        self.fields['org_f'].widget.attrs['class']='form-control'
        self.fields['org_cli'].widget.attrs['class']='form-control'
        self.fields['org_clg'].widget.attrs['class']='form-control'
        self.fields['org_jfo'].widget.attrs['class']='form-control'
        self.fields['org_choferes'].widget.attrs['class']='form-control'
        self.fields['text_nom6'].widget.attrs['class']='form-control'
        self.fields['text_nom7'].widget.attrs['class']='form-control'
        self.fields['text_nom8'].widget.attrs['class']='form-control'
        self.fields['text_nom9'].widget.attrs['class']='form-control'
        self.fields['text_nom10'].widget.attrs['class']='form-control'



