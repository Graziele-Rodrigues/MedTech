from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'telefone', 'telefone_secundario', 'data_nascimento', 'plano_saude', 'endereco']

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }