from django import forms
from .models import ProfissionalSaude, Funcionarios

class FuncionariosForm(forms.ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome', 'cargo', 'telefone', 'salario']  # Inclua os campos comuns a todos os funcionários
        widgets = {
            'cargo': forms.Select(attrs={'id': 'id_cargo'}),
        }

class ProfissionalSaudeForm(forms.ModelForm):
    class Meta:
        model = ProfissionalSaude
        fields = ['funcionario', 'registro_cc', 'especialidade']
        widgets = {
            'especialidade': forms.CheckboxSelectMultiple(),
        }
