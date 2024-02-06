from django.urls import path
from consultas.views import consultas, criar_consulta, editar_consulta, visualizar_consulta, deletar_consulta

urlpatterns = [
    path('', consultas, name='consultas'),
    path('criar-consulta/', criar_consulta, name='criar-consulta'),
    path('editar-consulta/<int:consulta_id>/', editar_consulta, name='editar-consulta'),
    path('visualizar-consulta/<int:consulta_id>/', visualizar_consulta, name='visualizar-consulta'),
    path('deletar-consulta/<int:consulta_id>/', deletar_consulta, name='deletar-consulta'),
]