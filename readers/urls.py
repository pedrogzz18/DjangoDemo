from django.urls import path, include

from . import views

urlpatterns = [
    path('home/', views.ReaderHome.as_view(), name="reader_home"),
    path('home/filtered/<title>', views.reader_home_filtered, name="reader_home_filtered"),
    path('home/redirect/filtered/', views.redirect_home_filtered, name="filtered_redirect"),
    path('books/<int:pk>', views.BookDetailView.as_view(), name="book_view"),
    path('profile/', views.ReaderUpdateView.as_view(), name="profile_view"),
    path('books/buy/<int:pk>', views.buy_book, name='buy_book'),
    path('mybooks/', views.MyBooksListView.as_view(), name='my_books'),
    path('mybooks/share/<int:pk>', views.share_book, name='share_book'),
    path('shared-with-me/', views.SharedWithMeView.as_view(), name='shared_with_me'),
    path('logout/', views.logout_request, name='logout'),
    path('home/search/', views.search_books),
]