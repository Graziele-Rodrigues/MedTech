from django.urls import path
from login.views import user_login,index, tela_inicial

urlpatterns = [
    path('', index, name='index'),
    path('autenticacao', user_login, name='login'),
    path('tela_inicial', tela_inicial, name="tela-inicial"),
]