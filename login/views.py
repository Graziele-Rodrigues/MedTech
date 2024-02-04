
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from pacientes.models import Paciente

def tela_inicial(request):
    pacientes = Paciente.objects.all()
    return render(request,'registration/tela-inicial.html', {'pacientes': pacientes})

# FUNÇÕES APENAS PARA CRIAÇÃO DO FRONT-END
def consultas(request):
    return render(request, 'consultas/consultas.html')

def visualizar_consulta(request):
    return render(request, 'consultas/visualizar-consulta.html')