from django.urls import path

from . import views
urlpatterns = [
    path('homepage/', views.homepage, name='Übersicht'),
    path('impressum/', views.impressum, name='Impressum'),
    path('new/', views.new, name='New'),
    path('edit/<cluster_id>', views.edit, name='edit'),
    path('delete/<cluster_id>', views.deletee, name='delete'),
    path('cls/', views.homepagestudis, name='homestudi'),
    path('', views.loggingin, name='Login'),
    path('logout/', views.loggingout, name='Logout'),
    path('register/', views.register, name='Register'),
    path('editProfil/<user_id>', views.editProfil, name='EditProfil'),
    path('book/<cluster_id>', views.book, name='book'),
    path('respage/', views.ResPage, name='ResPage'),
    path('book/<date_id>', views.book_slots, name='book_slots'),
    path('book/<str:slot_value>/<str:date_value>/<int:clust_id>', views.update_slots, name='update_slots'),
    path('reservation/', views.reservation, name='bookSlot'),
]
