from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'login/index.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
<<<<<<< Updated upstream
            email = form.cleaned_data.get('username')  # Use 'username' para pegar o campo de e-mail
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('tela_inicial')  # Substitua 'tela_inicial' pelo nome da sua view

    else:
        form = AuthenticationForm()

    return render(request, 'login/index.html', {'form': form})
=======
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']

            #  try:
            #     usuario = Usuario.objects.get(email=email_fornecido)
            #     return JsonResponse({'existe': True, 'usuario_nome': usuario.nome})
            # except Usuario.DoesNotExist:
            #     return JsonResponse({'existe': False})
            # Validar se senha corresponde ao email
            return render(request, 'login/tela-inicial.html')
        else:
            # O formulário não é válido, exception
            return render(request, 'login/index.html')
>>>>>>> Stashed changes
