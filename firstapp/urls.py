from django.urls import path

from . import views
urlpatterns = [
    path('homepage/', views.homepage, name='Übersicht'),
    path('impressum/', views.impressum, name='Impressum'),
    path('new/', views.new, name='New'),
    path('edit/<cluster_id>', views.edit, name='edit'),
    path('deleteCluster/<cluster_id>', views.deleteCluster, name='deleteCluster'),
    path('deleteReservation/<cluster_id>', views.deleteReservation, name='deleteReservation'),
    path('cls/', views.homepagestudis, name='homestudi'),
    path('', views.loggingin, name='Login'),
    path('logout/', views.loggingout, name='Logout'),
    path('register/', views.register, name='Register'),
    path('editProfil/<user_id>', views.editProfil, name='EditProfil'),
    path('reservation/<cluster_id>/<user_id>', views.reservation, name='bookSlot'),
    path('myreservations/<user_id>', views.myreservation, name='MyReservations')
]
