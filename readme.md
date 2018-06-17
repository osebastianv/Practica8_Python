# WordPlease

*WordPlease* es una aplicación de backend que simula una plataforma de blogging que permite a los usuarios registrarse para crear su blog personal y poder publicar artículos de diferentes contenidos.

La aplicación se ha realizado en *python* utilizando el framework *Django*. Contiene un Sitio Web y una API REST.

## 1. Entorno (versiones)

| Entorno | Versión |
| ------ | ------ |
| Pycharm Pro | 2018.1.3 |
| Python | 3.6 |

| Paquete | Versión |
| ------ | ------ |
| Django | 2.0.5 |
| djangorestframework | 3.8.2 |

| S.O. | Versión |
| ------ | ------ |
| Windows  | 7 Pro (64 bits) |

| Navegador | Versión |
| ------ | ------ |
| chrome | 67.0.3396.87 (Build oficial) (64 bits) |


##	2. Preparando el entorno
Una vez abierto el proyecto con *pycharm*, vamos a realizar una serie de pasos previos a la ejecución de la aplicación.

#### 2.1 Configurar y activar entorno

- Configurar entorno. En caso de no tener configurado el entorno (no exista la carpeta *venv* en la raiz de mi proyecto), se configurará de la siguiente manera:
    -  En el menú File / Settings, nos vamos a la opción Project / Project Interpreter y pulsando el botón de project interpreter (arriba a la derecha), seleccionamos add.
        -  Location: seleccionamos nuestra carpeta \venv.
        Ruta-mi-proyecto\venv
        - Base interpreter: seleccionamos nuestro intértrete de python.
        c:\Users\mi-usuario\AppData\Local\Programs\Python\Python36-32\python.exe

    - Instalamos los paquetes necesarios. Para ello pulsamos el botón + y buscamos *Django* del repositorio. Lo seleccionamos y lo instalamos pulsando el botón *Install package*. Repetir lo mismo con el paquete *djangorestframework*.

    **Nota**: Al configurar el entorno, en la carpeta de trabajo debe existir una nueva carpeta llamada venv.
    Ruta-mi-proyecto\venv

- Activar el entorno. Una vez configurado, hay que activarlo. Abrimos el terminal de pycharm (te posiciona en la carpeta de trabajo, Ruta-mi-proyecto). Tecleamos:
```sh
cd venv/Scripts
activate
```
-   Para saber si el entorno está bien activado, en la terminal debe aparecer, el literal *venv* (a la izquierda de la ruta):
    (venv) Ruta-mi-proyecto\
 Ahora estamos en Ruta-mi-proyecto\venv\Scripts. Volvemos a la ruta de nuestro proyecto:
```sh
cd..
cd..
```
Y ya estamos en Ruta-mi-proyecto\

#### 2.2 Crear base de datos sqlite3 y usuario administrador

- Crear la base de datos sqlite3. Nos vamos a la terminal de pycharm posicionada en Ruta-mi-proyecto y tecleamos:
```sh
python manage.py migrate
```

- Crear el usuario administrador:
```sh
python manage.py createsuperuser
```
```sh
User: admin
Email: (lo podemos dejar vacío)
Password:la-que-queráis (que sea supersegura)
```

#### 2.3 Arranque del servidor

Para arrancar el servidor, nos vamos a la terminal en la Ruta-mi-proyecto y teclearemos:
```sh
python manage.py runserver
```

#### 2.4 Configurar run / debug y arranque del servidor

Existe otra manera de arrancar el servidor sin utilizar la terminal y que además, te permita utilizar el debug:

- Configurar run / debug: arriba a la derecha, en el combo box, seleccionamos edit configuration, pulsamos el botón + y seleccionamos python.
    - Name: Django server
    - Script path: Ruta-mi-proyecto\manage.py
    - Parameters: runserver
    - Python Interpreter: Project default. Importante poner por defecto por si en el futuro cambiamos la versión de python.
    - Working directory: Ruta-mi-proyecto

 - Arranque del servidor. Una vez configurado el servidor, arriba a la derecha del menú de pycharm, seleccionamos nuestra configuración *Django Server* y pulsamos el botón > (play).

