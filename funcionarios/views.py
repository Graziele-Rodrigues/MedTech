from django.shortcuts import render, redirect

from .models import Funcionarios, ProfissionalSaude
from .forms import FuncionariosForm, ProfissionalSaudeForm


def lista_funcionarios(request):
    funcionarios = Funcionarios.objects.all()
    return render(request, 'funcionarios/funcionarios.html', {'funcionarios': funcionarios})


def cria_funcionarios(request):
    funcionarios_form = FuncionariosForm(request.POST or None)
    profissional_saude_form = ProfissionalSaudeForm(request.POST or None)

    if request.method == 'POST':
            if funcionarios_form.is_valid():
                funcionarios = funcionarios_form.save()

            # Verifica se o cargo é "atendente"
            if funcionarios.cargo.nome.lower() == 'atendente':
                # Se for atendente, não precisa preencher os campos do ProfissionalSaude
                funcionarios.save()
                return redirect('lista_funcionario')
            
            # Se não for atendente, continua com a validação e salvamento do ProfissionalSaudeForm
            if profissional_saude_form.is_valid():
                profissional_saude_form.instance.funcionario = funcionarios
                profissional_saude_form.save()
                return redirect('lista_funcionario')
            return redirect('lista_funcionario')

    return render(
        request,
        'funcionarios/funcionarios-form-create.html',
        {'funcionarios_form': funcionarios_form, 'profissional_saude_form': profissional_saude_form}
    )

def edita_funcionarios(request, id):
    funcionarios = Funcionarios.objects.get(id=id)
    funcionarios_form = FuncionariosForm(request.POST or None, instance=funcionarios)
    profissional_saude_form = None

    try:
        profissionalSaude = ProfissionalSaude.objects.get(funcionario=funcionarios)
        profissional_saude_form = ProfissionalSaudeForm(request.POST or None, instance=profissionalSaude)
    except ProfissionalSaude.DoesNotExist:
        # Se não existir, cria uma instância vazia do ProfissionalSaude
        profissionalSaude = None

    if request.method == 'POST':
        if funcionarios_form.is_valid():
            funcionarios = funcionarios_form.save()

            # Verifica se o cargo é "atendente"
            if funcionarios.cargo.nome.lower() == 'atendente':
                # Se for atendente, não precisa preencher os campos do ProfissionalSaude
                return redirect('lista_funcionario')
                
            # Se não for atendente, continua com a validação e salvamento do ProfissionalSaudeForm
            if profissional_saude_form.is_valid():
                profissional_saude_form.instance.funcionario = funcionarios
                profissional_saude_form.save()
                return redirect('lista_funcionario')

    return render(
        request,
        'funcionarios/funcionarios-form-edit.html',
        {'funcionarios_form': funcionarios_form, 'profissional_saude_form': profissional_saude_form, 'funcionarios': funcionarios}
    )


def deleta_funcionarios(request, id):
    funcionarios = Funcionarios.objects.get(id=id)

    if request.method == 'POST':
        funcionarios.delete()
        return redirect('lista_funcionario')

    return render(request, 'funcionarios/delete-confirm.html', {'funcionarios': funcionarios})
