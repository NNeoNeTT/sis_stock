
from django.urls import path
from . import views
urlpatterns = [
    path("", views.lista, name="empleados_lista"),
    path("nuevo/", views.crear, name="empleados_crear"),
]
