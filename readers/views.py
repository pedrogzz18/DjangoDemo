from typing import Any
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.http import HttpResponseBadRequest
from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from ourbooks.views import reader_check
from ourbooks.models import Reader, Editorial
from Editoriales.models import Books
from readers.models import Purchase, Share, OwnerShare, Review 
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
import datetime
import json
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.utils import timezone
from readers.forms import ReviewForm
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

@user_passes_test(reader_check)
def reader_home_filtered(request, title):
    print(title)
    books = Books.objects.filter(book_name=title)
    return render(request, 'readers/reader-home-filtered.html', {'Books' : books})

@user_passes_test(reader_check)
def redirect_home_filtered(request):
    title = request.GET.get("title")
    return redirect('reader_home_filtered', title)

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

            context['reviews'] = Review.objects.filter(book=self.get_object())
            
            return context
    
   
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = self.object
            review.reader = request.user.reader
            review.date = timezone.now()
            review.save()
            return redirect('book_view', pk=self.object.pk)
        else:
            # Si el formulario no es válido, renderizar la página con el formulario y errores
            context = self.get_context_data(form=form)
            return render(request, self.template_name, context)

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
    template_name = 'readers/shared-with-me.html'
    context_object_name = 'Shares'
    fields = ['book']

    def get_queryset(self):
        #filtrate by user
        return Share.objects.filter(reader=get_reader(self.request))

@user_passes_test(reader_check)
def share_book(request, pk):
    book = Books.objects.get(pk=pk)
    #get username from request
    data = json.loads(request.body)
    receptor_username = data['username']
    try:
        receptor = Reader.objects.get(username=receptor_username)
        share = Share(reader=receptor, book=book)
        share.save()
        owner_share = OwnerShare(share=share, book_owner=request.user.reader)
        owner_share.save()
        return redirect('book_view', pk)
    except Reader.DoesNotExist:
        response_data = {'status': 'Error', 'message': 'User does not exist'}
        return JsonResponse(response_data)

@user_passes_test(reader_check)
def logout_request(request):
    logout(request)
    return redirect('/accounts/login')

# search/?title=
def search_books(request):
    title = request.GET.get('title')
    if(title == None):
        return JsonResponse({'status' : 200, 'data' : []})
    books = Books.objects.filter(book_name__icontains=title)
    payload = []

    for book in books:
        payload.append(book.book_name)
    return JsonResponse({'status' : 200, 'data' : payload})


@login_required
def my_reviews(request):
    reader_profile = get_object_or_404(Reader, user=request.user)
    user_reviews = Review.objects.filter(reader=reader_profile).select_related('book').order_by('-date')
    paginator = Paginator(user_reviews, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'readers/my-reviews.html', {'page_obj': page_obj})

def edit_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)  # Corrección aquí
        if form.is_valid():
            form.save()
        return redirect('my-reviews')    
    else:
        form = ReviewForm(instance=review)
    return render(request, 'readers/edit_review.html', {'form': form})
    


def delete_review(request, pk):
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        review.delete()
        return redirect('my-reviews')
    return render(request, 'readers/delete_review.html', {'review': Review})
