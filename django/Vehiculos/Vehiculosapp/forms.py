from django import forms
from .models import vehiculo

# Creating a form 

class VehiculoForm(forms.ModelForm):

    # Create meta class
    class Meta:
        # Specify model to be used
        model = vehiculo

        # Specify fields to be used
        fields=[
            "placa",
            "marca",
            "modelo",
            "color",
        ]

        labels = {
            'placa': 'Numero de Placa',
            'marca': 'Marca del Vehículo',
            'modelo': 'Modelo del Vehículo',
            'color': 'Color del Vehículo',
        }

        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.Select(attrs={'class': 'form-control'}),
        }