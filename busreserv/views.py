from django.shortcuts import render, get_object_or_404
from .models import Bus
from .forms import BusForm

def panel_view(request):
    buses = Bus.objects.all()
    return render(request, 'busreserv/panel.html', {'buses' : buses})

def edit_vehicle_view(request, pk):
    vehicle = get_object_or_404(Bus, pk=pk)
    return render(request, 'busreserv/edit_vehicle.html', {'vehicle':vehicle}) 

def new_vehicle_view(request):
    if request.method == "POST":
        form_var = BusForm(request.POST)
        if form_var.is_valid():
            newBus = form_var.save()
            newBus.save()                       #save to database
            buses = Bus.objects.all()           #to previos site in broswer
            return render(request, 'busreserv/panel.html', {'buses' : buses})
    else:
        form_var = BusForm()
    return render(request, 'busreserv/new_vehicle.html', {'formBus': form_var})
