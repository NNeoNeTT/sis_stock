
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from .models import Prenda

class PrendaForm(forms.ModelForm):
    class Meta:
        model = Prenda
        fields = ["categoria", "talla", "color", "cantidad_total", "cantidad_disponible"]

@login_required
def lista(request):
    prendas = Prenda.objects.all()
    return render(request, "inventario/lista.html", {"prendas": prendas})

@login_required
def crear(request):
    if request.method == "POST":
        form = PrendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("prendas_lista")
    else:
        form = PrendaForm()
    return render(request, "inventario/crear.html", {"form": form})
