
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.inventario.models import Prenda
from apps.empleados.models import Empleado
from apps.movimientos.models import Movimiento

@login_required
def dashboard(request):
    total_prendas = Prenda.objects.count()
    total_empleados = Empleado.objects.count()
    ultimos_movs = Movimiento.objects.select_related("prenda", "empleado").order_by("-fecha")[:10]
    bajos_stock = Prenda.objects.filter(cantidad_disponible__lte=3)[:10]
    return render(request, "dashboard.html", {
        "total_prendas": total_prendas,
        "total_empleados": total_empleados,
        "ultimos_movs": ultimos_movs,
        "bajos_stock": bajos_stock,
    })
