from django.shortcuts import render, get_object_or_404
from .models import Paciente
from registros.models import RegistroMedico
from .forms import PacienteForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test


def atendente(user):
    return user.groups.filter(name='atendente').exists()

def profissionalSaude(user):
    return user.groups.filter(name='profissional saude').exists()

def index(request):
    usuario_autenticado_atendente = atendente(request.user)
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/index.html', {'pacientes': pacientes, 'usuario_autenticado_atendente': usuario_autenticado_atendente})

@user_passes_test(atendente)
def criar_paciente(request):
    if request.method == 'POST':
        pacientes_form = PacienteForm(request.POST)
        if pacientes_form.is_valid():
            pacientes_form.save()
            return redirect('index')  # Redireciona para a página inicial
    else:
        pacientes_form = PacienteForm()

    return render(request, 'pacientes/criar_paciente.html', {'pacientes_form': pacientes_form})

@user_passes_test(atendente)
def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    if request.method == 'POST':
        pacientes_form = PacienteForm(request.POST, instance=paciente)
        if pacientes_form.is_valid():
            pacientes_form.save()
            return redirect('index') 
    else:
        pacientes_form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/editar_paciente.html', {'pacientes_form': pacientes_form, 'paciente': paciente})

@user_passes_test(atendente)
def delete_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    if request.method == 'POST':
        paciente.delete()
        return redirect('index')

    return render(request, 'pacientes/delete_paciente.html', {'paciente': paciente})

def visualizar_paciente(request, paciente_id):
    usuario_autenticado_profissional = profissionalSaude(request.user)
    paciente = get_object_or_404(Paciente, pk=paciente_id)
    registros = RegistroMedico.objects.filter(paciente__id=paciente_id)
    return render(request, 'pacientes/visualizar_paciente.html', {'paciente': paciente, 'registros': registros, 'usuario_autenticado_profissional': usuario_autenticado_profissional})
