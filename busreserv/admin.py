from django.contrib import admin
from .models import Bus, Driver,  Reservation

admin.site.register(Bus)
admin.site.register(Driver)

admin.site.register(Reservation)
