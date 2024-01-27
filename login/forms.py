from django import forms
# from .models import Funcionario

class LoginForm(forms.ModelForm):
    class Meta:
        # model =  Funcionario
        fields = ['email', 'senha']