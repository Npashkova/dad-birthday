from django.shortcuts import render
from .models import Wish
# Create your views here.


def wish(request):
    wishes = Wish.objects
    return render(request, 'wishes/wishes.html', {'wishes': wishes})