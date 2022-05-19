from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='Übersicht'),
    path('impressum/', views.impressum, name='Impressum'),
    path('new/', views.new, name='New'),
    path('edit/<todo_id>', views.edit, name='edit'),
    path('', views.index, name='Index'),
    
    
]
