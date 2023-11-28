from django.shortcuts import render
from .forms import BookForm
from .models import Books
from ourbooks.views import editorial_check
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
def create_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # Process the form data
            book = Books()
            book.book_name = form.cleaned_data['book_name']
            book.description = form.cleaned_data['description']
            book.pages = form.cleaned_data['pages']
            book.publication_year = form.cleaned_data['publication_year']
            book.image_url = form.cleaned_data['image_url']
            book.author_first_name = form.cleaned_data['author_first_name']
            book.author_last_name = form.cleaned_data['author_last_name']
            book.ISBN = form.cleaned_data['ISBN']
            book.editorial_mail = request.user.email
            book.price = form.cleaned_data['price']
            # Here, you can save the data to your database or perform other actions
            # For demonstration purposes, let's just print the data
            
            book.save()
            #print(f'Book Name: {book_name}, Description: {description}, pages: {pages}')
            print(book.editorial_mail)
            # Redirect to a success page or render a new template
            my_books = Books.objects.filter(editorial_mail = request.user.email)
            return render(request, 'editoriales-home.html', {'my_books':my_books})
    else:
        form = BookForm()
        return render(request, 'AddBook.html', {'form': form})
    


def editorial_add_book_view(request):
    form = BookForm(request.POST)
    
    return render(request, "AddBook.html", {'form': form})


@user_passes_test(editorial_check)
def editorial_home(request):
    my_books = Books.objects.filter(editorial_mail = request.user)
    return render(request, 'editoriales-home.html',{'my_books': my_books})

class BookDeleteView(DeleteView):
    model = Books
    success_url = reverse_lazy('editorial_home')
    template_name = 'book_delete_confirmation.html'

class BookUpdateView(UpdateView):
    model = Books
    fields = ['book_name', 'pages', 'price','publication_year', 'description', 'image_url', 'author_first_name', 'author_last_name']
    template_name = 'books_form.html'
    success_url = reverse_lazy('editorial_home')