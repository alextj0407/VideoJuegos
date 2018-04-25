from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
	user        = models.OneToOneField(User, on_delete=models.CASCADE)    
	foto        = models.ImageField(upload_to='perfiles', null=True, blank=True)
	nombre      = models.CharField(max_length = 100)

	def __str__ (self):
		return self.user.username

class Animador(models.Model):
	nombre      = models.CharField(max_length = 100)
	sede        = models.CharField(max_length = 100)
	f_fundacion = models.DateField()

	def __str__ (self):
		return self.nombre


class Valoraciones(models.Model):
	
	valoracion = models.IntegerField()
	reglas     = models.IntegerField()
	graficos   = models.IntegerField()
	controles  = models.IntegerField()

	def __str__ (self):
		return str(self.valoracion)


class Desarrollador(models.Model):
	nombre      = models.CharField(max_length = 100)
	sede        = models.CharField(max_length = 100)
	f_fundacion = models.DateField()

	animador    = models.ForeignKey(Animador, on_delete=models.CASCADE)

	def __str__ (self):
		return self.nombre

class Plataforma(models.Model):
	nombre      = models.CharField(max_length = 100)

	def __str__ (self):
		return self.nombre


class Videojuego(models.Model):
	
	nombre       = models.CharField(max_length = 100)
	descripcion  = models.TextField(max_length = 500)
	categoria    = models.CharField(max_length = 100)
	imagen       = models.ImageField(upload_to='foto', null=True, blank=True)


	f_lanzamiento= models.DateField()
	version      = models.CharField(max_length = 100)
	descargas    = models.IntegerField()
	precio       = models.DecimalField(max_digits = 6, decimal_places = 2)
	tamaño       = models.DecimalField(max_digits = 3, decimal_places = 2)

	desarrollador= models.ForeignKey(Desarrollador, on_delete=models.CASCADE)
	valoraciones = models.ForeignKey(Valoraciones, on_delete=models.CASCADE)

	plataforma  = models.ManyToManyField(Plataforma, null = True, blank = True)
	
	def __str__ (self):
		return self.nombre



