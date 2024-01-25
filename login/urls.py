from django.urls import path
from login.views import index

urlpatterns = [
    path('', index),
]