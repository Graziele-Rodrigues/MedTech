from django.shortcuts import render, redirect, get_object_or_404
from .models import RegistroMedico
from .forms import RegistroMedicoForm

def criar_registro(request, paciente_id):
    form = RegistroMedicoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('visualizar_paciente', paciente_id)
    return render(request, 'registros/criar_registro.html', {'form': form})

def editar_registro(request, registro_id, paciente_id):
    registro = get_object_or_404(RegistroMedico, pk=registro_id)
    form = RegistroMedicoForm(request.POST or None, instance=registro)

    if form.is_valid():
        form.save()
        return redirect('visualizar_paciente', paciente_id)
    return render(request, 'registros/editar_registro.html', {'form': form})

def deletar_registro(request, registro_id, paciente_id):
    registro = get_object_or_404(RegistroMedico, pk=registro_id)
    form = RegistroMedicoForm(request.POST or None, instance=registro)

    if request.method == 'POST':
        registro.delete()
        return redirect('visualizar_paciente', paciente_id)
    
    return render(request, 'registros/deletar_registro.html', {'form': form})