
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from consultas.models import Consultas

def tela_inicial(request):
    consultas = Consultas.objects.all()
    return render(request,'registration/tela-inicial.html', {'consultas': consultas})