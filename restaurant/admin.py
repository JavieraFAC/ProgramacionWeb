from django.contrib import admin
from .models import Genero, Alumno, Contacto, CategoriaProd, Producto,Pedido,LineaPedido

# Define las clases admin primero
class CategoriaProdAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "update") 

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "update")  

# Registra tus modelos
admin.site.register(Genero)
admin.site.register(Alumno)
admin.site.register(Contacto)
admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Pedido)
admin.site.register(LineaPedido)