## 3. Modelo de datos

La aplicación *WordPlease* contendrá las siguientes tablas:

### 3.1 Tabla de usuarios (User)
Tabla del sistema, cada usuario tendrá su blog personal de publicaciones de artículos.
```sh
id              Identificador de usuario (numérico único)
username        Nombre de usuario (único)
password        Contraseña (hasheada)
first_name      Nombre
last_name       Apellidos
email           Correo electrónico
is_superuser    Si el usuario es administrador
is_active       Si el usuario está activo
...
```
**Nota:** En el sitio web se puede registrar un nuevo usuario que no sea administrador. En la zona de administración, se pueden crear, modificar y eliminar todo tipo de usuarios, incluidos administradores.

### 3.2 Tabla de categorías (Category)
Tabla de categorías de artículos publicados. Un artículo puede tener varias categorías asociadas.
```sh
id              Identificador de categoría (numérico único)
name            Nombre de la categoría
created_on      Fecha de creación
modified_on     Fecha de modificación
```

**Nota:** Solo se pueden crear, modificar y eliminar categorías en la zona de administración. Debe de haber al menos una categoría creada para poder crear un nuevo artículo.

### 3.3 Tabla de artículos (Posts)
Tabla de artículos de cada usuario.
```sh
id              Identificador de artículo (numérico único)
title           Título
intro           Introducción
body            Cuerpo del artículo
url             Ruta a la imagen o video del artículo
content_type    Tipo de archivo/formato (ej: 'image/jpg', 'video/mp4', ...)
published       Si el artículo está publicado
published_on    Fecha de publicación
created_on      Fecha de creación
modified_on     Fecha de modificación
categories      Categorías asociadas al artículo (una o varias)
owner_id        Usuario propietario del artículo (solo uno)
```
**Nota:** En el sitio web se puede crear un nuevo artículo. En la zona de administración, se pueden crear, modificar y eliminar artículos.

## 4. Administración Sitio Web

Antes de entrar en el sitio web, vamos a necesitar crear categorías para clasificar artículos. Para ello entraremos en la zona de administrador:

http://127.0.0.1:8000/admin

Nos logeamos con el usuario admin creado al preparar el entorno. Solo los usuarios administradores pueden acceder a esta zona.

Dentro de la zona de administración tendremos creadas dos zonas: zona de usuarios y zona de artículos.

### 4.1 Administración de usuarios

Contiene un enlace de grupos y otro de usuarios. Si pulsamos en *Users*, saldrá una lista con todos los usuarios registrados.

Pulsamos en el usuario de administración y nos sale la edición del usuario. Aprovechamos y le incluimos los campos *first_name*, *last_name* y lo guardamos (se utilizan en el sitio web, así no verás campos de bienvenida de usuario en blanco).

En esta vista podemos crear, actualizar y eliminar los usuarios.

### 4.2 Administración de artículos

Contiene un enlace de categorías y otro de artículos.
- Si pulsamos en *Categorys*, saldrá una lista con todas las categorías creadas. En esta vista podemos crear una nueva categoría o bien, entrando en una de ellas, actualizar y eliminar la categoría seleccionada.

    Aprovechamos y creamos un par de categorías que necesitaremos cuando entremos en la zona del sitio web.

    **Nota:** Recuerda que las categorías solo se crean en esta zona.

- Si pulsamos en *posts*, saldrá una lista de todos los artículos creados. Se podrán realizar búsquedas y filtrar por publicación y categorías. En esta vista podemos crear un nuevo artículo o bien, entrando en uno de ellos, actualizar y eliminar el artículo seleccionado.

    **Nota:** solo seran visibles en el sitio web los artículos publicados, los no publicados solo los podrán ver sus usuarios o un usuario administrador.

