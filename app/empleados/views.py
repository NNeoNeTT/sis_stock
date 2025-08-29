
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ["nombre", "cedula", "puesto"]

@login_required
def lista(request):
    empleados = Empleado.objects.all().order_by("nombre")
    return render(request, "empleados/lista.html", {"empleados": empleados})

@login_required
def crear(request):
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("empleados_lista")
    else:
        form = EmpleadoForm()
    return render(request, "empleados/crear.html", {"form": form})
