from django import forms
from .models import Funcionarios


class FuncionariosForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'cargo', 'valor_consulta']