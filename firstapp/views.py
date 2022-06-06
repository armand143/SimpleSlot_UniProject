from multiprocessing import context
from tkinter import Entry
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Cluster 
from .forms import  ClusterForm, RegisterForm

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from firstapp import models

def loggingin(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('Übersicht')
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
            #create user
            form.save()
            messages.success(request, "Erfolgreich registriert.")
            return redirect('Login')
        else:
            messages.error(request, "Registrierung fehlgeschlagen. Bitte erneut versuchen.")
    context = {'form': form}
    return render(request, 'firstapp/register.html', context)

# our own registration try without the defaul django Form
# def register(request):
#     if request.method == "POST":
#         register_form = RegisterForm(request.POST)
#         message = "check"
#         if register_form.is_valid(): 
#             matrikelnummer = register_form.cleaned_data['matrikelnummer']
#             username = register_form.cleaned_data['username']
#             password1 = register_form.cleaned_data['password1']
#             password2 = register_form.cleaned_data['password2']        
#             if password1 != password2: 
#                 message = "Passwort muss übereinstimmen."
#                 return render(request, 'firstapp/register.html', locals())
#             else:
#                 same_matrikelnummer = models.User.objects.filter(matrikelnummer=matrikelnummer)
#                 if same_matrikelnummer:
#                     message = 'Matrikelnummer existiert bereits.'
#                     return render(request, 'firstapp/register.html', locals())

#                 new_user = models.User.objects.create()
#                 new_user.matrikelnummer = matrikelnummer
#                 new_user.username = username
#                 new_user.password = password1
#                 new_user.save()
#                 return redirect('/login/')
#     register_form = RegisterForm()
#     return render(request, 'firstapp/register.html', locals())


def homepage(request):
    cluster = Cluster.objects.all()
    context ={'cluster' : cluster}
    return render(request,'firstapp/ÜbersichtCLA.html', context)

def homepagestudis(request):
    cluster = Cluster.objects.all()
    context ={'cluster' : cluster}
    return render(request,'firstapp/ÜbersichtCLS.html', context)

def edit(request, cluster_id):
    cluster = Cluster.objects.get(pk=cluster_id)
    form = ClusterForm(request.POST or None, instance=cluster)
    if request.method == "POST":
        if form.is_valid():
            form.save() 
        clusterr = Cluster.objects.all()
        context ={'cluster' : clusterr}
        return render(request,'firstapp/ÜbersichtCLA.html', context)
    else:             
        return render(request, 'firstapp/EditCL.html', {'cluster': cluster , 'form' : form} )

def new(request):
    form = ClusterForm
    context = {'form' : form}
    if request.method== 'POST' :
        print(request.POST)
        form = ClusterForm(request.POST)
        if form.is_valid():
            form.save()
        clusterr = Cluster.objects.all()
        contextt ={'cluster' : clusterr}
        return render(request,'firstapp/ÜbersichtCLA.html', contextt)
    else:          
        return render(request, 'firstapp/NewCL.html', context)

def delete(request, todo_id):
     todo = Cluster.objects.get(pk=todo_id)
     todo.delete()
     return redirect('Übersicht')

def impressum(request):
    return render(request, 'firstapp/Impressum.html')
    
