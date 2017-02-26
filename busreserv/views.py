from django.shortcuts import render
from .models import Bus

def panel(request):
    buses = Bus.objects.all()
    return render(request, 'busreserv/panel.html', {'buses' : buses})
