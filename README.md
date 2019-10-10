# Servidor para juego del gato

## Proyecto de la materia de Diseño de Sistemas Inteligentes

### Instalación

Es necesario el uso de un entorno virtual para utulizar solo las dependencias necesarias.

Para crear un entorno virtual es necesario instalar `virtualenv` con pip.

```bash
pip install virtualenv
```

O si se cuenta con `pip3`:

```bash
pip3 install virtualenv
```

Accedemos en la terminal hasta el directorio donde se clonó este repositorio y ejecutamos el comando:

```bash
virtualenv NOMBRE_ENTORNO_VIRTUAL
```

Esto generará una carpeta con el nombre que le dimos al entorno virtual, procederemos a activar el entorno virtual:

```bash
source NOMBRE_ENTORNO_VIRTUAL/bin/activate
```

Nuestra terminal deberá mostrar el nombre del entorno virtual en paréntesis `(entorno)`.

### Instalación de dependencias

Hay un archivo con las dependencias listadas, ejecute el siguiente comando para instalarlas en su entorno virtual:

```bash
pip install -r dependencias.txt
```

### Levantar el servidor

```bash
env FLASK_APP=server.py flask run
```

Deberá mostrar algo como lo siguiente:

```bash
* Serving Flask app "server.py"
* Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```