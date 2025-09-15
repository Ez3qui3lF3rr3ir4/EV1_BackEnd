# BioBioMotors - Proyecto Django

Este proyecto es una aplicación de gestión de clientes, vehículos, servicios y órdenes de reparación desarrollada en Django.

---

## 🛠 Requisitos

* Python 3.10 o superior
* pip
* Un entorno virtual para aislar dependencias

---

## 🚀 Instalación y ejecución

Sigue estos pasos para preparar y ejecutar el proyecto:

1. **Crear un entorno virtual**

```bash
python -m venv [nombre_del_entorno_virtual]
```

2. **Copiar la carpeta del proyecto**
   Copia la carpeta `BioBioMotors` dentro de la raíz del entorno virtual.

3. **Activar el entorno virtual**
   Selecciona el intérprete de Python correspondiente al entorno virtual que acabas de crear.

4. **Navegar a la carpeta del proyecto**

```bash
cd [nombre_del_entorno_virtual]
cd BioBioMotors
```

5. **Instalar dependencias**

```bash
pip install -r requirements.txt
```

6. **Ejecutar el servidor de desarrollo**

```bash
python manage.py runserver
```

---

## 📂 Estructura del proyecto

* `BioBioMotors/` - Carpeta principal de la aplicación Django
* `AplicationWeb/` - Aplicación principal con modelos, vistas y rutas
* `requirements.txt` - Archivo con todas las dependencias necesarias

---

## ⚡ Notas

* Asegúrate de tener activado el entorno virtual antes de instalar paquetes o ejecutar el servidor.
* Puedes usar `python manage.py migrate` para aplicar migraciones si es la primera vez que ejecutas el proyecto.
* Crear un superusuario con `python manage.py createsuperuser` si necesitas acceder al panel de administración de Django.
* Para poblar la base de datos con datos de prueba, puedes usar el comando personalizado de Faker (\`python manage.py seed\_biobi
