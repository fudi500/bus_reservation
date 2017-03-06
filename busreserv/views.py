from django.shortcuts import render, get_object_or_404
from .models import Bus , Driver, Reservation
from .forms import BusForm,DriverForm, ReservationForm
from django.utils import timezone
from django.contrib import messages
from datetime import datetime, date
from django.http import HttpResponseRedirect
import datetime
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.template import loader
from smsapi.client import SmsAPI


# main admin panel for owner
def panel_view(request):
    buses = Bus.objects.all()
    drivers = Driver.objects.all()

    # colect list of reservation in future
    # take reservations (__gte - greater than or equal)
    res = Reservation.objects.filter(reDate__gte=date.today())

    """"  old version
    res = Reservation.objects.all()
    resfuture = []
    for item in res:
        #if is in the furure
        if item.reDate >= date.today():
            resfuture.append(item)
    """

    return render(request, 'busreserv/panel.html', {
        'buses' : buses,
        'drivers':drivers,
        'res': res,
    })

def new_driver_view(request):
    if request.method == "POST":
        driverForm = DriverForm(request.POST)
        if driverForm.is_valid():
            newDriver = driverForm.save()
            return HttpResponseRedirect("/panel")
    else:
        driverForm = DriverForm()
    return render(request, 'busreserv/driver.html', {
        'driverForm':driverForm
    })

def edit_driver_view(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    if request.method == "POST":
        driverForm = DriverForm(request.POST, instance=driver)
        if driverForm.is_valid():
            newDriver = driverForm.save()
            return HttpResponseRedirect("/panel")
    else:
        driverForm = DriverForm(instance=driver)
    return render(request, 'busreserv/driver.html', {
        'driverForm':driverForm
    })

def delete_driver_view(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    driver.delete()
    return HttpResponseRedirect("/panel")

def edit_vehicle_view(request, pk):
    vehicle = get_object_or_404(Bus, pk=pk)
    if request.method == "POST":
        form_var = BusForm(request.POST, instance=vehicle)
        if form_var.is_valid():
            editedBus = form_var.save(commit=False)
            editedBus.save()
            return render(request, 'busreserv/bus_details.html', {
                'Bus': editedBus
            })
    else:
        form_var = BusForm(instance=vehicle)
    return render(request, 'busreserv/new_vehicle.html', {'formBus': form_var})

def new_vehicle_view(request):
    if request.method == "POST":
        form_var = BusForm(request.POST)
        if form_var.is_valid():
            newBus = form_var.save()            #create nawBus
            newBus.save()                       #save to database
            return render(request, 'busreserv/bus_details.html', {
                'Bus': newBus
            })
    else:
        form_var = BusForm()
    return render(request, 'busreserv/new_vehicle.html', {
        'formBus': form_var
    })

def vehicle_details_view(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    return render(request, 'busreserv/bus_details.html', {
        'Bus': bus
    })

def delete_vehicle_view(request, pk):
    vehicle = get_object_or_404(Bus, pk=pk)
    vehicle.delete()
    return HttpResponseRedirect("/panel")

def client_panel_view(request):
    buses = Bus.objects.filter(available_for_cutomers=True)
    return render(request, 'busreserv/client.html', {
        'buses' : buses
    })

def reservation_view(request, pk):
    bus = get_object_or_404(Bus, pk=pk)
    newreservation = Reservation()
    newreservation.reBusID = bus
    if request.method == "POST":
        form_var = ReservationForm(request.POST,instance=newreservation,initial={'reDate': datetime.datetime.now()})
        date = request.POST.get('reDate')
        if form_var.is_valid():
            newreservation = form_var.save(commit=False)
            if not request.POST.get('EndDate'):
                newreservation.EndDate = request.POST.get('reDate') # if EndDate is none: EndDate = reDate
            else:
                newreservation.EndDate = request.POST.get('EndDate')
            newreservation.save()

            return HttpResponseRedirect(reverse("reservation_details",
                                                kwargs={'pk':   newreservation.id, 'bus': bus.id}
            ))

    else:
        form_var = ReservationForm()
    return render(request, 'busreserv/newreservation.html', {'formReservation' : form_var, 'bus':bus})


def reservation_details_view(request, pk, bus):
    res = get_object_or_404(Reservation, pk=pk)
    bus = get_object_or_404(Bus, pk=bus)

    price = res.km * bus.price_per_km

    #----sending Email-------------
    """
    subject1 =  str(res.reDate) + ' Bus reservation '
    message1 = ''
    html_message = loader.render_to_string(
            'busreserv/message.html',
            {
                'Bus' : bus,
                'Reservation' : res,
                'price' : price
            }
        )

    send_mail(
        subject1,
        html_message,
        'busreservation500@gmail.com',
        [res.clientEmail],
        fail_silently=True,
        html_message=html_message
    )
    """
    #-------------------------

    #------S M S  to the driver-------------
    """
    driversms = Driver()
    driversms = Driver.objects.get(id=bus.currentDriver.id)

    # if driver exist (in Bus.model currentDriver in not required)
    if kierowca:
        # if reservatnion for 1 day
        if res.reDate == res.EndDate:
            messageSMS = 'Witaj '+ kierowca.driverName + '. Rezerwacja ' + bus.plate_nr +" Data: "+ str(res.reDate)
        else:
            messageSMS = 'Witaj '+ kierowca.driverName + '. Rezerwacja ' + bus.plate_nr +" od "+ str(res.reDate) + " do " + str(res.EndDate)

        api = SmsAPI()

        api.set_username('busreservation500@gmail.com')
        api.set_password('haslo SmsAPI.pl')

        api.service('sms').action('send')

        api.set_content(messageSMS)
        api.set_to(driversms.driverPhone)

        result = api.execute()
    """
    #-------------------------

    return render(request, 'busreserv/details.html', {
        'Bus' : bus,
        'Reservation' : res,
        'price' : price
    })
