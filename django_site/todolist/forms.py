from django import forms
from django.contrib.auth.forms import UserCreationForm
from todolist.models import User


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
