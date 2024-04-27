from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница'
    }  
    return render(request, 'posts/index.html', data)

def about(request):
    return render(request, 'posts/about.html')
# Create your views here.
