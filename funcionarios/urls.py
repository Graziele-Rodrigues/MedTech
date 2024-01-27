from django.urls import path
from funcionarios.views import lista_funcionarios, cria_funcionarios, edita_funcionarios, deleta_funcionarios

urlpatterns = [
    path('', lista_funcionarios, name='lista_funcionario'),
    path('new', cria_funcionarios, name='cria_funcionario'),
    path('update/<int:id>/', edita_funcionarios, name='edita_funcionario'),
    path('delete/<int:id>/', deleta_funcionarios, name='deleta_funcionario'),
]
