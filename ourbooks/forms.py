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

class BookForm(forms.Form):
    book_name = forms.CharField(label = 'Book Name', max_length = 100)
    pages = forms.IntegerField(label = 'Number of Pages')
    publication_year = forms.CharField(label = "Publication Year", max_length=20)
    description = forms.CharField(label = 'Description', max_length=300,widget=forms.Textarea)
    image_url = forms.CharField(label = "Image URL", max_length=250)
    author_first_name = forms.CharField(label = "Author First Name", max_length=40)
    author_last_name = forms.CharField(label = "Author Last Name", max_length=40)