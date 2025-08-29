
from django.db import models
from apps.empleados.models import Empleado
from apps.inventario.models import Prenda

class Movimiento(models.Model):
    TIPOS = [("entrada", "Entrada"), ("salida", "Salida")]
    tipo = models.CharField("Tipo", max_length=10, choices=TIPOS)
    prenda = models.ForeignKey(Prenda, on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.PositiveIntegerField("Cantidad")
    fecha = models.DateTimeField("Fecha", auto_now_add=True)
    observacion = models.CharField("Observación", max_length=200, blank=True)

    class Meta:
        ordering = ["-fecha"]

    def __str__(self):
        return f"{self.get_tipo_display()} - {self.prenda} ({self.cantidad})"
