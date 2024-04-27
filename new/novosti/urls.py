from django.urls import path
from . import views

urlpatterns = [
    path('', views.novosti_home, name='novosti_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.NovostiDetailView.as_view(), name='novosti_detail'),
    
]