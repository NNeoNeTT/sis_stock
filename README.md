
# Uniformes Prevención SRL (Django)

Sistema web para gestionar inventario de uniformes, empleados y movimientos.
Incluye panel, login, CRUD básicos y despliegue en Render.

## Probar en local
```bash
python -m venv venv
source venv/bin/activate  # En Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acceso: ir a http://127.0.0.1:8000/login/ (crear superusuario en admin si querés)
```bash
python manage.py createsuperuser
```

## Rutas principales
- `/` Panel (dashboard)
- `/login` Ingreso
- `/inventario/` Lista y alta de prendas
- `/empleados/` Lista y alta de empleados
- `/movimientos/nuevo/` Registrar entrada/salida (actualiza stock)

## Despliegue en Render
1. Subí este repo a GitHub.
2. En Render, crea un nuevo servicio **Web (Python)** desde el repo.
3. Render leerá `render.yaml` y hará:
   - instalar dependencias
   - migrar
   - crear/asegurar el superusuario (de las env vars)
   - iniciar gunicorn
4. Tu app quedará online con el usuario:
   - Email: `solgaleano52@gmail.com`
   - Contraseña: `prevencion123`
