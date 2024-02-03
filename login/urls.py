from django.urls import path, include
from login.views import tela_inicial, visualizar_consulta, consultas

urlpatterns = [
    path('tela_inicial/', tela_inicial, name="tela-inicial"),
    path('consultas/', consultas, name="consultas"),
    path('visualizar_consulta/', visualizar_consulta, name="visualizar-consulta"),
    path('', include('django.contrib.auth.urls')),  # Coloque isso no final das suas URLs
]
