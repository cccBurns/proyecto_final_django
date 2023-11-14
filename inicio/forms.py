from django import forms
from inicio.models import Monitor
#from ckeditor.fields import RichTextFormField

class BaseMonitorFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    
class CrearMonitorFormulario(BaseMonitorFormulario):
    tipo = forms.CharField(max_length=50)
    modelo = forms.CharField(max_length=40)
    
    
class BusquedaMonitorFormulario(forms.Form):
    tipo = forms.CharField(max_length=50, required=False)
    marca = forms.CharField(max_length=30, required=False)
    modelo = forms.CharField(max_length=40, required=False)
    
class CrearMonitorFormulario(BaseMonitorFormulario):
    ...


class ActualizarMonitorFormulario(BaseMonitorFormulario):
    ...
    