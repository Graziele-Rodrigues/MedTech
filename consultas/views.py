from django.shortcuts import render, redirect, get_object_or_404
from .models import Consultas
from .forms import ConsultaForm

def atendente(user):
    return user.groups.filter(name='atendente').exists()

def profissionalSaude(user):
    return user.groups.filter(name='profissional saude').exists()

def consultas(request):
    usuario_autenticado_atendente = atendente(request.user)
    consultas = Consultas.objects.all()
    return render(request, 'consultas/consultas.html', {'consultas': consultas, 'usuario_autenticado_atendente': usuario_autenticado_atendente})

def criar_consulta(request):
    if request.method == 'POST':
        consultas_form = ConsultaForm(request.POST)
        consultas_form.instance.status = 'agendada'
        if consultas_form.is_valid():
            consultas_form.save()
            return redirect('consultas')
    else:
        consultas_form = ConsultaForm()
    return render(request, 'consultas/criar-consulta.html',{'consultas_form': consultas_form})

def visualizar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consultas, pk=consulta_id)
    return render(request, 'consultas/visualizar-consulta.html', {'consulta': consulta})

def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consultas, pk=consulta_id)

    if request.method == 'POST':
        consultas_form = ConsultaForm(request.POST, instance=consulta)
        if consultas_form.is_valid:
            consultas_form.save()
            return redirect('consultas')
    else:
        consultas_form = ConsultaForm(instance=consulta)

    return render(request, 'consultas/editar-consulta.html', {'consultas_form': consultas_form, 'consulta': consulta})

def deletar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consultas, pk=consulta_id)

    if request.method == 'POST':           
        consulta.delete()
        return redirect('consultas')
 
    return render(request, 'consultas/deletar-consulta.html', {'consulta': consulta})