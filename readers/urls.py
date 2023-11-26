from django.urls import path, include

from . import views

urlpatterns = [
    path('home/', views.reader_home, name="reader_home"),
]