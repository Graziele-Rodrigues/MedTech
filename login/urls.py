from django.urls import path
from login.views import user_login,index

urlpatterns = [
    path('', index, name='index'),
    path('autenticacao/', user_login, name='login'),
]