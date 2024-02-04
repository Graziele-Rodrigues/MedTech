from django.urls import path
from registros.views import criar_registro, editar_registro, deletar_registro

urlpatterns = [
    path('criar_registro/<int:paciente_id>', criar_registro, name='criar_registro'),
    path('editar_registro/<int:registro_id> <int:paciente_id>/', editar_registro, name='editar_registro'),
    path('deletar_registro/<int:registro_id> <int:paciente_id>/', deletar_registro, name='deletar_registro'),
]
