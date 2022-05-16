from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
# Create your views here.
from .models import Todo


def homepage(request):
    todos = Todo.objects.all().order_by('deadline')
    return render(request,'firstapp\Übersicht.html', {'todos':todos})

def index(request):
    return HttpResponse("It started correctly, nice")

def edit(request, todo_id):
    elem = get_object_or_404(Todo, pk=todo_id)
    return render(request, 'firstapp/EditTODO.html', {'todo.title' : elem.title}, {'todo.deadline' : elem.deadline}, {'todo.percent' : elem.percent})

def new(request):
    return render(request, 'firstapp/NewTODO.html')

def impressum(request):
    return render(request, 'firstapp/Impressum.html')