from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('login.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('admin/', admin.site.urls),
]
