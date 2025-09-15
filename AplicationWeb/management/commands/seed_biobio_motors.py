from AplicationWeb.models import Cliente,Vehiculo,OrdenReparacion,Servicio
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta
from faker import Faker
import random

class Command(BaseCommand):
    def handle(self,*args,**options):
        fake = Faker("es_ES")

        OrdenReparacion.objects.all().delete()
        Servicio.objects.all().delete()
        Vehiculo.objects.all().delete()
        Cliente.objects.all().delete()

        clientes = []
        for _ in range(2):
            cliente = Cliente.objects.create(
                nombre = fake.first_name(),
                apellido = fake.last_name(),
                telefono = fake.msisdn()[:9],
                email = fake.email()
            )
            clientes.append(cliente)

        vehiculos = []
        for a in clientes:
            vehiculo = Vehiculo.objects.create(
                patente = fake.bothify(text="??####"),
                marca = fake.company(),
                modelo = fake.word(),
                anio = random.randint(2000,2025),
                cliente = cliente
            )
            vehiculos.append(vehiculo)
        
        servicios = []
        for _ in range(3):
            servicio = Servicio.objects.create(
                nombre=fake.word(),
                descripcion=fake.sentence(),
                precio=random.randint(10000, 50000)
            )
            servicios.append(servicio)


        for _ in range(2):
            vehiculo = random.choice(vehiculos)
            orden = OrdenReparacion.objects.create(
                vehiculo=vehiculo,
                fecha_ingreso=fake.date_time_between(start_date='-30d', end_date='now'),
                fecha_salida=fake.date_time_between(start_date='now', end_date='+10d'),
                estado=random.choice(['ingresado','en_proceso','finalizado']),
                monto_total=0
            )
            seleccion_servicios = random.sample(servicios, k=random.randint(1, 3))
            orden.servicios.set(seleccion_servicios)

            total = sum(s.precio for s in seleccion_servicios)
            orden.monto_total = total
            orden.save()

        self.stdout.write(self.style.SUCCESS('Datos de prueba generados correctamente ✅'))