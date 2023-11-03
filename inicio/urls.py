from django.urls import path
from inicio.views import inicio, nosotros, ListadoPlacaVideo, CrearPlacaVideo, ListadoProcesador, CrearProcesador, ListadoMonitor, CrearMonitor

urlpatterns = [
    path('', inicio, name='inicio'),
    path('nosotros/', nosotros, name='nosotros'),
    path('placavideo/' , ListadoPlacaVideo.as_view(), name='placavideo'),
    path('placavideo/crear/' , CrearPlacaVideo.as_view(), name='crear_placavideo'),
    path('procesador/' , ListadoProcesador.as_view(), name='procesador'),
    path('procesador/crear/' , CrearProcesador.as_view(), name='crear_procesador'),
    path('monitor/' , ListadoMonitor.as_view(), name='monitor'),
    path('monitor/crear/' , CrearMonitor.as_view(), name='crear_monitor'),
]
