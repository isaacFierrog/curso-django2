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
                    'class': 'form-control',
                    'placeholder': 'Introduce el nombre del autor'
                }
            ),
            'apellidos': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduce los apellidos del autor'
                }
            ),
            'nacionalidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduce la nacionalidad del autor'
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Introduce la descripcion del autor'
                }
            )
        }