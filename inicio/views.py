from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from inicio.models import Video, Proce, Monitor
from django.urls import reverse_lazy

def inicio(request):   
    return render(request, 'inicio/inicio.html', {})

def nosotros(request):
    return render(request, 'inicio/nosotros.html')

class ListadoPlacaVideo(ListView):
    model = Video
    context_object_name = 'listado_de_placaVideo'
    template_name = 'inicio/placavideo.html'
    
class CrearPlacaVideo(CreateView):
    model = Video
    template_name = 'inicio/crear_placaVideo.html'
    fields = ['tipo', 'marca', 'descripcion', 'anio']
    success_url = reverse_lazy('placavideo')
    
class ListadoProcesador(ListView):
    model = Proce
    context_object_name = 'listado_de_procesador'
    template_name = 'inicio/procesador.html'
    
class CrearProcesador(CreateView):
    model = Proce
    template_name = 'inicio/crear_procesador.html'
    fields = ['tipo', 'marca', 'descripcion', 'anio']
    success_url = reverse_lazy('procesador')
    
class ListadoMonitor(ListView):
    model = Monitor
    context_object_name = 'listado_de_monitor'
    template_name = 'inicio/monitor.html'
    
class CrearMonitor(CreateView):
    model = Monitor
    template_name = 'inicio/crear_monitor.html'
    fields = ['tipo', 'marca', 'descripcion', 'anio']
    success_url = reverse_lazy('monitor')