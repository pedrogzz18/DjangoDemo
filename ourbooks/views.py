from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import EditorialRegistrationForm, ReaderRegistrationForm, EditorialLoginForm, ReaderLoginForm
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, "index.html")

class SignupEditorial(CreateView):
    form_class = EditorialRegistrationForm
    success_url = reverse_lazy('login-editorial/')
    template_name = 'registration/signup.html'

class EditorialLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('editorial-home/')
    authentication_form = EditorialLoginForm