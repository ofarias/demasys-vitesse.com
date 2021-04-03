# coding: utf-8
from django import forms
from django.contrib.auth.forms import UserChangeForm
#from django.contrib.auth.models import User
from models import Perfil
######################################################
from django.contrib.auth.models import User,Group,Permission

class UsuarioForm(UserChangeForm):
    
    email = forms.EmailField()
    user_permissions = forms.ModelMultipleChoiceField(Permission.objects.all(), widget=forms.CheckboxSelectMultiple,  required=False, label=u'Permisos para el Usuario:')
    
    
    class Meta:
        model = User
        exclude = ('password', 'is_staff',
                   'last_login', 'date_joined')
        
    def clean_password(self):
        return ''
        
    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['groups'].widget.attrs['class'] = 'form-control'
        #self.fields['user_permissions'].queryset = Permission.objects.all().exclude(content_type__app_label__in=['admin', 'auth'])
        
class PerfilModelForm(forms.ModelForm):    
    apellido_materno = forms.CharField(max_length=40, required=False)
    telefono = forms.CharField(max_length=40, required=False, label=u'Teléfono')
    
    class Meta:
        model = Perfil
        exclude = ('user',)
        
    def __init__(self, *args, **kwargs):
        super(PerfilModelForm, self).__init__(*args, **kwargs)
        self.fields['apellido_materno'].widget.attrs['class'] = 'form-control'
        self.fields['telefono'].widget.attrs['class'] = 'form-control'
        self.fields['cliente'].widget.attrs['class'] = 'form-control'
        
        
        
class UsuarioPerfilForm(UserChangeForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        exclude = ('password', 'is_staff', 
                   'is_active', 'groups',
                  'is_superuser', 'last_login', 'date_joined', 'user_permissions')
##########################################################################################


#class PermissionGroup(forms.ModelForm):
    #permissions = forms.ModelMultipleChoiceField(Permission.objects.none(), widget=forms.CheckboxSelectMultiple)
    #permisos = forms.ModelMultipleChoiceField(Permission.objects.all(), widget=forms.CheckboxSelectMultiple)
    
    #class Meta:
    #    model = Perfil
    #    exclude = ('user',)

    #def __init__(self,  *args, **kwargs):
    #    super(PermissionGroup, self).__init__( *args, **kwargs)
        
    #    self.fields['permisos'].queryset = Permission.objects.all().exclude(content_type__app_label__in=['admin', 'auth']) 

