from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator
from .models import Productos

class ProductosForm(forms.ModelForm):
    class Meta:  # clase meta para establecer las caracteristicas del formulario ProductosForm
        model = Productos  # modelo al que pertenece el formulario
        fields = ['nombre', 'precio', 'descripcion']  # campos que llevara el formulario
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'descripcion': 'Descripcion',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'style': 'width: 300px'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 300px'})
        }