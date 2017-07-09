from django.shortcuts import render
from django.utils import timezone
from .models import Genero, Juego
from .forms import JuegoForm
from django.shortcuts import redirect


def juego_list(request):
    generos = Genero.objects.all()
    return render(request, 'steam/juego_list.html', {'generos': generos})

def categoria_list(request,pk):
    juegos=Juego.objects.filter(genero=pk)
    return render(request, 'steam/categoria_list.html', {'juegos': juegos})
        
def Juego_nuevo(request):
	if request.method == "JUEGO":
		form = JuegoForm(request.JUEGO)
		if form.is_valid():
			juego = form.save(commit=False)
			juego.save()
			return redirect('juego_detail', pk=juego.pk)
	else:
		form = JuegoForm()
	return render(request, 'steam/agregar_juego.html', {'form': form})

