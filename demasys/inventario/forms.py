from django import forms
from models import Productos, Movimientos
from transportes import settings


TIPO = (
	('E', 'Entrada'),
	('S', 'Salida'),
)

class InventarioUploadForm(forms.Form):
    docfile = forms.FileField(
        label='Selecciona un archivo'
        )

class ProductoForm(forms.ModelForm):

    existencia = forms.DecimalField (max_digits = 7, decimal_places = 2, required = False)
    costoUnitario = forms.DecimalField (max_digits = 7, decimal_places = 2, required = False)

    class Meta:
        model = Productos

    def __init__(self, *args, **kwargs):
        super(ProductoForm, self).__init__(*args, **kwargs)
        self.fields['descripcion'].widget.attrs['class'] = 'form-control'
        self.fields['existencia'].widget.attrs['class'] = 'form-control'
        self.fields['costoUnitario'].widget.attrs['class'] = 'form-control'

class reporteForm(forms.Form):

    producto = forms.ModelChoiceField(queryset = Productos.objects.all(),required = False)
    tipo = forms.ChoiceField(choices = TIPO, required = True)
    fecha_from = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=True)
    fecha_to = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS, required=True)

    def __init__(self, *args, **kwargs):
        super(reporteForm, self).__init__(*args, **kwargs)
        self.fields['producto'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['tipo'].widget.attrs['class']='form-control form-filter input-sm select2'
        self.fields['fecha_from'].widget.attrs['class'] = 'form-control form-filter input-sm '
        self.fields['fecha_from'].widget.attrs['readonly'] = 'readonly'
        self.fields['fecha_to'].widget.attrs['class'] = 'form-control form-filter input-sm'
        self.fields['fecha_to'].widget.attrs['readonly'] = 'readonly'

class MovimientosForm(forms.ModelForm):

     fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = False)
     costo = forms.DecimalField (max_digits = 8, decimal_places = 2, required = False)
     factor= forms.DecimalField (max_digits = 6, decimal_places = 2, required = False)
     movimiento = forms.CharField (max_length = 1, required = False )
     


     class Meta:
          model = Movimientos
      
     def __init__(self, *args, **kwargs):
         super(MovimientosForm, self).__init__(*args, **kwargs)
         self.fields['fecha'].widget.attrs['class']='form-control form-filter input-sm'
         self.fields['costo'].widget.attrs['class']='form-control'
         self.fields['unidades'].widget.attrs['class']='form-control'
         self.fields['movimiento'].widget.attrs['class']='form-control'
         self.fields['idProducto'].widget.attrs['class']='form-control'
         self.fields['idSolicitud'].widget.attrs['class']='form-control'
         self.fields['idEconomico'].widget.attrs['class']='form-control'


class MovimientosAddForm(forms.ModelForm): ##Compras de productos

     fecha = forms.DateField(input_formats=settings.DATE_INPUT_FORMATS,required = False)
     costo = forms.DecimalField (max_digits = 8, decimal_places = 2, required = True)
     factor= forms.DecimalField (max_digits = 6, decimal_places = 2, required = False)
     movimiento = forms.CharField (max_length = 1, required = False )
     idEconomico = forms.IntegerField (required = False)


     class Meta:
          model = Movimientos
      
     def __init__(self, *args, **kwargs):
         super(MovimientosAddForm, self).__init__(*args, **kwargs)
         self.fields['fecha'].widget.attrs['class']='form-control form-filter input-sm'
         self.fields['costo'].widget.attrs['class']='form-control'
         self.fields['unidades'].widget.attrs['class']='form-control'
         self.fields['movimiento'].widget.attrs['class']='form-control'
         self.fields['idProducto'].widget.attrs['class']='form-control'
         self.fields['idSolicitud'].widget.attrs['class']='form-control'
         self.fields['idEconomico'].widget.attrs['class']='form-control'
