from django.shortcuts import render, redirect

from .models import Funcionarios
from .forms import FuncionariosForm


def lista_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    return render(request, 'funcionarios/funcionarios.html', {'funcionarios': funcionarios})


def cria_funcionarios(request):
    form = FuncionariosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_funcionario')

    return render(request, 'funcionarios/funcionarios-form.html', {'form': form})


def edita_funcionarios(request, id):
    funcionarios = Funcionarios.objects.get(id=id)
    form = FuncionariosForm(request.POST or None, instance=funcionarios)

    if form.is_valid():
        form.save()
        return redirect('lista_funcionario')

    return render(request, 'funcionarios/funcionarios-form.html', {'form': form, 'funcionarios': funcionarios})


def deleta_funcionarios(request, id):
    funcionarios = Funcionarios.objects.get(id=id)

    if request.method == 'POST':
        funcionarios.delete()
        return redirect('lista_funcionario')

    return render(request, 'funcionarios/delete-confirm.html', {'funcionarios': funcionarios})