from django.urls import path, include

from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path('signup-editorial/', views.editorial_registration, name="signup_editorial"),
    path('signup-reader/', views.reader_registration, name="signup_reader"),
    path('home/', views.redirect_home, name="redirect_home"),
]