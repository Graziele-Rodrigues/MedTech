from django.urls import path
from relatorios.views import relatorios,relatorio_pacientes, relatorio_profissional_saude, relatorio_atendentes, relatorio_consultas

urlpatterns = [
    path('', relatorios, name="relatorios"),
    path('pacientes', relatorio_pacientes, name="relatorio_pacientes"),
    path('profissional-saude', relatorio_profissional_saude, name="relatorio_profissional_saude"),
    path('funcionarios', relatorio_atendentes, name="relatorio_atendentes"),
    path('consultas', relatorio_consultas, name="relatorio_consultas"),
]
