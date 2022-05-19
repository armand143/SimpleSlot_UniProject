from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'deadline', 'percent')