from django import forms
from datetime import datetime, date, timedelta
from django.utils import timezone
from .models import Bus,Driver,  Reservation
from django.core.validators import MaxValueValidator, MinValueValidator


class BusForm(forms.ModelForm):

    class Meta:
        model = Bus
        fields = ('brand', 'plate_nr','people_capacity','price_per_km','description','available_for_cutomers','currentDriver')

class DriverForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ('driverName','driverPhone')




class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ( 'reDate', 'km','details','clientName','clientEmail','clientPhone')
        widgets = {
            'reDate': DateInput()
        }


    clientName = forms.CharField(label='Your name')
    km = forms.IntegerField(label='Distance in [km]')
    details = forms.CharField(label="Details: type of event, the destination")
    clientEmail = forms.EmailField(label="Your email")
    clientPhone = forms.CharField(label="Your phone number")

    #reDate = forms.DateField(label='Date of reservation yyyy-mm-dd', initial=timezone.now())   #date to show in form

    def clean_reDate(self):
        reDate = self.cleaned_data['reDate']

        if reDate < date.today()+ timedelta(days=1):   # cheackig if date is not in the past
            raise forms.ValidationError("The date cannot be in the past or today!")

        if reDate > date.today()+ timedelta(days=365):   # cheackig if date is not in the past
            raise forms.ValidationError("You can make a reservation for less than a year ahead")


        res_all = Reservation.objects.all()           #  cheacking if date for this bus is free
        for item in res_all:
            if item.reDate == reDate and item.reBusID == self.instance.reBusID:
                raise forms.ValidationError("This date is reserved for this bus, type another date or choose another bus.")
        return reDate



    def __init__(self,*args,**kwargs):
        super(ReservationForm, self).__init__(*args,**kwargs)     #
