from django.urls import path
from pacientes.views import index, criar_paciente, editar_paciente, delete_paciente

urlpatterns = [
    path('', index, name='index'),
    path('criar_paciente/', criar_paciente, name='criar_paciente'),
    path('editar_paciente/<int:paciente_id>/', editar_paciente, name='editar_paciente'),
    path('deletar_paciente/<int:paciente_id>/', delete_paciente, name='deletar_paciente'),
]