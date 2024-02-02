from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from pacientes.models import Paciente

def index(request):
    return render(request, 'login/index.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Use 'username' para pegar o campo de e-mail
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('login/tela-inicial.html') # Substitua 'tela_inicial' pelo nome da sua view

            else:
                form = AuthenticationForm()

                return render(request, 'login/index.html', {'form': form})

def tela_inicial(request):
    pacientes = Paciente.objects.all()
    return render(request,'login/tela-inicial.html', {'pacientes': pacientes})