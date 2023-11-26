from django import forms
from .models import Atendentes


class AtendentesForm(forms.ModelForm):
    class Meta:
        model = Atendentes
        fields = ['nome', 'cargo', 'valor_consulta']