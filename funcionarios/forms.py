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
        
    def __init__(self, *args, **kwargs):
        super(ProfissionalSaudeForm, self).__init__(*args, **kwargs)
        # Define os campos como não obrigatórios por padrão
        self.fields['funcionario'].required = False
        self.fields['registro_cc'].required = False
        self.fields['especialidade'].required = False
