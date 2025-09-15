from django.db import models

class Cliente (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Vehiculo (models.Model):
    id = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=100)
    anio = models.SmallIntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patente} {self.cliente}"
    
class Servicio (models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=500)
    precio = models.BigIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.descripcion} {self.precio}"
    
class OrdenReparacion (models.Model):
    id = models.AutoField(primary_key=True)
    fecha_ingreso = models.DateTimeField()
    fecha_salida = models.DateTimeField(null=True,blank=True)
    estado = models.CharField(max_length=20, choices=[
        ("ingresado","Ingresado"),
        ("en_proceso","En Proceso"),
        ("finalizado","Finaliazdo")
        ], default="Ingresado")
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    servicios = models.ManyToManyField(Servicio, blank=True)
    monto_total = models.BigIntegerField()

    def __str__(self):
        return f"{self.id} {self.monto_total}"