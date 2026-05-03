# SmashUy
Proyecto final desarrollado en Python con Django.

# Descripción
SmashUy es una tienda online orientada a productos para Beach Tennis, Pádel y Tenis.
Incluye catálogo de productos, buscador, perfiles de usuario, autenticación y blog con contenido relacionado.

# Funcionalidades principales

# Usuarios
* Registro de usuarios
* Login / Logout
* Perfil de usuario
* Edición de perfil
* Avatar personalizado

# Productos
* Ver listado de productos
* Ver detalle de cada producto
* Buscar productos
* Crear productos (solo si el usuario está logueado)
* Editar productos (solo si el usuario está logueado)
* Eliminar productos (solo si el usuario está logueado)

# Otras secciones
* Home
* Acerca de mí
* Blog
* Panel Admin de Django

------------------------------------

# Cómo ejecutar el proyecto

1. Clonar repositorio:

```bash
git clone URL_DEL_REPOSITORIO
```

2. Crear entorno virtual:

```bash
python -m venv venv
```

3. Activar entorno virtual:

```bash
venv\Scripts\activate
```

4. Instalar dependencias:

```bash
pip install -r requirements.txt
```

5. Ejecutar migraciones:

```bash
python manage.py migrate
```

6. Iniciar servidor:

```bash
python manage.py runserver
```
----------------------------------

# Rutas principales

* `/` → Inicio
* `/productos/` → Productos
* `/buscar/` → Buscar productos
* `/about/` → Acerca de mí
* `/accounts/login/` → Login
* `/accounts/registro/` → Registro
* `/accounts/perfil/` → Perfil

