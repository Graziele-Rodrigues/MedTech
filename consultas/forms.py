from django import forms
from .models import Consultas
from django.utils import timezone

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = ['paciente', 'profissional', 'data_hora']
        widgets = {
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
        input_formats = {
            'data_hora': ['%Y-%m-%dT%H:%M'],
        }
