from django import forms
from .models import Autor


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            'nombre',
            'apellidos',
            'nacionalidad',
            'descripcion'
        ]
        labels = {
            'nombre': 'Nombre del autor',
            'apellidos': 'Apellido del autor',
            'nacionalidad': 'Nacionalidad del autor',
            'descripcion': 'Pequeña descripcion'
        }
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }