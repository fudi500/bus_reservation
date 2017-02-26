from django.shortcuts import render, get_object_or_404
from .models import Bus

def panel(request):
    buses = Bus.objects.all()
    return render(request, 'busreserv/panel.html', {'buses' : buses})

def edit_vehicle(request, pk):
    vehicle = get_object_or_404(Bus, pk=pk)
    return render(request, 'busreserv/edit_vehicle.html', {'vehicle':vehicle})
