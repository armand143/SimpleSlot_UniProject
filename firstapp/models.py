from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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


# not used yet, using the defaul "User" model from django
class Nutzer(models.Model):
    matrikelnummer = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=64)
    def str(self):
        return '%s'%self.username

class Appointment(models.Model):
    timeslot_list = (
        (0, '08:00 – 10:00'),
        (1, '10:00 – 12:00'),
        (2, '12:00 – 14:00'),
        (3, '14:00 – 16:00'),
        (4, '16:00 – 18:00'),
        (5, '18:00 – 20:00'),
    )
    timeslot = models.IntegerField(choices=timeslot_list)


class Reservation(models.Model):
    cluster = models.ForeignKey(Cluster, on_delete=models.CASCADE)
    clus_name = models.CharField(max_length=100)
    date = models.CharField(max_length=100)

class Datum(models.Model):
    diction = models.JSONField(null = True)


#python manage.py makemigrations --> python manage.py migrate
