from django.shortcuts import render
from django.http import HttpResponse

from .forms import *
from .models import *

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def equipos(request):
    
    if request.method == 'POST':
        miFormulario = EquipoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            equipo = Equipo(nombre=data['nombre'], pais=data['pais'], plataforma=data['plataforma'])
            
            equipo.save()
            
            return render(request, 'inicio.html')
    else:
        miFormulario = EquipoFormulario()
    
    return render(request, 'equipos.html', {'miFormulario':miFormulario})

def torneos(request):
    
    if request.method == 'POST':
        
        miFormulario = TorneoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            torneo = Torneo(nombre=data['nombre'], reglas=data['reglas'], puntos=data['puntos'])
            
            torneo.save()
            
            return render(request, 'inicio.html')
    else:
        miFormulario = TorneoFormulario()
    
    return render(request, 'torneos.html', {'miFormulario':miFormulario})

def juegos(request):
    
    if request.method == 'POST':
        
        miFormulario = JuegoFormulario(request.POST)
        
        if miFormulario.is_valid():
            
            data = miFormulario.cleaned_data
            
            juego = Juego(nombre=data['nombre'], genero=data['genero'], anio_lanzamiento=data['anio_lanzamiento'], desarrolladora=data['desarrolladora'])
            
            juego.save()
            
            return render(request, 'inicio.html')
    else:
        miFormulario = JuegoFormulario()
    
    return render(request, 'juegos.html', {'miFormulario':miFormulario})

def busqueda_juego(request):
    return render(request, 'busquedaJuego.html')

def buscar(request):
    
    busqueda = request.GET['nombre']
    
    juego = Juego.objects.get(nombre = busqueda)
    
    return render(request, 'resultadoBusqueda.html', {'juego':juego})