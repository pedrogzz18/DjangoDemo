from django.urls import path, include

from . import views

urlpatterns = [
    path('editorial/', views.editorial_home, name='editorial'),
    path('editorialBook/', views.editorial_add_book_view, name='addbook'),
    path('create/', views.create_book, name='create_book'),
    path('home/', views.editorial_home, name="editorial_home"),
    path('book/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),
    path('book/<int:pk>/update/', views.BookUpdateView.as_view(), name = 'update_book'),
]