# Escaneo de Puertos con Nmap

## Requisitos
- Python 
- virtualenv

> Instalar virtualenv

```
pip install virtualenv
```
------------

> Lo primero que tenenemos que hacer es descargar o clonal el repositorio, para poder ejecutar el script y finalmente abrir el proyecto con nuestro editor, se recomienda que a la hora de abrir el editor, lo habra como administrador.

> Ya en el editor tenemos que descargar las librerias para poder usar el script, podemos escoger la OPCION 1 o OPCION 2.

-------------------

## Opcion 1
Crear un entorno Virtualizado, para instalar las librerias

#### Paso 1
Creamos el entorno de Virtualizacion
```python
python -m virtualenv venv
```

#### Paso 2
Activamos el entorno de Virtualizacion
```python
.\venv\Scripts\activate
```

#### Paso 3
Instalamos las librerias
```python
pip install -r ".\requirements.tx
```
----
## Opcion 2
Instalar toda las librerias de forma local

#### Paso 1
Instalamos las librerias de forma local
```
pip install -r ".\requirements.tx
```

## Forma de Uso

> Donde dice "tu_ip", vas a poner al ip, que deseeas hacer el scaner, ejecutas el script y tendras como salida, port, Name, State y Version:

```
scaner.scan('tu_ip','1-1024', '-v -sS -sV -sC -A -O')
```
