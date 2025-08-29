
from django.contrib import admin
from .models import Prenda
@admin.register(Prenda)
class PrendaAdmin(admin.ModelAdmin):
    list_display = ("categoria", "talla", "color", "cantidad_total", "cantidad_disponible")
    list_filter = ("categoria", "talla")
    search_fields = ("categoria", "talla", "color")
