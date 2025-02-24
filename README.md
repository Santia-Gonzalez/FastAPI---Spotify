# README.md

## Resumen del proyecto
`omni-pro-app-base` es una librería de Django diseñada para ser utilizada como módulo base en aplicaciones que conectan con OMS. Proporciona funcionalidades comunes y configuraciones necesarias para el desarrollo y despliegue de aplicaciones Django.

## Fines de uso
- Proveer un conjunto de clases, vistas, serializadores y modelos predefinidos para facilitar el desarrollo de nuevas aplicaciones Django.
- Integrarse con servicios externos utilizando endpoints de autenticación OAuth2 y otras librerías necesarias.
- Configurar la administración del sistema en Django con Jazzmin.

## Instalación

Para instalar `omni-pro-app-base`, siga estos pasos:

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/Omnipro-Solutions/saas-app-base.git
    cd saas-app-base
    ```

2. Crear y activar un entorno virtual (opcional pero recomendado):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # En Linux o macOS
    venv\Scripts\activate     # En Windows
    ```

3. Instalar las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

## Inicialización del Proyecto

Para inicializar el proyecto y generar las migraciones necesarias, ejecute los siguientes comandos:

1. Configurar la base de datos (por defecto se usa SQLite):
   ```python
   DATABASE_URL=sqlite:///db.sqlite3 python make_migrations.py
   ```

2. Generar las migraciones:
    ```bash
    python make_migrations.py
    ```

## Estructura del Proyecto

- `omni_pro_base/`: Directorio principal que contiene todos los archivos de la aplicación.
  - `__init__.py`
  - `apps.py`: Configuración de la aplicación Django.
  - `backends.py`: Lógica para autenticar usuarios utilizando endpoints externos y configuraciones del sistema.
  - `http_request.py`: Clase que gestiona las peticiones HTTP al servicio de OMS.
  - `urls.py`: Registro de URLs para la integración con el servicio Health Check.
  - `util.py`: Funciones auxiliares, como obtener valores anidados en un diccionario.

- `omni_pro_base/admin/`: Subdirectorio que contiene los archivos necesarios para la configuración del administrador de Django.
  - `__init__.py`
  - `auth.py`, `base_admin.py`, `users.py`: Configuraciones específicas para el panel de administración.

- `omni_pro_base/forms/`: Formularios personalizados para la aplicación.
  - `__init__.py`
  - `users.py`: Implementa formularios personalizados para manipulación de usuarios y grupos.

- `omni_pro_base/migrations/`: Contiene las migraciones generadas por Django durante el desarrollo del proyecto.

- `omni_pro_base/models/`: Definición de modelos de datos.
  - `__init__.py`
  - `base_model.py`, `users.py`: Define un modelo base y los usuarios personalizados para la aplicación.

- `omni_pro_base/serializers/`: Serializadores para convertir objetos Python en JSON y viceversa.
  - `__init__.py`
  - `users.py`: Serialización de datos del usuario, incluyendo autenticación y recuperación de tokens.

- `omni_pro_base/settings/`: Configuraciones Django
  - `__init__.py`, `base.py`, `local.py`, `production.py`: Configuraciones base y específicas para entornos de desarrollo y producción.

- `omni_pro_base/static/vendor/omni/css/main.css`: Archivo CSS personalizado para el panel de administración.
  
- `omni_pro_base/tests/`: Directorio para pruebas unitarias y de integración (más tests podrían ser añadidos aquí).
  - `__init__.py`

- `omni_pro_base/views/`: Vistas de la API REST
  - `__init__.py`
  - `users.py`: Implementa vistas que permiten manejar usuarios y grupos, incluyendo autenticación.

## Funcionalidades

### Autenticación
1. **Configuración del backend de autenticación:**
   - Los archivos en `omni_pro_base/backends.py` implementan dos clases principales para la autenticación:
     - `SettingsBackend`: Utiliza las variables de configuración ADMIN_LOGIN y ADMIN_PASSWORD para verificar usuarios.
     - `AppUserBackend`: Llama a un servicio remoto (endpoint del OMS) para verificar los detalles del usuario.

2. **Serialización de datos de usuario:**
   - En `omni_pro_base/serializers/users.py`, se define una clase `UserLoginSerializer` que gestiona la autenticación y entrega tokens al usuario.

### Integración con servicios externos
- El archivo `http_request.py` proporciona métodos para realizar solicitudes HTTP a endpoints de servicios externos, como el servicio OMS.

### Modelos personalizados
- En `omni_pro_base/models/users.py`, se define un modelo `User` que hereda de Django's AbstractUser y agrega campos adicionales necesarios para la aplicación.

### API REST
- Las vistas en `omni_pro_base/views/__init__.py` y `omni_pro_base/views/users.py` proporcionan endpoints CRUD básicos para manejar usuarios y grupos. Además, se incluye un endpoint de login personalizado que devuelve tokens OAuth2.

### Configuración del panel de administración
- Las clases en los archivos de la carpeta `admin/` personalizan cómo Django adminstrará las instancias del modelo `User`.

## Herramientas Utilizadas

1. **Django 5.0**: Framework web de alto nivel basado en Python.
2. **Rest Framework**: Librería para API RESTful.
3. **OAuth2 Provider**: Para autenticación OAuth2.
4. **Celery**: Para procesamiento asíncrono y cola de tareas.
5. **Redis**: Como backend para la cola de tareas de Celery.
6. **Django Auditlog**: Para rastreo de cambios en modelos.

## Ejecución del Proyecto

1. **Configuración de entorno:**
   - Asegúrese de que las variables de entorno necesarias estén configuradas, como `SECRET_KEY`, `DATABASE_URL`, y `ADMIN_PASSWORD`.

2. **Corriendo el servidor:**
    ```bash
    python manage.py runserver
    ```

3. **Crear superusuario para acceder al panel de administración:**
    ```bash
    python manage.py createsuperuser
    ```

4. **Ejecutar migraciones y cargar datos iniciales (si es necesario):**
    ```bash
    python manage.py migrate
    ```
   
5. **Habilitar logs en producción:**
   - Configurar el archivo `settings/production.py` para configuraciones específicas de producción.

## Conclusión

Este repositorio proporciona una base sólida para desarrolladores que necesiten crear aplicaciones Django que interactúen con servicios externos, especialmente aquellos relacionados con OMS. La estructura y funcionalidades incluidas facilitan el desarrollo rápido y eficiente de nuevas aplicaciones.

---

Para más detalles sobre la configuración específica del entorno o la documentación de cada componente individual del sistema, por favor consulte los archivos `settings.py` y otros documentos en el repositorio.