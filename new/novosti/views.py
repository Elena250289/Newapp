from django.shortcuts import render, redirect
# Обращаемся к моделям где таблица
from .models import Artiles
from .form import ArtilesForm
#Для динамических страниц
from django.views.generic import DetailView


def novosti_home(request):
    #выводим объекты в обратном порядке по названию
    novosti = Artiles.objects.order_by('-title')
    # Передадим объекты {'novosti': novosti} внутрь шаблона
    return render(request, 'novosti/novosti_home.html', {'novosti': novosti})

class NovostiDetailView(DetailView):
    model = Artiles
    template_name = 'novosti/details_view.html'
    context_object_name = 'artile'

def create(request):
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('novosti')
        else:
            error = 'Форма заполнена неверно'    
    

    form = ArtilesForm()
    
    return render(request, 'novosti/create.html', {'form': form})

