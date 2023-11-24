from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Editorial, Reader

class EditorialRegistrationForm(UserCreationForm):
    class Meta:
        model = Editorial
        fields = ['email', 'editorial_name', 'password1', 'password2']
        labels = {
            'email': 'Email',
            'editorial_name': 'Editorial name',
            'password1' : 'Password'
        }

class ReaderRegistrationForm(UserCreationForm):
    class Meta:
        model = Reader
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2']
        labels = {
            'email': 'Email',
            'first_name': 'Name',
            'last_name' : 'Last name',
            'username' : 'Username',
        }

class EditorialLoginForm(AuthenticationForm):
    username = UsernameField(label=("Email"), widget=forms.TextInput(attrs={"autofocus": True}))

    class Meta:
        model = Editorial
        labels = {
            'email' : 'email'
        }

class ReaderLoginForm(AuthenticationForm):
    class Meta:
        model = Reader
        fields = ['email']
        labels = {
            'email': 'Email'
        }