from django.shortcuts import render
from django.utils import timezone
from .models import Genero, Juego

def juego_list(request):
    generos = Genero.objects.all()
    return render(request, 'steam/juego_list.html', {'generos': generos})

def categoria_list(request,pk):
    juegos=Juego.objects.filter(genero=pk)
    return render(request, 'steam/categoria_list.html', {'juegos': juegos})
        


