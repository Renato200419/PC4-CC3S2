# Proyecto de Gestión de Usuarios y Catálogo de Productos

Este proyecto implementa dos microservicios:

1. **Gestión de Usuarios**: Permite crear, leer, actualizar y eliminar usuarios.
2. **Catálogo de Productos**: Permite crear, leer, actualizar y eliminar productos asociados a usuarios existentes.

Ambos servicios están desarrollados en Python utilizando Flask y Peewee como ORM. Se aplican principios SOLID, y se incluye una suite de pruebas unitarias y de integración con métricas de cobertura de código y complejidad ciclomática.

## Tabla de Contenidos

- [Requisitos Previos](#requisitos-previos)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración del Entorno](#configuración-del-entorno)
- [Ejecución de los Servicios](#ejecución-de-los-servicios)
- [Ejecución de Pruebas y Cobertura de Código](#ejecución-de-pruebas-y-cobertura-de-código)
- [Métricas de Complejidad Ciclomática](#métricas-de-complejidad-ciclomática)

## Requisitos Previos

- Docker y Docker Compose instalados en tu sistema.
- Python 3.8 o superior 

## Estructura del Proyecto

```
/project
|-- docker-compose.yml
|-- requirements.txt
|-- README.md
|-- product_catalog
|   |-- Dockerfile
|   |   |-- src
|   |   |-- __init__.py
|   |   |-- app.py
|   |   |-- controllers.py
|   |   |-- services.py
|   |   `-- repositories.py
|   `-- tests
|       |-- test_product_controllers.py
|       `-- test_product_services.py
`-- user_management
    |-- Dockerfile
    |-- src
    |   |-- __init__.py
    |   |-- app.py
    |   |-- controllers.py
    |   |-- services.py
    |   `-- repositories.py
    `-- tests
        |-- test_user_controllers.py
        `-- test_user_services.py
```

## Configuración del Entorno

### 1. Clonar el Repositorio

Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Renato200419/PC4-CC3S2.git
```

### 2. Configurar Docker Compose

El archivo `docker-compose.yml` orquesta ambos servicios y define una red compartida para la comunicación entre ellos.

## Ejecución de los Servicios

Para construir y ejecutar los servicios, utilizamos Docker Compose:

```bash
docker-compose up --build -d
```

Este comando hará lo siguiente:

- Construirá las imágenes Docker para `user_management` y `product_catalog`.
- Creará y ejecutará los contenedores.
- Expondrá los puertos 5000 (Gestión de Usuarios) y 5001 (Catálogo de Productos).

Los servicios estarán accesibles en:

- **Gestión de Usuarios**: `http://localhost:5000/users`
- **Catálogo de Productos**: `http://localhost:5001/products`

## Ejecución de Pruebas y Cobertura de Código

### 1. Acceder al Contenedor

Para ejecutar las pruebas y generar el reporte de cobertura de código, primero accedemos al contenedor correspondiente. Se puede hacer utilizando `docker exec` o abriendo una terminal interactiva.

**Ejemplo para `user_management`:**

```bash
# Obtener el ID o nombre del contenedor
docker ps

# Acceder al contenedor
docker exec -it tu_contenedor_user_management /bin/bash
```

### 2. Ejecutar las Pruebas y Generar Cobertura

Dentro del contenedor, ejecutamos los siguientes comandos:

#### Para `user_management`

```bash
cd /app
coverage run -m unittest discover tests
coverage report -m
```

#### Para `product_catalog`

Si estamos en el contenedor de `product_catalog`, ejecutamos:

```bash
cd /app
coverage run -m unittest discover tests
coverage report -m
```



### 3. Interpretación del Reporte

El comando `coverage report -m` mostrará un resumen de la cobertura de código, indicando el porcentaje de líneas cubiertas por las pruebas y señalando las líneas que no fueron ejecutadas.

## Métricas de Complejidad Ciclomática

Para evaluar la complejidad ciclomática del código, se puede utilizar la herramienta `radon`.

### 1. Instalar Radon

Podemos instalar:

```bash
pip install radon
```

### 2. Analizar la Complejidad

#### Para `user_management`

```bash
cd user_management
radon cc src -s -a
```

#### Para `product_catalog`

```bash
cd product_catalog
radon cc src -s -a
```

### 3. Interpretación del Resultado

`radon` proporcionará una calificación de A (menos compleja) a F (más compleja) para cada función o método, y un promedio general de complejidad.

