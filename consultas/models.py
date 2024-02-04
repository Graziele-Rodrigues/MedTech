from django.db import models
from funcionarios.models import ProfissionalSaude
from pacientes.models import Paciente

class Consultas(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
    data_hora = models.DateTimeField(null=False, blank=False)

    STATUS_CHOICES = (
        ('agendada', 'Agendada'),
        ('concluída', 'Concluída'),
        ('cancelada', 'Cancelada'),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='agendada')

    def __str__(self):
        return f"Consulta em {self.data_hora} com {self.paciente.nome} - Status: {self.status}"
