from django.shortcuts import render, redirect
from .models import Pelicula
from .forms import PeliculaForm

def lista_peliculas(request):
    peliculas = Pelicula.objects.all()
    return render(request, 'peliculas/lista.html', {'peliculas': peliculas})

def agregar_pelicula(request):
    if request.method == 'POST':
        form = PeliculaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = PeliculaForm()
    return render(request, 'peliculas/formulario.html', {'form': form})
