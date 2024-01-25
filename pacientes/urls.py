from django.urls import path
from pacientes.views import index

urlpatterns = [
    path('', index),
]