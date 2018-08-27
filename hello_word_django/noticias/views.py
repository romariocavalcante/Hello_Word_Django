from django.shortcuts import render
from .models import *

def home(request):
    list = noticias.objects.all
    return render(request, 'lista.html', {'list': list})

