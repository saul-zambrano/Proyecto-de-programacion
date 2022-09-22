from pyexpat import model
from django.db import models

# Create your models here.
class CategoriaProducto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f'Categoria Producto: {self.id}: {self.nombre}'


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=15)
    nombres = models.CharField(max_length=60)
    apellidos = models.CharField(max_length=60)
    celular = models.CharField(max_length=10)
    dni = models.CharField(max_length=10)

    def __str__(self) -> str:
        return f'Cliente: {self.id}: {self.nombre} {self.email} {self.password}'


class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    pais = models.CharField(max_length=60)
    provincia = models.CharField(max_length=60)
    ciudad = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f'Direccion: {self.id}: IdCliente{self.id_cliente} {self.pais} {self.ciudad} {self.direccion}'

class MetodoPago(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f'Metodo de pago: {self.id}: {self.nombre}'


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    cat_prod = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=70)
    precio = models.FloatField()
    stock = models.IntegerField()
    imagen = models.CharField(max_length=60)

    def __str__(self) -> str:
        return f'Producto: {self.id}: {self.nombre} {self.descripcion} {self.precio} {self.stock}'

class Orden(models.Model):
    id = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_metodo_pago = models.ForeignKey(MetodoPago, on_delete=models.CASCADE)
    id_domicilio = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    total = models.FloatField()

    def __str__(self) -> str:
        return f'Orden: {self.id}: {self.id_usuario} {self.id_metodo_pago} {self.id_domicilio} {self.total}'

class OrdenDetalle(models.Model):
    id = models.AutoField(primary_key=True)
    id_orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=12, decimal_places=2)
    total = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self) -> str:
        return f'Orden Detalle: {self.id}: {self.id_orden} {self.id_producto} {self.cantidad} {self.precio}'

class Carrito(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self) -> str:
        return f'Carrito: {self.id}: {self.id_usuario} {self.id_producto} {self.cantidad}'