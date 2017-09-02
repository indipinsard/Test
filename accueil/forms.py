from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")

    class Meta:
        model = User
        fields = ("username", "email",)

class LoginForm(forms.Form):
    username = forms.CharField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
