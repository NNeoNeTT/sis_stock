
from django.contrib import admin
from .models import Movimiento
@admin.register(Movimiento)
class MovimientoAdmin(admin.ModelAdmin):
    list_display = ("tipo", "prenda", "empleado", "cantidad", "fecha")
    list_filter = ("tipo", "fecha")
    search_fields = ("prenda__categoria", "empleado__nombre")
