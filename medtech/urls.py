from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('funcionarios/', include('funcionarios.urls')),
    path('pacientes/', include('pacientes.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
]
