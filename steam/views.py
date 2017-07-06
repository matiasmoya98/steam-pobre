from django.shortcuts import render
from django.utils import timezone
from .models import Genero
from .models import Juego

def juego_list(request):
    generos = Genero.objects.all()
    return render(request, 'steam/juego_list.html', {'generos': generos})

def listado_categoria(request,pk):
    juegos=Juego.objetcs.filter(genero=pk)
    return render(request, 'steam/categoria_list.html', {'juegos': juegos})
        


