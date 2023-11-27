from typing import Any
from django.urls import reverse
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from ourbooks.views import reader_check
from ourbooks.models import Reader, Editorial
from Editoriales.models import Books
from readers.models import Purchase, Share, OwnerShare
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import logout
import datetime
# Create your views here.

@user_passes_test(reader_check)
def get_reader(request):
    user = request.user
    reader = user.reader
    return reader

@method_decorator(user_passes_test(reader_check), name='dispatch')
class ReaderHome(ListView):
    model = Books
    template_name = 'readers/reader-home.html'
    context_object_name = 'Books'


    def get(self, request, *args, **kwargs):
        self.reader = get_reader(request)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        # Obtener el contexto base llamando al método de la clase base
        context = super().get_context_data(**kwargs)
        
        # Agregar datos adicionales al contexto
        context['reader'] = self.reader

        return context



@method_decorator(user_passes_test(reader_check), name='dispatch')
class BookDetailView(DetailView):
    model = Books
    template_name = 'readers/book-view.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
            # Add additional context variables here
            context = super().get_context_data(**kwargs)
            candidate = Purchase.objects.filter(reader=self.request.user.reader, book=self.kwargs['pk'])
            context['purchased'] = False
            if(candidate.exists()):
                context['purchased'] = True
            
            candidate = Share.objects.filter(reader=self.request.user.reader, book=self.kwargs['pk'])
            context['shared'] = False
            if(candidate.exists()):
                context['shared'] = True
            return context

@method_decorator(user_passes_test(reader_check), name='dispatch')
class ReaderUpdateView(UpdateView):
    model = Reader
    template_name = 'readers/reader-profile.html'
    context_object_name = 'user'
    success_url = reverse_lazy('reader_home')
    fields = ['first_name', 'last_name', 'username']
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        self.kwargs['pk'] = self.request.user.reader.id
        pk = self.kwargs.get('pk')
        return self.model.objects.get(pk=pk)

@user_passes_test(reader_check)
def buy_book(request, pk):
    book = Books.objects.get(pk=pk)
    purchase = Purchase(reader=request.user.reader, book=book, date=datetime.date.today())
    purchase.save()
    # Redirect to the generated URL
    return redirect('book_view', pk)

@method_decorator(user_passes_test(reader_check), name='dispatch')
class MyBooksListView(ListView):
    model = Purchase
    template_name = 'readers/reader-books.html'
    context_object_name = 'Purchases'
    fields = ['book']

    def get_queryset(self):
        #filtrate by user
        return Purchase.objects.filter(reader=get_reader(self.request))
    
@method_decorator(user_passes_test(reader_check), name='dispatch')
class SharedWithMeView(ListView):
    model = Share
    template_name = 'readers/reader-books.html'
    context_object_name = 'Shares'
    fields = ['book']

    def get_queryset(self):
        #filtrate by user
        return Share.objects.filter(reader=get_reader(self.request))

@user_passes_test(reader_check)
def logout_request(request):
    logout(request)
    return redirect('/accounts/login')