from django.db import models
from pacientes.models import Paciente

class RegistroMedico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tratamento = models.TextField()
    diagnostico = models.TextField()
