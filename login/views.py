from django.shortcuts import render
from .models import Pictures

# Create your views here.
def home(request):
    blogs = Pictures.objects
    return render(request, 'login/home.html', {'blogs': blogs}) 