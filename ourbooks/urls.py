from django.urls import path, include

from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path("signup/", views.SignupEditorial.as_view(), name="signup"),
    path("login-editorial/", views.EditorialLoginView.as_view(), name="login_editorial"),
    path("base/", views.editorial_view, name="editorial_home"),
    path('editorial/', views.editorial_view, name='editorial'),
    path('editorialBook/', views.editorial_add_book_view, name='addbook'),
    path('create/', views.create_book, name='create_book'),
]