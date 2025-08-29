
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from django.db import transaction
from apps.inventario.models import Prenda
from apps.empleados.models import Empleado
from .models import Movimiento

class MovimientoForm(forms.ModelForm):
    class Meta:
        model = Movimiento
        fields = ["tipo", "prenda", "empleado", "cantidad", "observacion"]

@login_required
@transaction.atomic
def crear(request):
    if request.method == "POST":
        form = MovimientoForm(request.POST)
        if form.is_valid():
            mov = form.save(commit=False)
            prenda = mov.prenda
            if mov.tipo == "salida":
                if mov.cantidad > prenda.cantidad_disponible:
                    form.add_error("cantidad", "No hay stock suficiente para esta salida.")
                    return render(request, "movimientos/crear.html", {"form": form})
                prenda.cantidad_disponible -= mov.cantidad
            else:
                prenda.cantidad_disponible += mov.cantidad
                prenda.cantidad_total += mov.cantidad
            prenda.save()
            mov.save()
            return redirect("dashboard")
    else:
        form = MovimientoForm()
    return render(request, "movimientos/crear.html", {"form": form})
