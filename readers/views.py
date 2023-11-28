from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from ourbooks.views import reader_check
# Create your views here.

@user_passes_test(reader_check)
def reader_home(request):
    return render(request, 'readers/reader-home.html')