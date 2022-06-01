from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Cluster, Todo
        
class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'deadline', 'percent')

        
class ClusterForm(ModelForm):
    class Meta:
        model = Cluster
        fields = ('title', 'quantity', 'duration', 'availability')
