from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect


urlpatterns = [
    path('', lambda request: redirect('login/', permanent=False)),
    path('funcionarios/', include('funcionarios.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('consultas/', include('consultas.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('registros/', include('registros.urls')),
    path('', include('login.urls')),
    path('admin/', admin.site.urls),
]
