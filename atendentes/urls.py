from django.urls import path
from .views import lista_atendentes, cria_atendentes, edita_atendentes, deleta_atendentes

urlpatterns = [
    path('', lista_atendentes, name='lista_atendente'),
    path('new', cria_atendentes, name='cria_atendente'),
    path('update/<int:id>/', edita_atendentes, name='edita_atendente'),
    path('delete/<int:id>/', deleta_atendentes, name='deleta_atendente'),
]