## 5. Sitio Web

Vamos a entrar en el sitio web. Utilizaremos el usuario admin (que es administrador), como ejemplo.

El sitio web contiene las siguientes características:
- En la página principal, deberán aparecer los últimos posts publicados por los usuarios.

    http://127.0.0.1:8000/
    Contiene paginación de 5 páginas por vista.

- En la URL /blogs/, se deberá mostrar un listado de los blogs de los usuarios que hay en la plataforma.

    http://127.0.0.1:8000/blogs/
    Contiene paginación de 5 páginas por vista.

- El blog personal de cada usuario, se cargará en la URL /blogs/<nombre_de_usuario>/ donde aparecerán todos los posts del usuario ordenados de más actual a más antiguo (los últimos posts primero).

    http://127.0.0.1:8000/blogs/admin

- En la URL /blogs/<nombre_de_usuario/<post_id> se deberá poder ver el detalle de un post.

    http://127.0.0.1:8000/blogs/admin/1

- Un post estará compuesto de: título, texto a modo de introducción, cuerpo del post, URL de imagen o vídeo destacado (opcional), fecha y hora de publicación (para poder publicar un post en el futuro), categorías en las que se publican (un post puede publicarse en una o varias categorías). Las categorías deben poder ser gestionadas desde el administrador.

- Tanto en la página principal como en el blog personal de cada usuario, se deberán listar los posts con el mismo diseño/layout. Para cada post deberá aparecer el título, la imagen destacada (si tiene) y el resumen.

    Se ha  utilizado un diseño basado en la práctica 4 de frontend avanzado. Para los formularios, se ha incluido bootstrap para generar un diseño sencillo.

- En la URL /new-post deberá mostrarse un formulario para crear un nuevo post. Para acceder a esta URL se deberá estar autenticado. En formulario para crear el post deberá identificar al usuario autenticado para publicar el POST en el blog del usuario.

    http://127.0.0.1:8000/new-post/

    El formulario permite que no se meta ningún archivo asociado, pero si se incluye uno, este debe ser de tipo 'imagen' o de tipo 'video', y no superar los 5MB de tamaño.

    Además, está seleccionado por defecto que se publica el artículo. En caso de publicarse, se inserta la fecha de publicación.

    Cualquier futuro cambio en el artículo solo se podrá realizar en el área de administración.

- En la URL /login el usuario podrá hacer login en la plataforma.

    http://127.0.0.1:8000/login

- En la URL /logout el usuario podrá hacer logout de la plataforma.

    La opción de logout se visualiza en la cabecera solo cuando un usuario esté logeado.

- En la URL /signup el usuario podrá registrarse en la plataforma indicando su nombre, apellidos, nombre de usuario, e-mail y contraseña.

    http://127.0.0.1:8000/signup

    Una vez registrado el nuevo usuario, automáticamente se logea con ese usuario y entra en el sistema.

## 6. API REST

Adicionalmente, se ha implementado una API REST para que pueda ser utilizada para futuros desarrollos (para consumo de apps móviles, por ejemplo).

Deberá tener los siguientes endpoints:

### 6.1 API de usuarios

- Endpoint que permita a cualquier usuario registrarse indicando su nombre, apellidos, nombre de usuario, e-mail y contraseña.

    *Navegador:*

    http://127.0.0.1:8000/api/v1/users/
    Mostrará un listado de todos los usuarios creados. Adicionalmente, creará un formulario en la parte inferior que permitirá crear un nuevo usuario.

    Otra forma de crear un usuario sería mediante un cliente REST tipo *Insomnia* o *Postman*.

    *Insomnia:*
```sh
    Operación: POST
    URL: http://127.0.0.1:8000/api/v1/users/
    Multipart: username, first_name, last_name, email, password (crear los campos con sus valores)
 ```

