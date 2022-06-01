from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Cluster(models.Model):
    title = models.CharField(max_length=250)
    quantity = models.PositiveIntegerField(default=0,
                validators=[MaxValueValidator(1),MinValueValidator(0)])
    duration= models.PositiveIntegerField()
    availability = models.DateField()

class freeDates(models.Model):
    date = models.DateField()   



class Todo(models.Model):
    title = models.CharField(max_length=250)
    deadline = models.DateField()
    percent = models.PositiveIntegerField(default=0,
                validators=[MaxValueValidator(100),MinValueValidator(0)])


#python manage.py makemigrations --> python manage.py migrate
