from django.urls import path
from images import views as views

urlpatterns = [
    path('', views.index, name='index'),
    path('bulk', views.bulk, name='bulk'),
    path('api/random', views.random, name='random')
]
