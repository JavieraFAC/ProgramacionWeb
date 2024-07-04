from django.shortcuts import render, redirect
from .models import Producto
from .models import Alumno, Genero, Contacto
from .forms import ContactoForm
from .carro import Carro
from .models import Producto,Pedido,LineaPedido
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail


# Create your views here.

def Index(request):
    context={}
    carro=Carro(request)
    return render(request, 'restaurant/Index.html', context)

def Register(request):
    context={}
    return render(request, 'restaurant/Register.html', context)

def Carrito(request):
    context={}
    return render(request, 'restaurant/tienda.html', context)

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
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Index')
    else:
        form = ContactoForm()
    context= {'form' : form}
    return render(request, 'restaurant/Formulario.html', context)

def Restaurantes(request):
    context={}
    return render(request, 'restaurant/Restaurantes.html', context)



def tienda(request):
    
    productos = Producto.objects.all()
    
    return render(request, "restaurant/tienda.html", {"productos": productos})


def agregar_producto(request, producto_id):
    carro = Carro(request)  # Instancia de la clase Carro
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect("tienda")

def eliminar_producto(request, producto_id):
    carro = Carro(request)  # Instancia de la clase Carro
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect("tienda")

def restar_producto(request, producto_id):
    carro = Carro(request)  # Instancia de la clase Carro
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request):
    carro = Carro(request)  # Instancia de la clase Carro
    carro.limpiar_carro()
    return redirect("tienda")


@login_required(login_url='/autenticacion/logear')
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user) # damos de alta un pedido
    carro=Carro(request)  # cogemos el carro
    lineas_pedido=list()  # lista con los pedidos para recorrer los elementos del carro
    for key, value in carro.carro.items(): #recorremos el carro con sus items
        lineas_pedido.append(LineaPedido(
            producto_id=key,
            cantidad=value['cantidad'],
            user=request.user,
            pedido=pedido                 
            ))

    LineaPedido.objects.bulk_create(lineas_pedido) # crea registros en BBDD en paquete
    #enviamos mail al cliente
    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombreusuario=request.user.username,
        email_usuario=request.user.email
        

    )
    #mensaje para el futuro
    messages.success(request, "El pedido se ha creado correctamente")
    
    return redirect('../tienda')
    #return redirect('listado_productos')
    #return render(request, "tienda/tienda.html",{"productos":productos})
    

def enviar_mail(**kwargs):
    asunto="Gracias por el pedido"
    mensaje=render_to_string("restaurant/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "lineas_pedido": kwargs.get("lineas_pedido"),
        "nombreusuario":kwargs.get("nombreusuario") 
                       
        })

    mensaje_texto=strip_tags(mensaje)
    from_email="comiloncitox2@outlook.com"
    #to=kwargs.get("email_usuario")
    to="vejarcfelipea@gmail.com"
    send_mail(asunto,mensaje_texto,from_email,[to], html_message=mensaje)



def some_view(request):
    is_admin = request.user.is_staff
    context = {'is_admin': is_admin}
    return render(request, 'your_template.html', context)    

@login_required
def some_view2(request):
    context = {'is_admin': request.user.is_staff, 'is_not_admin': not request.user.is_staff}
    return render(request, 'your_template.html', context)


# views.py
@login_required(login_url='/autenticacion/logear')
def Productos(request):
    pedidos = Pedido.objects.filter(user=request.user).prefetch_related('lineapedido_set__producto').order_by('-created_at')
    
    # Crear una lista para almacenar cada pedido con su total calculado
    pedidos_con_totales = []
    
    # Calcular el total de cada pedido y almacenarlo en una lista
    for pedido in pedidos:
        total_pedido = sum(linea.producto.precio * linea.cantidad for linea in pedido.lineapedido_set.all())
        pedidos_con_totales.append({
            'pedido': pedido,
            'total': total_pedido,
        })
    
    return render(request, 'restaurant/Productos.html', {'pedidos': pedidos_con_totales})


