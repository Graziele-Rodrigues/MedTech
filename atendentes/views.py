from django.shortcuts import render, redirect

from .models import Atendentes
from .forms import AtendentesForm


def lista_atendentes(request):
    atendentes = Atendentes.objects.all()
    return render(request, 'atendentes/atendentes.html', {'atendentes': atendentes})


def cria_atendentes(request):
    form = AtendentesForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_atendentes')

    return render(request, 'atendentes/atendentes-form.html', {'form': form})


def edita_atendentes(request, id):
    atendentes = Atendentes.objects.get(id=id)
    form = AtendentesForm(request.POST or None, instance=atendentes)

    if form.is_valid():
        form.save()
        return redirect('lista_atendente')

    return render(request, 'atendentes/atendentes-form.html', {'form': form, 'atendentes': atendentes})


def deleta_atendentes(request, id):
    atendentes = Atendentes.objects.get(id=id)

    if request.method == 'POST':
        atendentes.delete()
        return redirect('lista_atendente')

    return render(request, 'atendentes/delete-confirm.html', {'atendentes': atendentes})