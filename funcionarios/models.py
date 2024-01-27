from django.db import models

class Cargo(models.Model):
    id = models.AutoField(primary_key=True)  # Adicionando campo id
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Especialidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Funcionarios(models.Model):
    id = models.AutoField(primary_key=True)  # Adicionando campo id
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)  # Você pode usar models.CharField para números de telefone
    cargo = models.ForeignKey(Cargo, on_delete=models.SET_NULL, null=True)    
    salario = models.DecimalField(max_digits=9, decimal_places=2)
    def __str__(self):
        return self.nome

class ProfissionalSaude(models.Model):
    funcionario = models.OneToOneField(Funcionarios, on_delete=models.CASCADE, primary_key=True)
    registro_cc = models.CharField(max_length=20)
    especialidade = models.ManyToManyField(Especialidade)

    def __str__(self):
        return self.funcionario.nome
