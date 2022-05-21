from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250)
    deadline = models.DateField()
    percent = models.PositiveIntegerField(default=0,
                validators=[MaxValueValidator(100),MinValueValidator(0)])

