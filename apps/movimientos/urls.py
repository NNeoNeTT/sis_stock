
from django.urls import path
from . import views
urlpatterns = [
    path("nuevo/", views.crear, name="mov_crear"),
]
