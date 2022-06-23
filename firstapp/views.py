from cmath import pi
from collections import UserDict
from multiprocessing import context
from sqlite3 import Date
from tkinter import Entry
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Cluster, Nutzer, Reservation
from .forms import ClusterForm, RegisterForm, ReservationForm, DateInput
import firstapp

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from firstapp import models
from django.db.models import Q
from django.db import IntegrityError
from django.views.generic.edit import CreateView
#from django.utils import simplejson as json
import json
from django.forms.models import model_to_dict


def loggingin(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user) 
            if username == 'admin':
                return redirect('Übersicht')
            else:
                return redirect('homestudi')
        else:
            messages.error(request, "Name oder Passwort ist falsch.")
    return render(request, 'firstapp/login.html')


def loggingout(request):
    logout(request)
    return redirect('Login')


def register(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # create user
            form.save()
            messages.success(request, "Erfolgreich registriert.")
            return redirect('Login')
        else:
            messages.error(
                request, "Registrierung fehlgeschlagen. Bitte erneut versuchen.")
    context = {'form': form}
    return render(request, 'firstapp/register.html', context)

#will be replaced by yirans edit
def editProfil(request, user_id):
    user = User.objects.get(pk=user_id)
    return render(request, 'firstapp/EditProfil.html', {'user': user})


def homepage(request):
    if 'suche' in request.GET:
        suche = request.GET['suche']
        sortieren = Q(Q(tag_system__icontains=suche) | Q( title__icontains=suche) | Q( Beschreibung__icontains=suche))
        cluster = Cluster.objects.filter(sortieren)
    elif 'order_by' in request.GET:
        order_by = request.GET.get('order_by', 'defaultOrderField')
        cluster = Cluster.objects.all().order_by(order_by)
    else:
        cluster = Cluster.objects.all()
    context = {'cluster' : cluster}
    return render(request,'firstapp/homepageAdmin.html', context)

def homepagestudis(request):
    if 'suche' in request.GET:
        suche = request.GET['suche']
        sortieren = Q(Q(tag_system__icontains=suche) | Q( title__icontains=suche) | Q( Beschreibung__icontains=suche))
        cluster= Cluster.objects.filter(sortieren)
    elif 'order_by' in request.GET:
        order_by = request.GET.get('order_by', 'defaultOrderField')
        cluster = Cluster.objects.all().order_by(order_by)
    else:
        cluster = Cluster.objects.all()
    context = {'cluster' : cluster}
    return render(request,'firstapp/homepageStudent.html', context)

def edit(request, cluster_id):
    cluster = Cluster.objects.get(pk=cluster_id)
    form = ClusterForm(request.POST or None, instance=cluster)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        clusterAll = Cluster.objects.all()
        context = {'cluster': clusterAll}
        return render(request, 'firstapp/homepageAdmin.html', context)
    else:
        return render(request, 'firstapp/EditCL.html', {'cluster': cluster, 'form': form})


def new(request):
    form = ClusterForm
    context = {'form': form}
    if request.method == 'POST':
        print(request.POST)
        form = ClusterForm(request.POST)
        if form.is_valid():
            form.save()
        clusterr = Cluster.objects.all()
        contextt = {'cluster': clusterr}
        return render(request, 'firstapp/homepageAdmin.html', contextt)
    else:
        return render(request, 'firstapp/NewCL.html', context)


def deleteCluster(request, cluster_id):
    cluster = Cluster.objects.get(pk=cluster_id)
    cluster.delete()
    return redirect('Übersicht')


def deleteReservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    reservation.delete()
    return redirect('MyReservations')


def impressum(request):
    return render(request, 'firstapp/Impressum.html')


def remove_dups(list):
    unique_list = []
    for l in list:
        if l not in unique_list:
            unique_list.append(l)
    return unique_list 


def reservation(request, cluster_id, user_id):
    if request.method == 'POST':
        """ form = ReservationForm(request.POST, initial={'cluster':cluster_id, 'user':user_id},) """
        form = DateInput(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            cluster = Cluster.objects.get(pk=cluster_id)
            user = User.objects.get(pk=user_id)
            r = Reservation(cluster=cluster, date=date, user=user)
            try:
                r.save()
            except IntegrityError:
                messages.error(request,'Cluster already booked at that time.')
                """this is wrong -> return redirect('bookSlot', cluster_id, user_id) """
            else:
                messages.success(request,'Reservation was successfull.')
        cluster = Cluster.objects.all()
        context = {'cluster': cluster}
        return render(request,'firstapp/homepageStudent.html', context)
    """ form = ReservationForm(initial={'cluster':cluster_id, 'user':user_id}) """
    form = DateInput
    cluster = Cluster.objects.get(pk=cluster_id)
    user = User.objects.get(pk=user_id)    
    return render(request, 'firstapp/reservation.html', {'cluster': cluster, 'form': form, 'user': user})


def myreservation(request, user_id):
    n = User.objects.get(pk=user_id)
    s = Q(Q(user=n))
    reservation = Reservation.objects.filter(s).order_by('cluster', 'date')
    context= {'reservation' : reservation}
    return render(request,'firstapp/myreservations.html', context)
