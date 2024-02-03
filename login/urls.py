from django.urls import path
from login.views import user_login,index, tela_inicial, visualizar_consulta, consultas

urlpatterns = [
    path('', index, name='index'),
    path('autenticacao', user_login, name='login'),
    path('tela_inicial', tela_inicial, name="tela-inicial"),
    path('consultas', consultas, name="consultas"),
    path('visualizar_consulta', visualizar_consulta, name="visualizar-consulta"),
]