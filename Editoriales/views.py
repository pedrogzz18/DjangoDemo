from django.shortcuts import render
from .forms import BookForm
from .models import Books

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
            book.editorial_mail = request.user
            # Here, you can save the data to your database or perform other actions
            # For demonstration purposes, let's just print the data
            
            book.save()
            #print(f'Book Name: {book_name}, Description: {description}, pages: {pages}')
            print(book.editorial_mail)
            # Redirect to a success page or render a new template
            my_books = Books.objects.filter(editorial_mail = request.user)
            return render(request, 'EditorialSite/base.html', {'my_books':my_books})
    else:
        form = BookForm()

    return render(request, 'AddBook.html', {'form': form})

def editorial_view(request):
    my_books = Books.objects.filter(editorial_mail = request.user)
    return render(request, "base.html", {'my_books': my_books})

def editorial_add_book_view(request):
    form = BookForm(request.POST)
    
    return render(request, "AddBook.html", {'form': form})