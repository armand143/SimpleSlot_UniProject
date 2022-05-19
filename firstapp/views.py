from multiprocessing import context
from tkinter import Entry
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Todo
from .forms import TodoForm

def homepage(request):
    todos = Todo.objects.all()
    context ={'todos' : todos}
    return render(request,'firstapp/Übersicht.html', context)

def edit(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    form = TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
            form.save()
            
    return render(request, 'firstapp/EditTODO.html', {'todo': todo , 'form' : form} )

def new(request):
    form = TodoForm
    if request.method== 'POST' :
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form' : form}
    return render(request, 'firstapp/NewTODO.html', context)

def delete(request, todo_id):
     todo = Todo.objects.get(pk=todo_id)
     todo.delete()
     return redirect('Übersicht')

def impressum(request):
    return render(request, 'firstapp/Impressum.html')
    
