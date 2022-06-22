from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Cluster(models.Model):
    tag_choice = (
        ('Art' , 'Art'),
        ('Chemistry' , 'Chemistry'),
        ('Technical Devices' , 'Technical Devices'),
        ('Cooking' , 'Cooking'),
        ('Music' , 'Music'),
    )

    tag_system = models.CharField(max_length=30, blank=True, choices=tag_choice)
    title = models.CharField(max_length=250)
    Beschreibung = models.CharField(max_length=250)
    availability = models.BooleanField()  

    def __str__(self):
        return self.title


# not used yet, using the defaul "User" model from django
class Nutzer(models.Model):
    matrikelnummer = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    def str(self):
        return '%s'%self.username


class Reservation(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    date = models.DateField()
    user = models.ForeignKey(User, on_delete= models.CASCADE)

    class Meta:
        unique_together = ('cluster', 'date')

    def __str__(self):
        return self.user.username

#python manage.py makemigrations --> python manage.py migrate
