from django.contrib import admin
from .models import Cluster, Reservation

# Register your models here.
admin.site.register(Cluster)
admin.site.register(Reservation)
