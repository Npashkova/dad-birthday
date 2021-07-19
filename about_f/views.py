from django.shortcuts import render
from .models import About
# Create your views here.


def home(request):
    posts = About.objects
    return render(request, 'about/home.html', {'posts': posts})