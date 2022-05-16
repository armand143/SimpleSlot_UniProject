from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='Übersicht'),
    path('', views.impressum, name='Impressum'),
    path('', views.new, name='New'),
    path('', views.edit, name='Edit'),
    path('', views.index, name='Index'),
]