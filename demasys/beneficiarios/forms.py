from django import forms
from models import Benefi
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User



TIPOS = (
	(1,'Fisica'),
	(2,'Moral'),
)

TIPO_PROD = (
	(1, 'Servicio'),
	(2, 'Producto'),
)

class SearchForm(forms.Form):

	tipo = forms.MultipleChoiceField(choices = TIPOS, required = False)
	razon_social = forms.CharField(max_length = 150, required = False)
	nombre = forms.CharField(max_length = 100, required = False)
	a_paterno = forms.CharField(max_length = 100, required = False)
	a_materno = forms.CharField(max_length = 100, required = False)
	producto = forms.MultipleChoiceField(choices = TIPO_PROD, required = False)
	
	def __init__ (self, *args, **kwargs):
		super(SearchForm, self).__init__(*args, **kwargs)
		self.fields['tipo'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['razon_social'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['nombre'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['a_paterno'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['a_materno'].widget.attrs['class']='form-control form-filter input-sm select2'
		self.fields['producto'].widget.attrs['class']='form-control form-filter input-sm select2'


class AgregarForm(forms.ModelForm):

	a_paterno = forms.CharField(required = False)
	a_materno = forms.CharField(required = False)
	calle = forms.CharField (required = False)
	no_ext = forms.CharField (required = False)
	no_int = forms.CharField (required = False)
	col = forms.CharField (required = False)
	mun_est = forms.CharField (required = False)
	cp = forms.IntegerField(required = False)
	no_cta = forms.CharField(required = False)
	ban = forms.CharField (required = False)
	clabe = forms.CharField(required = False)	

	
	class Meta:
		model = Benefi
		fields = [
			'tipo',
			'nombre',
			'a_paterno',
			'a_materno',
			'producto',
			'no_ext',
			'no_int',
			'col',
			'mun_est',
			'cp',
			'no_cta',
			'ban',
			'clabe',
		]

	def __init__ (self, *args, **kwargs):
		super(AgregarForm, self).__init__(*args, **kwargs)
		self.fields['tipo'].widget.attrs['class']='form-control'
		self.fields['nombre'].widget.attrs['class']='form-control'
		self.fields['a_paterno'].widget.attrs['class']='form-control'
		self.fields['a_materno'].widget.attrs['class']='form-control'
		self.fields['producto'].widget.attrs['class']='form-control'
		self.fields['no_ext'].widget.attrs['class']='form-control'
		self.fields['no_int'].widget.attrs['class']='form-control'
		self.fields['col'].widget.attrs['class']='form-control'
		self.fields['mun_est'].widget.attrs['class']='form-control'
		self.fields['cp'].widget.attrs['class']='form-control'
		self.fields['no_cta'].widget.attrs['class']='form-control'
		self.fields['ban'].widget.attrs['class']='form-control'
		self.fields['clabe'].widget.attrs['class']='form-control'


class EditForm(forms.ModelForm):

	a_paterno = forms.CharField(required = False)
	a_materno = forms.CharField(required = False)
	calle = forms.CharField (required = False)
	no_ext = forms.CharField (required = False)
	no_int = forms.CharField (required = False)
	col = forms.CharField (required = False)
	mun_est = forms.CharField (required = False)
	cp = forms.IntegerField(required = False)
	no_cta = forms.CharField(required = False)
	ban = forms.CharField (required = False)
	clabe = forms.CharField(required = False)	

	
	class Meta:
		model = Benefi
		fields = [
			'tipo',
			'nombre',
			'a_paterno',
			'a_materno',
			'producto',
			'no_ext',
			'no_int',
			'col',
			'mun_est',
			'cp',
			'no_cta',
			'ban',
			'clabe',
		]

	def __init__ (self, *args, **kwargs):
		super(EditForm, self).__init__(*args, **kwargs)
		instance = getattr(self,'instance',None)
		if instance and instance.id:
			self.fields['tipo'].widget.attrs['class']='form-control'
			self.fields['nombre'].widget.attrs['class']='form-control'
			self.fields['a_paterno'].widget.attrs['class']='form-control'
			self.fields['a_materno'].widget.attrs['class']='form-control'
			self.fields['producto'].widget.attrs['class']='form-control'
			self.fields['no_ext'].widget.attrs['class']='form-control'
			self.fields['no_int'].widget.attrs['class']='form-control'
			self.fields['col'].widget.attrs['class']='form-control'
			self.fields['mun_est'].widget.attrs['class']='form-control'
			self.fields['cp'].widget.attrs['class']='form-control'
			self.fields['no_cta'].widget.attrs['class']='form-control'
			self.fields['ban'].widget.attrs['class']='form-control'
			self.fields['clabe'].widget.attrs['class']='form-control'
	
	def clean_fields(self):
		instance = getattr(self,'instance',None)
		if instance:
			return instance.beneficiario
		else:
			return self.cleaned_data.get('beneficiario',None)
