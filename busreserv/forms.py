from django import forms
from datetime import datetime, date, timedelta
from django.utils import timezone
from .models import Bus,Driver,  Reservation
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

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
        fields = ( 'reDate','EndDate', 'km','details','clientName','clientEmail','clientPhone')
        widgets = {
            'reDate': DateInput(),
            'EndDate': DateInput()
        }

    clientName = forms.CharField(label='Your name')
    km = forms.IntegerField(label='Distance in [km]')
    details = forms.CharField(label="Details: type of event, the destination")
    clientEmail = forms.EmailField(label="Your email")
    clientPhone = forms.CharField(label="Your phone number")
    tempReDate = datetime.date(1,1,1) # temp local variable

    def clean_reDate(self):
        reDate = self.cleaned_data['reDate']

        # cheackig if date is not in the past and today,
        if reDate < date.today()+ timedelta(days=1):
            raise forms.ValidationError("The date cannot be in the past or today!")

        # reservation date avilable only for one yeer in future
        if reDate > date.today()+ timedelta(days=365):
            raise forms.ValidationError("You can make a reservation for less than a year ahead")

        #  cheacking if date for this bus is free
        res_all = Reservation.objects.all()
        for item in res_all:
            if reDate >= item.reDate and reDate <= item.EndDate  and item.reBusID == self.instance.reBusID:
                raise forms.ValidationError("This date is reserved for this bus, type another date or choose another bus.")
        #set variable to send for next funtion: clean_EndDate
        self.tempReDate = reDate
        return reDate


    def clean_EndDate(self):
        #check if EndDate is empty
        if not self.data['EndDate']:
            #set numbers days of reservation 1 if no end date
            self.instance.numOfDays =  1
            return None

        # if start date is empty
        if self.tempReDate == datetime.date(1,1,1):
            raise forms.ValidationError("Choose starting date.")

        # if start date is not empty
        else:
            reDate = self.tempReDate
            EndDate = self.cleaned_data['EndDate']

            # cheackig start date is not lower than end date
            if EndDate < reDate:
                raise forms.ValidationError("This data can't be less than the beginning of the reservation!")

            # cheackig if reservation is no longer than 14 days
            if EndDate > reDate+ timedelta(days=14):
                raise forms.ValidationError("You can make a reservation for max 14 days")

            #  cheacking if reservation  for this bus is free
            res_all = Reservation.objects.all()
            for item in res_all:

                #czy rezerwacja od tego autobusu
                if item.reBusID == self.instance.reBusID:

                    #jesli w przedziale nowego zamowienia jest poczatek albo koniec innego to zajęte
                    if reDate <= item.reDate and item.reDate <= EndDate or reDate <= item.EndDate and item.EndDate <= EndDate:
                       raise forms.ValidationError("This date is reserved for this bus, type another date or choose another bus.")

        # calculateing number  days of reservation and save it
        var = EndDate - reDate
        self.instance.numOfDays = var.days + 1
        return reDate



    def __init__(self,*args,**kwargs):
        super(ReservationForm, self).__init__(*args,**kwargs)     #
