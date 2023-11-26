from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from ourbooks.views import reader_check
from ourbooks.models import Reader, Editorial
from Editoriales.models import Books
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse
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
class BookDetailView(View):
    template_name = 'book-view.html'

    def get(self, request, pk):
        book = get_object_or_404(Books, pk=pk)
        return render(request, 'readers/book-view.html', {'book' : book})