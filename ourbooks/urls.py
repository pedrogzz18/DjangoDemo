from django.urls import path, include

from . import views

urlpatterns = [
	path("", views.index, name="index"),
    path("signup/", views.SignupEditorial.as_view(), name="signup"),
    path("login-editorial/", views.EditorialLoginView.as_view(), name="login_editorial"),
]