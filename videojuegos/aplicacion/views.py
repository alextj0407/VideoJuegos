from django.shortcuts import render, redirect #impor para redirec
from django.contrib.auth import login, logout, authenticate  #imports para login

from django.http import HttpResponse #imports para usar formato json
from django.core import serializers

from .models import *
from .forms import *

# Create your views here.

def vista_base(request):

	#LOGIN
	usu = ""
	pas = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			pas = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=pas)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj="Usuario o Clave incorrectos"
	formulario= login_form()
	#END login

	l = Videojuego.objects.all()
	return render (request, 'base.html', locals())
#=================================================

def vista_index(request):

	#LOGIN
	usu = ""
	pas = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			pas = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=pas)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj="Usuario o Clave incorrectos"
	formulario= login_form()
	#END login

	lista = Videojuego.objects.all()
	return render (request, 'index.html', locals())

#--------------------------------------------------
def vista_animadores(request):

	#LOGIN
	usu = ""
	pas = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			pas = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=pas)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj="Usuario o Clave incorrectos"
	formulario= login_form()
	#END login


	dsr = Desarrollador.objects.all()
	anm = Animador.objects.all()

	return render (request, 'animadores.html', locals())

#====================CRUD======================================

def vista_agregar_juego(request):

	#LOGIN
	usu = ""
	pas = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			pas = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=pas)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj="Usuario o Clave incorrectos"
	formulario= login_form()
	#END login

	if request.method == 'POST':
		form = agregar_juego(request.POST, request.FILES)
		if form.is_valid():
			game = form.save(commit = False)
			game.status = True
			game.save()
			form.save_m2m()
			return redirect ('/')

	else:
		form = agregar_juego()
	return render (request, 'agregar_juego.html', locals())

	#.........................................................

def vista_agregar_animador(request):	
	#LOGIN
	usu = ""
	pas = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			pas = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=pas)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj="Usuario o Clave incorrectos"
	formulario= login_form()
	#END login

	if request.method == 'POST':
		form = agregar_animador(request.POST, request.FILES)
		if form.is_valid():
			anim = form.save(commit = False)
			anim.status = True
			anim.save()
			form.save_m2m()
			return redirect ('/animadores/')

	else:
		form = agregar_animador()
	return render (request, 'agregar_animador.html', locals())

	#...............................................................
def vista_agregar_desarrollador(request):	
	#LOGIN
	usu = ""
	pas = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			pas = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=pas)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj="Usuario o Clave incorrectos"
	formulario= login_form()
	#END login

	if request.method == 'POST':
		form = agregar_desarrollador(request.POST, request.FILES)
		if form.is_valid():
			des = form.save(commit = False)
			des.status = True
			des.save()
			form.save_m2m()
			return redirect ('/animadores/')

	else:
		form = agregar_desarrollador()
	return render (request, 'agregar_desarrollador.html', locals())
#----------------VER-------------------------------------------
def vista_ver_juego(request, id_juego):

	#LOGIN
	usu = ""
	pas = ""
	if request.method == 'POST':
		formulario = login_form(request.POST)
		if formulario.is_valid():
			usu = formulario.cleaned_data['usuario']
			pas = formulario.cleaned_data['clave']
			usuario = authenticate(username=usu, password=pas)
			if usuario is not None and usuario.is_active:
				login(request, usuario)
				return redirect('/')
			else:
				msj="Usuario o Clave incorrectos"
	formulario= login_form()
	#END login

	j = Videojuego.objects.get(id=id_juego)

	return render (request, 'ver_juego.html',locals())


#==================EDITAR====================================

def vista_editar_juego(request, id_juego):

	game = Videojuego.objects.get(id=id_juego)

	if request.method == 'POST':
		form = agregar_juego(request.POST, request.FILES, instance=game)
		if form.is_valid():

			game = form.save()

			return redirect ('/')
	else:
		form = agregar_juego(instance=game)
	return render (request, 'agregar_juego.html', locals())
	#...........................................................

def vista_editar_desarrollador(request, id_des):

	des = Desarrollador.objects.get(id=id_des)

	if request.method == 'POST':
		form = agregar_desarrollador(request.POST, request.FILES, instance=des)
		if form.is_valid():

			des = form.save()

			return redirect ('/animadores/')
	else:
		form = agregar_desarrollador(instance=des)
	return render (request, 'agregar_desarrollador.html', locals())

	#...........................................................

def vista_editar_animador(request, id_ani):

	ani = Animador.objects.get(id=id_ani)

	if request.method == 'POST':
		form = agregar_animador(request.POST, request.FILES, instance=ani)
		if form.is_valid():

			ani = form.save()

			return redirect ('/animadores/')
	else:
		form = agregar_animador(instance=ani)
	return render (request, 'agregar_animador.html', locals())
#----------------------ELIMINAR---------------------------------------------------------

def vista_eliminar_juego(request, id_juego):

	j = Videojuego.objects.get(id=id_juego)
	j.delete()

	return redirect ('/')

#================LOGIN=======================================
#def vista_login(request):
#	usu = ""
#	pas = ""
#	if request.method == 'POST':
#		formulario = login_form(request.POST)
#		if formulario.is_valid():
#			usu = formulario.cleaned_data['usuario']
#			pas = formulario.cleaned_data['clave']
#			usuario = authenticate(username=usu, password=pas)
#			if usuario is not None and usuario.is_active:
#				login(request, usuario)
#				return redirect('/')
#
#			else:
#				msj="Usuario o Clave incorrectos"
#
#	formulario= login_form()
#	return render(request,'login.html', locals())


def vista_logout(request):
	logout(request)
	return redirect('/')

#================Registrar=========================

def vista_registrar(request):
	form_reg = RegisterForm()
	if request.method == 'POST':
		form_reg = RegisterForm(request.POST)
		if form_reg.is_valid():
			
			usuario = form_reg.cleaned_data['username']
			email   = form_reg.cleaned_data['email']
			password_one = form_reg.cleaned_data['password_one']
			password_two = form_reg.cleaned_data['password_two']

			u = User.objects.create_user(username=usuario,email=email,password=password_one)
			u.save() #guardar objeto u

			u = authenticate(username=usuario, password=password_one)
			if u is not None and u.is_active:
				login(request, u)

			return redirect ('/',locals())
		else:
			return render(request,'registrar.html',locals())

	return render(request,'registrar.html',locals())