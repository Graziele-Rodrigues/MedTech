from django.shortcuts import render, get_object_or_404
from .models import Paciente
from .forms import PacienteForm
from django.shortcuts import redirect

def index(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/index.html', {'pacientes': pacientes})

def criar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para a página inicial
    else:
        form = PacienteForm()

    return render(request, 'pacientes/criar_paciente.html', {'form': form})

def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('index') 
    else:
        form = PacienteForm(instance=paciente)

    return render(request, 'pacientes/editar_paciente.html', {'form': form, 'paciente': paciente})

def delete_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, pk=paciente_id)

    if request.method == 'POST':
        paciente.delete()
        return redirect('index') 

    return render(request, 'pacientes/delete_paciente.html', {'paciente': paciente})
