from django.shortcuts import render
from django.utils import timezone
from .models import Juego

def juego_list(request):
    juegos = Juego.objects.all()
    return render(request, 'steam/juego_list.html', {'juegos': juegos})
