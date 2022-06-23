from django.contrib import admin
from .models import Cluster, Reservation, UserProfile

# Register your models here.
admin.site.register(Cluster)
admin.site.register(Reservation)
admin.site.register(UserProfile)
