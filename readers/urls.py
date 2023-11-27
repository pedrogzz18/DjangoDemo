from django.urls import path, include

from . import views

urlpatterns = [
    path('home/', views.ReaderHome.as_view(), name="reader_home"),
    path('books/<int:pk>', views.BookDetailView.as_view(), name="book_view"),
    path('profile/', views.ReaderUpdateView.as_view(), name="profile_view"),
    path('books/buy/<int:pk>', views.buy_book, name='buy_book'),
    path('mybooks/', views.MyBooksListView.as_view(), name='my_books'),
]