from dataclasses import fields
from pyexpat import model
from django import forms
from .models import HC, TV
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class HistoriaClinicaForm(forms.ModelForm):

    class Meta:
        model = HC
        #fields = ["nombre", "apellidos", "CI", "edad", "sexo", "telefono", "direccion", "descripcion"]
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["first_name", "last_name", 'username', "password1", "password2"]



class TarjetaVacunacionForm(forms.ModelForm):

    class Meta:
        model = TV
        fields = '__all__'

        widgets = {
            "fecha_primera_dosis": forms.SelectDateWidget(),
            "fecha_segunda_dosis": forms.SelectDateWidget(),
            "fecha_tercera_dosis": forms.SelectDateWidget()

        }