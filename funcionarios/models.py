from django.db import models

# Create your models here.
class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    valor_consulta = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.description