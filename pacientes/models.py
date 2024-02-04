from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=15, null=False, blank=False)
    telefone_secundario = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(null=False, blank=False)
    plano_saude = models.CharField(max_length=50, blank=True)
    endereco = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.nome
    
    def idade(self):
        from datetime import date
        return date.today().year - self.data_nascimento.year