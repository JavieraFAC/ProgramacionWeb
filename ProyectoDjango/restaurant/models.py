# models.py

from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import F,Sum, FloatField

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero', primary_key=True) 
    genero = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return str(self.genero)

class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    id_genero = models.ForeignKey('Genero', on_delete=models.CASCADE, db_column='idGenero')  
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)  
    activo = models.IntegerField()

    def __str__(self):
        return str(self.nombre) + " " + str(self.apellido_paterno)   

SECTOR_CHOICES = [
    ('vinadelmar', 'Viña del Mar'),
    ('valpo', 'Valparaíso'),
    ('quilpue', 'Quilpué'),
    ('concon', 'Concón'),
]

class Contacto(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    correo = models.CharField(unique=True, max_length=100, blank=True, null=True)
    sector = models.CharField(max_length=50, choices=SECTOR_CHOICES)
    comentario = models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class CategoriaProd(models.Model):
    nombre = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "categoriaProd"
        verbose_name_plural = "categoriasProd"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    categorias = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tienda", null=True, blank=True)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


'''''

User = get_user_model()

class Pedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    @property
    def total(self):
        return self.lineapedido_set.aggregate(
            total=Sum(F("producto_id__precio") * F("cantidad"), output_field=FloatField())
        )["total"]

    class Meta:
        db_table = 'pedidos'
        verbose_name = "pedido"
        verbose_name_plural = "pedidos"
        ordering = ['id']


class LineaPedido(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    producto= models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto.nombre}'

    class Meta:
        db_table = 'lineapedidos'
        verbose_name = "Linea pedido"
        verbose_name_plural = "Lineas pedidos"
        ordering = ['id'] '''





User=get_user_model()
class Pedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) # Cuando se elimine un usuario sus pedidos se eliminirán en cascada
    created_at=models.DateTimeField(auto_now_add=True)   #Para le fecha de pedido automática

    @property
    def total(self):
        return self.lineapedido_set.aggregate(

            total=Sum(F("precio")*F("cantidad"), output_field=FloatField())

        )["total"] or FloatField(0)

    def __str__(self):
        return self.id


    class Meta:
        db_table='pedidos'
        verbose_name='Pedido'
        verbose_name_plural='Pedidos'
        ordering=['id']


class LineaPedido(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE) 
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} de {self.producto.nombre}'

    class Meta:
        db_table='lineapedidos'
        verbose_name='Línea Pedido'
        verbose_name_plural='Líneas Pedidos'
        ordering=['id']
