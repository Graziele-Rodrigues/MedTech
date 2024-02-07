from django.urls import path, include
from login.views import tela_inicial

urlpatterns = [
    path('tela_inicial/', tela_inicial, name="tela-inicial"),
    path('', include('django.contrib.auth.urls')),  # Coloque isso no final das suas URLs
]
