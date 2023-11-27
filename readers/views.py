from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from ourbooks.views import reader_check
from ourbooks.models import Reader, Editorial
from Editoriales.models import Books
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import logout
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

@method_decorator(user_passes_test(reader_check), name='dispatch')
class ReaderUpdateView(UpdateView):
    model = Reader
    template_name = 'readers/reader-profile.html'
    context_object_name = 'user'
    success_url = reverse_lazy('reader_home')
    fields = '__all__'
    pk_url_kwarg = 'pk'
    
    def get_object(self, queryset=None):
        self.kwargs['pk'] = self.request.user.reader.id
        pk = self.kwargs.get('pk')
        print(pk)
        return self.model.objects.get(pk=pk)