```sh
{
	"first_name": "usuario",
	"last_name": "user1",
	"username": "user1",
	"email": "",
	"password": "pbkdf2_sha256$100000$sIV0u43stZpa$fnSvMosowz0gcvQhQuYoPuA8B0cjPb07Pi7BXZLforo="
}
```

- Endpoint que permita ver el detalle de un usuario. Sólo podrán ver el endpoint de detalle de un usuario el propio usuario o un administrador.

    *Insomnia:*
```sh
    Operación: GET
    URL: http://127.0.0.1:8000/api/v1/users/1/
    Basic Auth: username, password
 ```

```sh
{
	"id": 1,
	"username": "admin",
	"first_name": "Usuario",
	"last_name": "admin",
	"email": "",
	"password": "pbkdf2_sha256$100000$2Tqbcix3FHLm$6EvAK41xw1499D5T+xyJ29En6Rhzwm8oEIEPHNF11Gg="
}
```

- Endpoint que permita actualizar los datos de un usuario. Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador.

    *Navegador:*

    http://127.0.0.1:8000/api/v1/users/2/
    Mostrará el detalle del usuario. Adicionalmente, creará un formulario en la parte inferior que permitirá actualizar el usuario.

    *Insomnia:*
```sh
    Operación: PUT
    URL: http://127.0.0.1:8000/api/v1/users/2/
    Multipart: username, first_name, last_name, email, password
    Basic Auth: username, password
 ```

```sh
{
	"id": 2,
	"username": "user1",
	"first_name": "Usuario",
	"last_name": "user1 cambiado",
	"email": "",
	"password": "pbkdf2_sha256$100000$USRKvHnWAx1a$K7/WoeBPvkrrpjcR0XScupgfrv2jTuyItBzHpJ+nf/Y="
}
```

**Nota:** en la operación PUT, en la pestaña multipart, hay que poner TODOS los campos de la tabla, aunque no se cambien sus valores.

- Endpoint que permita eliminar un usuario (para darse de baja). Sólo podrán usar el endpoint de un usuario el propio usuario o un administrador.

    *Insomnia:*
```sh
    Operación: DELETE
    URL: http://127.0.0.1:8000/api/v1/users/2/
    Basic Auth: username, password
 ```

```sh
    204 No Content
    No body returned for response
```


### 6.2 API de blogs
- Un endpoint que no requiera autenticación y devuelva el listado de blogs que hay en la plataforma con la URL de cada uno. Este endpoint debe permitir buscar blogs por el nombre del usuario y ordenarlos por nombre.

    *Navegador:*

    http://127.0.0.1:8000/api/v1/blogs/
    http://127.0.0.1:8000/api/v1/blogs/?search=admin
    http://127.0.0.1:8000/api/v1/blogs/?ordering=first_name

### 6.3 API de posts

- Un endpoint para poder leer los artículos de un blog de manera que, si el usuario no está autenticado, mostrará sólo los artículos publicados. Si el usuario está autenticado y es el propietario del blog o un administrador, podrá ver todos los artículos (publicados o no). En este endpoint se deberá mostrar únicamente el título del post, la imagen, el resumen y la fecha de publicación. Este endpoint debe permitir buscar posts por título o contenido y ordenarlos por título o fecha de publicación. Por defecto los posts deberán venir ordenados por fecha de publicación descendente.

> Sin autenticar:
    *Insomnia:*
```sh
    Operación: GET
    URL: http://127.0.0.1:8000/api/v1/posts/
 ```
```sh
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"owner": 1,
			"title": "Título 1",
			"intro": "Introducción 1",
			"url": "http://127.0.0.1:8000/media/Imagen_2P38NJO.jpg",
			"published_on": "2018-06-17T14:35:05.744006Z"
		},
		{
			"id": 2,
			"owner": 2,
			"title": "Título 2",
			"intro": "Introducción 2",
			"url": null,
			"published_on": "2018-06-17T14:25:40.142637Z"
		}
	]
}
```


