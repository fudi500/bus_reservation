from django import forms

from .models import Bus,  Client, Reservation

class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ('brand', 'plate_nr','people_capacity','price_per_km','description','available_for_cutomers')


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('firstName', 'lastName','clientEmail','clientPhone')

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ( 'km','details')
