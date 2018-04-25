from django.urls import path, include
from rest_framework import routers
from aplicacion.models import *
from webservices.views import *

router = routers.DefaultRouter()
router.register(r'desarrollador', desarrollador_viewset)
router.register(r'plataforma', plataforma_viewset)
router.register(r'videojuego', videojuego_viewset)

urlpatterns = [
	path('api/', include(router.urls)),
	path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
]