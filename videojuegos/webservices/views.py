from aplicacion.models import *
from .serializer import *
from rest_framework import viewsets

class desarrollador_viewset(viewsets.ModelViewSet):
	queryset = Desarrollador.objects.all()
	serializer_class =  desarrollador_serializer

class plataforma_viewset(viewsets.ModelViewSet):
	queryset = Plataforma.objects.all()
	serializer_class =  plataforma_serializer

class videojuego_viewset(viewsets.ModelViewSet):
	queryset = Videojuego.objects.all()
	serializer_class =  videojuego_serializer