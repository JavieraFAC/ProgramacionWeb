#from django.conf.urls.import url
from django.urls import path
from . import views



urlpatterns = [
    path('', views.Index, name='Index'),
    path('Register', views.Register, name='Register'),
    path('Carrito', views.Carrito, name='Carrito'),
    path('Productos', views.Productos, name='Productos'),
    path('Cuenta', views.Cuenta, name='Cuenta'),
    path('Planes', views.Planes, name='Planes'),
    path('Formulario', views.Formulario, name='Formulario'),
    path('Restaurantes', views.Restaurantes, name='Restaurantes'),
    
]