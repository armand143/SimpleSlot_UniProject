from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='Übersicht'),
    path('impressum/', views.impressum, name='Impressum'),
    path('new/', views.new, name='New'),
    path('edit/<cluster_id>', views.edit, name='edit'),
    path('delete/<todo_id>', views.delete, name='delete'),
    path('cls/', views.homepagestudis, name='homestudi'),
]
