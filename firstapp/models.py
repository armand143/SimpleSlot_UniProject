from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250)
    deadline = models.DateField()
    percent = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.id


