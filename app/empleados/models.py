
from django.db import models

class Empleado(models.Model):
    nombre = models.CharField("Nombre y apellido", max_length=100)
    cedula = models.CharField("Nº de cédula", max_length=20, unique=True)
    puesto = models.CharField("Puesto de cobertura", max_length=100)

    def __str__(self):
        return f"{self.nombre} ({self.cedula})"
