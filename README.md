# Construccion del proyecto

Para un proceso automático solo deberá ejecutar el la imagen de Docker

## En linux:

Ejecuta el siguiente comando:
    
    docker run -it --rm -p 8000:8000 imagenLinux

## En Windows:
Ejecuta el siguiente comando:

    docker run -it --rm -p 8000:8000 imagenWindows

*Nota:* Deberá tener Docker instalado en su sistema

## Manualmente

Para crear el entorno de ejecuccion se debera ejecutar los siguientes comandos:

Crear el entorno virtual de python:

    python -m venv venv

Se debe activar el entorno virtual, más info [aquí](https://docs.python.org/3/library/venv.html#:~:text=A%20virtual%20environment%20is%20created,the%20virtual%20environment%20are%20available.)

Si no desea crear este entorno puede pasar a los siguientes comandos directamente.

Instala las dependencias:

    pip install -r requirements.txt

Para la parte de archivos estaticos:

    python manage.py collectstatic --noinput

Inicia el proyecto localmente:

    python manage.py runserver

*Nota:* Se debe tener instalado Python versión 3.10 o posterior

# Base de datos

En la carpeta dbproject se encuentran los datos de prueba. En caso de querer verlos puede colocar esta carpeta en la carpeta mysql de WampServer.

Tambien se genera el constructor de la base de datos. Puede ejecutar directamente el archivo migration.sql para crear toda la base de datos Mysql.

# Notas finales:

El proyecto se basa en  el framework **Django** de Python, se usa principalmente python para el manejo de todo. 

La base de datos se maneja con modulos preestablecidos de **Django**, el manejo de todo se encuentra en el archivo crud.py en la carpeta *user*.

El programa usa una encriptacion para las contraseñas. A la hora de registrarse se validan los datos.

Gran parte de las tablas son preestablecidas por **Django**. Se puede observar más claramente las tablas creadas en este proyecto en el archivo models.py en la carpeta *user*. Los nombres de las variables son el nombre de la columna, despues de esta se indica el tipo de dato que es y sus otras instancias (si se pueden valores null, unicos, son primary key, etc), y el nombre de la clase representa parte del nombre de la tabla.

Los campos que son ForeignKey representan la relacion uno a muchos, los campos ManytoMany representan las relaciones muchos a muchos, esta misma crea la tabla intermediaria para la relacion (se pueder ver en la tabla *user_psychologist_clients*)

En la carpeta *media* se encuentran las imagenes generadas.

# Para pruebas

Para iniciar secion con alguno de los usuarios de prueba:

### Usuarios:
- juanb

- user2

- user3

- pruebauser3

### Psicólogos:
- psi

- psi2

- hola

>PARA TODOS LOS USUARIOS LA CONTRASEÑA ES: holaquehace?2

La contraseña no se puede ver en la base de datos ya que esta se encuentra encriptada...

---
### Autor:
Juan Esteban Cardona

---


