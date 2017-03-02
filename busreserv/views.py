from django.shortcuts import render, get_object_or_404
from .models import Bus , Client, Reservation
from .forms import BusForm, ClientForm, ReservationForm
from django.utils import timezone
from django.contrib import messages



def panel_view(request):
    buses = Bus.objects.all()
    return render(request, 'busreserv/panel.html', {'buses' : buses})

def edit_vehicle_view(request, pk):
    vehicle = get_object_or_404(Bus, pk=pk)
    if request.method == "POST":
        form_var = BusForm(request.POST, instance=vehicle)
        if form_var.is_valid():
            newBus = form_var.save(commit=False)
            newBus.save()
            buses = Bus.objects.all()           #to previos site in broswer
            return render(request, 'busreserv/panel.html', {'buses' : buses})
    else:
        form_var = BusForm(instance=vehicle)
    return render(request, 'busreserv/new_vehicle.html', {'formBus': form_var})

def new_vehicle_view(request):
    if request.method == "POST":
        form_var = BusForm(request.POST)
        if form_var.is_valid():
            newBus = form_var.save()            #create nawBus
            newBus.save()                       #save to database
            buses = Bus.objects.all()           #to previos site in broswer
            return render(request, 'busreserv/panel.html', {'buses' : buses})
    else:
        form_var = BusForm()
    return render(request, 'busreserv/new_vehicle.html', {'formBus': form_var})


def delete_vehicle_view(request, pk):
    vehicle = get_object_or_404(Bus, pk=pk)
    vehicle.delete()
    buses = Bus.objects.all()           #to previos site in broswer
    return render(request, 'busreserv/panel.html', {'buses' : buses})

def client_panel_view(request):
    buses = Bus.objects.filter(available_for_cutomers=True)
    return render(request, 'busreserv/client.html', {'buses' : buses})

def reservation_view(request, pk):
    bus = get_object_or_404(Bus, pk=pk)

    form_client = ClientForm(prefix='cl')
    form_var = ReservationForm(prefix='res')

    if request.method == "POST":

        form_client = ClientForm(request.POST,prefix='cl')
        form_var = ReservationForm(request.POST,prefix='res')

        if form_var.is_valid() and form_client.is_valid():
            newreservation = form_var.save(commit=False)
            newreservation.reBusID = bus
            newreservation.reClientID = form_client.save()       #can be changed i future if the same client
            newreservation.reDate = timezone.now()
            newreservation.save()
        buses = Bus.objects.filter(available_for_cutomers=True)
        return render(request, 'busreserv/client.html', {'buses' : buses})
    else:
        form_var = ReservationForm()
        form_client = ClientForm()
        return render(request, 'busreserv/newreservation.html', {'formReservation' : form_var, 'bus':bus , 'form_client':form_client})
