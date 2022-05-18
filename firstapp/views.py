from multiprocessing import context
from tkinter import Entry
from django.shortcuts import render
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

def index(request):
    return HttpResponse("It started correctly, nice")

def edit(request, todo_id):
    elem = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'firstapp/EditTODO.html', {'todo.title' : elem.title}, {'todo.deadline' : elem.deadline}, {'todo.percent' : elem.percent})

def new(request):
    form = TodoForm
    if request.method== 'POST' :
        print(request.POST)
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form' : form}
    return render(request, 'firstapp/NewTODO.html', context)

def impressum(request):
    return render(request, 'firstapp/Impressum.html')
