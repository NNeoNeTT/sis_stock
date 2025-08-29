
from django.urls import path
from . import views
urlpatterns = [
    path("", views.lista, name="prendas_lista"),
    path("nueva/", views.crear, name="prendas_crear"),
]
