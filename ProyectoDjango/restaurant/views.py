from django.shortcuts import render

from .models import Alumno, Genero
# Create your views here.

def Index(request):
    context={}
    return render(request, 'restaurant/Index.html', context)

def Register(request):
    context={}
    return render(request, 'restaurant/Register.html', context)

def Carrito(request):
    context={}
    return render(request, 'restaurant/Carrito.html', context)

def Productos(request):
    context={}
    return render(request, 'restaurant/Productos.html', context)

def Cuenta(request):
    context={}
    return render(request, 'restaurant/Cuenta.html', context)

def Planes(request):
    context={}
    return render(request, 'restaurant/Planes.html', context)

def Formulario(request):
    context={}
    return render(request, 'restaurant/Formulario.html', context)

def Restaurantes(request):
    context={}
    return render(request, 'restaurant/Restaurantes.html', context)
