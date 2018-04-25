from django.urls import path
from .views import *

urlpatterns =[
	path('base/',vista_base, name='vista_base'),
	path('',vista_index, name='vista_index'),
	path('animadores/',vista_animadores, name='vista_animadores'),
	#CRUD
		#Agregar
	path('agregar_juego/',vista_agregar_juego, name='agregar_juego'),
	path('agregar_animador/',vista_agregar_animador, name='agregar_animador'),
	path('agregar_desarrollador/',vista_agregar_desarrollador, name='agregar_desarrollador'),


	path('ver_juego/<int:id_juego>/',vista_ver_juego, name='ver_juego'),

		#Edita
	path('editar_juego/<int:id_juego>/',vista_editar_juego, name='editar_juego'),
	path('editar_animador/<int:id_ani>/',vista_editar_animador, name='editar_animador'),
	path('editar_desarrollador/<int:id_des>/',vista_editar_desarrollador, name='editar_desarrollador'),

	path('eliminar_juego/<int:id_juego>/',vista_eliminar_juego, name='eliminar_juego'),
	#LOGIN

	path('logout/',vista_logout, name='vista_logout'), #Cerrar sesion
	#REGISTRAR
	path('registrar/',vista_registrar, name='vista_registrar')

]