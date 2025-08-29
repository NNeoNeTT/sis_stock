
from django.contrib import admin
from .models import Empleado
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cedula", "puesto")
    search_fields = ("nombre", "cedula", "puesto")
