from rest_framework import serializers
from aplicacion.models import *

class desarrollador_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Desarrollador
		fields = ('url','nombre','sede','f_fundacion','animador',)

class plataforma_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Plataforma
		fields = ('url','nombre','capacidad','modelo','media','procesador',)

class videojuego_serializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model  = Videojuego
		fields = ('url','nombre','descripcion','categoria','imagen','f_lanzamiento','version','descargas','precio','tamaño','desarrollador','valoraciones','plataforma',)