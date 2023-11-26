from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Editorial, Reader, CustomUser

class CustomUserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

class EditorialRegistrationForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = ['editorial_name']
        labels = {
            'editorial_name': 'Editorial name'
        }

class ReaderRegistrationForm(forms.ModelForm):
    class Meta:
        model = Reader
        fields = ['first_name', 'last_name', 'username']