from django.shortcuts import render
from .forms import LoginForm

def index(request):
    return render(request, 'login/index.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            # Validar se senha corresponde ao email
            return render(request, 'login/tela-inicial.html')
        else:
            # O formulário não é válido, exception
            return render(request, 'login/index.html')