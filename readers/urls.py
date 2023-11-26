from django.urls import path, include

from . import views

urlpatterns = [
    path('home/', views.ReaderHome.as_view(), name="reader_home"),
    path('books/<int:pk>', views.BookDetailView.as_view(), name="book_view"),
]