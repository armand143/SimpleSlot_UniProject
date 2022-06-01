from multiprocessing import context
from tkinter import Entry
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Cluster 
from .forms import  ClusterForm

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
    
