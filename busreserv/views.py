from django.shortcuts import render

def panel(request):
    return render(request, 'busreserv/panel.html', {})
