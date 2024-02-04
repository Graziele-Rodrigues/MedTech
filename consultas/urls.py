from django.urls import path
from consultas.views import consultas, criar_consulta, editar_consulta, visualizar_consulta, deletar_consulta

urlpatterns = [
    path('consultas/', consultas, name='consultas'),
    path('criar_consulta/', criar_consulta, name='criar_consulta'),
    path('editar_consulta/<int:consulta_id>/', editar_consulta, name='editar_consulta'),
    path('visualizar_consulta/<int:consulta_id>/', visualizar_consulta, name='visualizar_consulta'),
    path('deletar_consulta/<int:consulta_id>/', deletar_consulta, name='deletar_consulta'),
]