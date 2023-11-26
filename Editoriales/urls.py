from django.urls import path, include

from . import views

urlpatterns = [
    path("base/", views.editorial_view, name="editorial_home"),
    path('editorial/', views.editorial_view, name='editorial'),
    path('editorialBook/', views.editorial_add_book_view, name='addbook'),
    path('create/', views.create_book, name='create_book'),
]