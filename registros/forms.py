from django.forms import ModelForm
from .models import RegistroMedico

class RegistroMedicoForm(ModelForm):
    class Meta:
        model = RegistroMedico
        fields = ['paciente', 'tratamento', 'diagnostico']