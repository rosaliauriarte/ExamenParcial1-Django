from .models import Usuario
from django.contrib.auth.forms import UserCreationForm
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario",
                               widget=forms.TextInput(attrs={'placeholder': 'inicio de sesion'}))
    password = forms.CharField(widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model=Usuario
        fields =['username', 'full_name', 'email', 'password1', 'password2']
