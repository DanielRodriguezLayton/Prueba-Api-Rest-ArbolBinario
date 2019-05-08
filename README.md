# Arbol Binario

De acuerdo a la prueba planteada se desarrolla una aplicación y una api que se encarga de entregar los datos a la aplicación webapp está procesa los datos crea el arbol y permite calcular el ancestro de dos nodos.

## Comenzando 🚀

_Estas instrucciones permiten la ejecución de la prueba._

Mira **Deployment** para conocer como desplegar el proyecto.


### Pre-requisitos 📋

_Que cosas necesitas para instalar el software y como instalarlas_

```
python 3.6 y flask framework
```

### Instalación 🔧
Download python version 3.6

_install environment virtual:

pip install virtualenv
*********** tambien, para administrar facilmente los ambientes virtuales:
pip install virtualenvwrapper(linux)
pip install virtualenvwrapper-win(windows)


crear virtualenv: mkvirtualenv FlaskApiRest -p C:\Python36\python.exe

_activate: workon FlaskApiRest


Dentro del directorio del repo clonado FlaskApiRest, instalar tools:

_pip install -r requeriments.txt


## Deployment 📦
_url con los nodos insertados:
http://127.0.0.1:5000/
_url con los nodos para consultar su Ancestro:
http://127.0.0.1:5000/nodosancestro

_Procesamiento:
_url con el arbol construido y recorido en modo InPreOrden:
http://localhost:83/arbol
_url con el ancestro calculado:
http://localhost:83/ancestro


Se carga archivo Python con la logica realizada:
_Arbol-binario.py

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [flask](http://flask.pocoo.org/) - El framework web usado
