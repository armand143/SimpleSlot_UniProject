from asyncio.windows_events import NULL
from cmath import pi
from multiprocessing import context
from sqlite3 import Date
from tkinter import Entry
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Cluster, Datum, Nutzer, Reservation, Datum
from .forms import ClusterForm, RegisterForm, ReservationForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from firstapp import models
from django.db.models import Q
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


def editProfil(request, user_id):
    user = Nutzer.objects.get(pk=user_id)
    return render(request, 'firstapp/EditProfil.html', {'user': user})


def homepage(request):
    if 'suche' in request.GET:
        suche = request.GET['suche']
        sortieren = Q(Q(tag_system__icontains=suche) | Q(
            title__icontains=suche) | Q(Beschreibung__icontains=suche))
        cluster = Cluster.objects.filter(sortieren)
    else:
        cluster = Cluster.objects.all()
    context = {'cluster': cluster}
    return render(request, 'firstapp/homepageAdmin.html', context)

# def login(request):
#     return render(request, 'firstapp/login.html')


def homepagestudis(request):
    if 'suche' in request.GET:
        suche = request.GET['suche']
        sortieren = Q(Q(tag_system__icontains=suche) | Q(
            title__icontains=suche) | Q(Beschreibung__icontains=suche))
        cluster = Cluster.objects.filter(sortieren)
    else:
        cluster = Cluster.objects.all()
    context = {'cluster': cluster}
    return render(request, 'firstapp/homepageStudent.html', context)


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


def deletee(request, cluster_id):
    cluster = Cluster.objects.get(pk=cluster_id)
    cluster.delete()
    return redirect('Übersicht')


def impressum(request):
    return render(request, 'firstapp/Impressum.html')


def remove_dups(list):
    unique_list = []
    for l in list:
        if l not in unique_list:
            unique_list.append(l)
    return unique_list 


def update_slots(request, slot_value, date_value):

    picked_cluster = Datum.objects.filter(diction__date = date_value)[0]
    picked_date = picked_cluster.diction['date']
    if picked_date == '':
        picked_cluster.diction['date'] = date_value
        picked_cluster.save()

    picked_date_obj = Datum.objects.filter(diction__date = date_value)[0] #Datum.objects.get(date_name=date_value)
    picked_date_dict = Datum.objects.filter(diction__date = date_value)[0].diction  #could be more than 1 cause you filter with date ...use clus_title for unique data
    

    picked_date_dict['not_av_slots'].append(slot_value)
    picked_date_dict['av_slots'].remove(slot_value)
    picked_date_obj.diction = picked_date_dict
    picked_date_obj.save()

    temp_list = picked_date_dict['not_av_slots']

    picked_date_dict['not_av_slots'] = remove_dups(temp_list)
    picked_date_obj.diction = picked_date_dict
    picked_date_obj.save()

    contextt = {'picked_date': picked_date_obj.diction['date'],
                'av_slots': picked_date_obj.diction['av_slots']
                }
    return render(request, 'firstapp/slot_booking.html', contextt)


def book_slots(request, date):
    picked_date = Datum.objects.filter(diction__date = date)[0] #date #Datum.objects.get(pk=date_id)
    available_slots = ['08:00 -09:00',
                       '09:30 -10:30',
                       '11:00 -12:00',
                       '12:30 -13:30',
                       '14:00 -15:00',
                       '15:30 -16:30',
                       '17:00 -18:00'
                       ]

    if picked_date is not NULL:
        booked_slots = picked_date.diction['not_av_slots']
        free_slots = []

        if len(booked_slots) == 0:
            picked_date.diction['av_slots'] = available_slots
            picked_date.save()

        else:
            for s in available_slots:
                if s not in booked_slots:
                    free_slots.append(s)
                    picked_date.diction['av_slots'] = free_slots
                    picked_date.save()

        return remove_dups(picked_date.diction['av_slots'])

    else:
        return []


def dict_exists(request, dict):
    all_dicts = Datum.objects.all()
    for dict_obj in all_dicts:
        if dict.diction['clus_title'] == dict_obj.diction['clus_title'] and dict.diction['date'] == dict_obj.diction['date']:
            return True
        else:
            return False

def book(request, cluster_id):
    available_slots = []
    cluster = Cluster.objects.get(pk=cluster_id)
    res = Reservation()
    res.cluster = cluster
    res.clus_name = cluster.title

    form = ReservationForm(request.POST or None, instance=res)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid:
        get_selected_date_set = Datum.objects.filter(diction__clus_title = cluster.title)  # gives a queryset with matching Date object

        if len(get_selected_date_set) is 0:
            form.date = str(request.POST['date'])
            form.save()
            picked_date = Datum(diction = {
                                           'clus_tag': cluster.tag_system,
                                           'clus_title' : cluster.title,
                                           'date': str(request.POST['date']),
                                           'clus_description': cluster.Beschreibung,
                                           'av_slots': [],
                                           'not_av_slots': []
               })
            picked_date.save()
            available_slots = book_slots(request, str(request.POST['date']))

        else:
            form.date = str(request.POST['date'])
            form.save()

            picked_cluster = Datum.objects.filter(diction__clus_title = cluster.title)[0]
            picked_date = picked_cluster.diction['date']
            if dict_exists(request, picked_cluster) == False: #picked_date == '':
                new_date_same_cluster = Datum(diction = {         
                                                        'clus_tag': cluster.tag_system,
                                                        'clus_title' : cluster.title,
                                                        'date': str(request.POST['date']),
                                                        'clus_description': cluster.Beschreibung,
                                                        'av_slots': [],
                                                        'not_av_slots': []
                                                        })
                new_date_same_cluster.save()    #because we should be capable to book the same cluster for different dates 
                available_slots =  book_slots(request, new_date_same_cluster.diction['date'])

            else:
                # picked_cluster.diction['date'] = str(request.POST['date'])
                # picked_cluster.save()
                available_slots =  book_slots(request, picked_cluster.diction['date'])
            #picked_date = Datum.objects.filter(diction__date = str(request.POST['date']))[0]

            

    else:
        return render(request, 'firstapp/reservationForm.html', context)
    reserved_objs = Reservation.objects.all()
    picked_cluster = Datum.objects.filter(diction__clus_title = cluster.title)[0]
    reserved_dates = Datum.objects.filter(diction__clus_title = picked_cluster.diction['clus_title'])[0]
    clusters = Cluster.objects.all()
    clus = model_to_dict(cluster)
    contextt = {'picked_date': str(request.POST['date']),    #this date is also passed in to update_slot() function
                'av_slots': available_slots,
                'schedules': reserved_objs,
                'res_dates': reserved_dates,
                'cluster': clusters,
                'mytext': messages,
                'test': clus
                }

    return render(request, 'firstapp/slot_booking.html', contextt)
    # return render(request, 'firstapp/ReservierteTermine.html', contextt)


def ResPage(request):
    reserved_objs = Reservation.objects.all().order_by('clus_name').distinct()
    cluster = Cluster.objects.all()
    reserved_dates = Datum.objects.all()

    contextt = {'schedules': reserved_objs,
                'cluster': cluster,
                'res_dates': reserved_dates,
                }
    return render(request, 'firstapp/ReservierteTermine.html', contextt)


class ReservationCreateView(CreateView):
    model = Reservation
    form_class = ReservationForm
