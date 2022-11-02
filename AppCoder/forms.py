from django import forms

class JuegoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    genero = forms.CharField(max_length=50)
    anio_lanzamiento = forms.IntegerField()
    desarrolladora = forms.CharField(max_length=50)
    
class EquipoFormulario(forms.Form):
    nombre  = forms.CharField(max_length=50)
    pais = forms.CharField(max_length=50)
    plataforma = forms.CharField(max_length=50)

class TorneoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    reglas = forms.CharField(max_length=255)
    puntos = forms.IntegerField()