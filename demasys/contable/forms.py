# coding: utf-8
from django import forms
from decimal import Decimal
from models import Partidas, Movimientos, Area

class MovimientosForm(forms.Form):

    concepto = forms.CharField(max_length=150)
    comentarios = forms.CharField(max_length=160)
    monto = forms.DecimalField(max_digits=12,decimal_places=2)
    partida = forms.ModelChoiceField(queryset = Partidas.objects.filter(activo=True),required = True)
    areas = forms.ModelChoiceField(queryset = Area.objects.filter(activo=True),required = True)

    def __init__(self, *args, **kwargs):
        super(MovimientosForm, self).__init__(*args, **kwargs)
        self.fields['concepto'].widget.attrs['class'] = 'form-control input-small select2 concepto'
        self.fields['comentarios'].widget.attrs['class']='form-control'
        self.fields['monto'].widget.attrs['class'] = 'form-control'
        self.fields['partida'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['areas'].widget.attrs['class']='form-control form-filter input-sm select2'

class MovContaForm(forms.ModelForm):

    class Meta:
        model = Movimientos
        exclude = ('id_auth_user', 'fecha', 'tipo','ref_viaje','ref_solicitud','montoPartida', 'maniobras_locales', 'maniobras_foraneas', 'maniobras_retrabajos', 'casetas_lg','cliente_paga')

    concepto = forms.CharField(max_length=150)
    comentarios = forms.CharField(max_length=160)
    importe = forms.DecimalField(max_digits=12,decimal_places=2)
    idPartida = forms.ModelChoiceField(queryset = Partidas.objects.filter(activo=True))
    idArea = forms.ModelChoiceField(queryset = Area.objects.filter(activo=True))

    def __init__(self, *args, **kwargs):
        super(MovContaForm, self).__init__(*args, **kwargs)
        self.fields['concepto'].widget.attrs['class'] = 'form-control input-small select2 concepto'
        self.fields['comentarios'].widget.attrs['class']='form-control'
        self.fields['importe'].widget.attrs['class'] = 'form-control'
        self.fields['idPartida'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['idArea'].widget.attrs['class']='form-control form-filter input-sm select2'
