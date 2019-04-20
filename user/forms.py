from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegestrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2', 'first_name', 'last_name']
