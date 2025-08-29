
from django.db import models

class Prenda(models.Model):
    CATEGORIAS = [
        ("camisa_m_corta", "Camisa manga corta"),
        ("camisa_m_larga", "Camisa manga larga"),
        ("pantalon_gala", "Pantalón de gala"),
        ("remera_blanca", "Remera blanca"),
        ("remera_negra", "Remera negra"),
        ("insignia_chica", "Insignia chica"),
        ("insignia_grande", "Insignia grande"),
        ("corbata", "Corbata"),
        ("silbato", "Silbato"),
        ("revolvera", "Revolvera"),
        ("cinturon", "Cinturón"),
        ("tahali", "Tahalí"),
        ("tonfa", "Tonfa"),
        ("pantalon_operativo", "Pantalón operativo"),
        ("chaqueta_operativa", "Chaqueta operativa"),
        ("gorra_femenina", "Gorra femenina"),
        ("gorra_masculina", "Gorra masculina"),
        ("keppy_gala", "Keppy gala"),
        ("keppy_operativo", "Keppy operativo"),
        ("campera", "Campera"),
    ]
    categoria = models.CharField("Categoría", max_length=30, choices=CATEGORIAS)
    talla = models.CharField("Talla", max_length=10)
    color = models.CharField("Color", max_length=30, blank=True)
    cantidad_total = models.PositiveIntegerField("Cantidad total", default=0)
    cantidad_disponible = models.PositiveIntegerField("Cantidad disponible", default=0)

    class Meta:
        verbose_name = "Prenda"
        verbose_name_plural = "Prendas"
        ordering = ["categoria", "talla"]

    def __str__(self):
        return f"{self.get_categoria_display()} - {self.talla}"