> Autenticado (admin):
    *Insomnia:*


```sh
    Operación: GET
    URL: http://127.0.0.1:8000/api/v1/posts/
    Basic Auth: username, password
 ```
```sh
{
	"count": 2,
	"next": null,
	"previous": null,
	"results": [
		{
			"id": 1,
			"owner": 1,
			"title": "Título 1",
			"intro": "Introducción 1",
			"url": "http://127.0.0.1:8000/media/Imagen_2P38NJO.jpg",
			"published_on": "2018-06-17T14:35:05.744006Z"
		},
		{
			"id": 2,
			"owner": 2,
			"title": "Título 2",
			"intro": "Introducción 2",
			"url": null,
			"published_on": "2018-06-17T14:25:40.142637Z"
		},
		{
			"id": 3,
			"owner": 1,
			"title": "Título 3",
			"intro": "Introducción 3",
			"url": null,
			"published_on": null
		},
		{
			"id": 4,
			"owner": 2,
			"title": "Título 4",
			"intro": "Introducción 4",
			"url": null,
			"published_on": null
		}
	]
}
```

- Un endpoint para crear posts en el cual el usuario deberá estar autenticado. En este endpoint el post quedará publicado automáticamente en el blog del usuario autenticado.

    *Navegador:*

    http://127.0.0.1:8000/api/v1/posts/
    Mostrará un listado de los artículos creados. Adicionalmente, creará un formulario en la parte inferior que permitirá crear un nuevo artículo.

    *Insomnia:*

```sh
    Operación: POST
    http://127.0.0.1:8000/api/v1/posts/
    Multipart: title, intro, body, url, categories
    Basic Auth: username, password
    Header: Content-Type: multipart/form-data
 ```

```sh
 {
    "id": 5,
    "owner": 1,
    "title": "Título 5",
    "intro": "Introducción 5",
    "url": "http://127.0.0.1:8000/media/bici4_jLcc1QW.jpg",
    "published_on": "2018-06-17T16:15:55.396613Z"
}
```

- Un endpoint de detalle de un post, en el cual se mostrará toda la información del POST. Si el post no es público, sólo podrá acceder al mismo el dueño del post o un administrador.

    *Navegador*

    http://127.0.0.1:8000/api/v1/posts/1/
    Mostrará el detalle del artículo. Adicionalmente, creará un formulario en la parte inferior que permitirá modificar el artículo.

- Un endpoint de actualización de un post. Sólo podrá acceder al mismo el dueño del post o un administrador.

    http://127.0.0.1:8000/api/v1/posts/2/
    Mostrará el detalle del artículo. Adicionalmente, creará un formulario en la parte inferior que permitirá modificar el artículo.

    *Insomnia:*
```sh
    Operación: PUT
    URL: http://127.0.0.1:8000/api/v1/posts/2/
    Multipart: title, intro, body, url, categories (todos los campos)
    Basic Auth: username, password
 ```

```sh
 {
    "id": 2,
    "owner": 2,
    "title": "Título 2",
    "intro": "Introducción 2 Cambiada",
    "body": "Cuerpo artículo 2",
    "url": "http://127.0.0.1:8000/media/Imagen_jLcc1QW.jpg",
    "published_on": "2018-06-17T14:25:40.142637Z"
    "categories": {
        1
    }
}
```

- Un endpoint de borrado de un post. Sólo podrá acceder al mismo el dueño del post o un administrador.

    *Insomnia:*
```sh
    Operación: DELETE
    URL: http://127.0.0.1:8000/api/v1/posts/2/
    Basic Auth: username, password
 ```

```sh
    204 No Content
    No body returned for response
```

 ## 7. Paginación

 La API contiene paginación, si se superan los 5 elementos, el sistema realiza de forma automática la paginación.

