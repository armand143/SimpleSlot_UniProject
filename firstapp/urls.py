from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='Übersicht'),
    path('impressum/', views.impressum, name='Impressum'),
    path('new/', views.new, name='New'),
    path('edit/<str:title>/<int:deadline>/<int:percent>/', views.edit, name='Edit'),
    path('index/', views.index, name='Index'),
]