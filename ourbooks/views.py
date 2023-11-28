from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .forms import EditorialRegistrationForm, ReaderRegistrationForm, CustomUserRegistrationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser, Editorial, Reader
# Create your views here.
def index(request):
    return render(request, "index.html")

def editorial_check(user):
    if hasattr(user, 'editorial'):
            return True
    return False

def reader_check(user):
    if hasattr(user, 'reader'):
            return True
    return False

def editorial_registration(request):
    if request.method == 'POST':
        editorial_form = EditorialRegistrationForm(request.POST)
        user_form = CustomUserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            editorial_profile = editorial_form.save(commit=False)
            editorial_profile.user = user
            editorial_profile.save()
            return redirect(reverse_lazy('login'))
    else:
        editorial_form = EditorialRegistrationForm()
        user_form = CustomUserRegistrationForm()

    return render(request, 'registration/signup-editorial.html', {'user_form': user_form, 'editorial_form' : editorial_form})

def reader_registration(request):
    if request.method == 'POST':
        reader_form = ReaderRegistrationForm(request.POST)
        user_form = CustomUserRegistrationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            reader_profile = reader_form.save(commit=False)
            reader_profile.user = user
            reader_profile.save()
            return redirect(reverse_lazy('login'))
    else:
        reader_form = ReaderRegistrationForm()
        user_form = CustomUserRegistrationForm()

    return render(request, 'registration/signup-reader.html', {'user_form': user_form, 'reader_form' : reader_form})

@login_required
def redirect_home(request):
    if request.user.is_authenticated:
        if hasattr(request.user, 'editorial'):
            return redirect('/Editoriales/home')
        elif hasattr(request.user, 'reader'):
            return redirect('/readers/home')
    else:
        return redirect('/accounts/login')
    

