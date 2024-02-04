from django.shortcuts import render
from django.http import HttpResponse
from excel_response import ExcelResponse
from pacientes.models import Paciente
from funcionarios.models import Funcionarios


def relatorios(request):
    return render(request, 'relatorios/relatorios.html')

def relatorio_pacientes(request):
    dados = Paciente.objects.all()
    dados_para_excel = [
        {'Nome': objeto.nome, 'Telefone': objeto.telefone, 'Telefone secundário': objeto.telefone_secundario, 'Data de nascimento': objeto.data_nascimento, 'Plano de saúde': objeto.plano_saude, 'Endereço':objeto.endereco} for objeto in dados
    ]
    response = ExcelResponse(dados_para_excel, 'relatorio_pacientes')
    response['Content-Disposition'] = 'attachment; filename=dados.xlsx'
    return response

def relatorio_profissional_saude(request):
    # dados = Funcionarios.objects.filter(name="Profissional da Saúde").all()
    dados = Funcionarios.objects.all() # Objeto para testes apenas
    dados_para_excel = [
        {'Nome': objeto.nome, 'Telefone': objeto.telefone, 'Cargo': objeto.cargo, 'Salário': objeto.salario, 'Registro CC': objeto.registro_cc, 'Especialidade': objeto.especialidade} for objeto in dados
    ]
    response = ExcelResponse(dados_para_excel, 'relatorio_profissional_saude')
    response['Content-Disposition'] = 'attachment; filename=dados.xlsx'
    return response

def relatorio_atendentes(request):
    # dados = Funcionarios.objects.filter(name="Atendente").all()
    dados = Funcionarios.objects.all() # Objeto para testes apenas
    dados_para_excel = [
        {'Nome': objeto.nome, 'Telefone': objeto.telefone, 'Cargo': objeto.cargo, 'Salário': objeto.salario} for objeto in dados
    ]
    response = ExcelResponse(dados_para_excel, 'relatorio_atendentes')
    response['Content-Disposition'] = 'attachment; filename=dados.xlsx'
    return response

def relatorio_consultas(request):
    dados = Paciente.objects.all()
    dados_para_excel = [
        {'Nome': objeto.nome, 'Telefone': objeto.telefone, 'Telefone secundário': objeto.telefone_secundario, 'Data de nascimento': objeto.data_nascimento, 'Plano de saúde': objeto.plano_saude, 'Endereço':objeto.endereco} for objeto in dados
    ]
    response = ExcelResponse(dados_para_excel, 'relatorio_pacientes')
    response['Content-Disposition'] = 'attachment; filename=dados.xlsx'
    return response
