from django.contrib import admin
from .models import Bus, Client, Reservation

admin.site.register(Bus)
admin.site.register(Client)
admin.site.register(Reservation)
