#from django.conf.urls.import url
from django.urls import path
from . import views
from .views import Formulario
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('', views.Index, name='Index'),
    path('Register', views.Register, name='Register'),
    path('tienda/', views.tienda, name='tienda'),
    path('Productos', views.Productos, name='Productos'),
    path('Cuenta', views.Cuenta, name='Cuenta'),
    path('Planes', views.Planes, name='Planes'),
    path('Formulario', views.Formulario, name='Formulario'),
    path('Restaurantes', views.Restaurantes, name='Restaurantes'),
    path("agregar/<int:producto_id>/",views.agregar_producto, name="agregar"),
    path("eliminar/<int:producto_id>/",views.eliminar_producto, name="eliminar"),
    path("restar/<int:producto_id>/",views.restar_producto, name="restar"),
    path("limpiar",views.limpiar_carro, name="limpiar"),
    path("procesar-pedido/", views.procesar_pedido, name="procesar_pedido"),
    path('admin/', admin.site.urls),
    path('limpiar/', views.limpiar_carro, name='limpiar'),
    path('adminPlatillos/', views.adminPlatillos, name='adminPlatillos'),
    #
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)