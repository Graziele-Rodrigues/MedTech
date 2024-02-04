from django import forms
from .models import Consultas

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consultas
        fields = ['paciente', 'profissional', 'data_hora', 'status']
