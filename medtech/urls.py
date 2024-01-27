from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('atendentes/', include('atendentes.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
]
