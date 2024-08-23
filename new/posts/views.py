from django.shortcuts import render
from django.http import HttpResponseNotFound


def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'posts/index.html', data)


def about(request):
    return render(request, 'posts/about.html')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
