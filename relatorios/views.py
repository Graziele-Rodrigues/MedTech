from django.shortcuts import render
from django.http import HttpResponse
from excel_response import ExcelResponse
from pacientes.models import Paciente
from consultas.models import Consultas
from funcionarios.models import Funcionarios, ProfissionalSaude


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
    profissionais_saude = ProfissionalSaude.objects.all()
    dados_para_excel = [
        {
            'Nome': profissional.funcionario.nome,
            'Telefone': profissional.funcionario.telefone,
            'Cargo': profissional.funcionario.cargo.nome,
            'Salário': profissional.funcionario.salario,
            'Registro CC': profissional.registro_cc,
            'Especialidade': ', '.join([especialidade.nome for especialidade in profissional.especialidade.all()])
        } 
        for profissional in profissionais_saude
    ]
    response = ExcelResponse(dados_para_excel, 'relatorio_profissional_saude')
    response['Content-Disposition'] = 'attachment; filename=dados.xlsx'
    return response

def relatorio_atendentes(request):
    dados = Funcionarios.objects.filter(cargo__nome="atendente").all()
    dados_para_excel = [
        {'Nome': objeto.nome, 'Telefone': objeto.telefone, 'Cargo': objeto.cargo.nome, 'Salário': objeto.salario} for objeto in dados
    ]
    response = ExcelResponse(dados_para_excel, 'relatorio_atendentes')
    response['Content-Disposition'] = 'attachment; filename=dados.xlsx'
    return response

def relatorio_consultas(request):
    dados = Consultas.objects.all()
    dados_para_excel = [
        {'Nome': objeto.paciente.nome, 'Telefone': objeto.paciente.telefone, 'Telefone secundário': objeto.telefone_secundario, 'Data de nascimento': objeto.data_nascimento, 'Plano de saúde': objeto.plano_saude, 'Endereço':objeto.endereco} for objeto in dados
    ]
    response = ExcelResponse(dados_para_excel, 'relatorio_pacientes')
    response['Content-Disposition'] = 'attachment; filename=dados.xlsx'
    return response
