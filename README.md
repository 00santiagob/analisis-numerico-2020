# analisis-numerico-2020

## Ejercicios de Laboratorio

### Autor

* __@00santiagob__

## Resumen

Ejercicios del Laboratorio de Analisis Numerico (2020) del FaMAF - UNC (FaMAFyC)

* **Lab_0.py** no se hizo porque es solo una guia introductoria a Python.
* **Lab_1.py** (*completo* - Temario 1).
* **Lab_2.py** (*completo* - Temario 2).
* **Lab_3.py** (*completo* - Temario 3).
* **Lab_4.py** (*completo* - Temario 4).
* **Lab_5.py** (*en proceso* - Temario 5).
* **Lab_6.py** (*en proceso* - Temario 6).
* **Parcial_1.py** (*completo* - Temarios 1, 2 y 3).
* **Parcial_2.py** (*en proceso* - Temarios 4, 5 y 6).

Ademas se uso *autopep8* para el estilo de codigo.

En los codigos se han usado librerias como ***Numpy***, ***Scipy***, ***Matplotlib*** y ***Math*** para la realizacion de algunos ejercicios.

### Temario

   1. Preliminares matematicas: errores, punto flotante, redondeo
   2. Re-Solucion de ecuaciones no lineales
   3. Interpolacion polinomial
   4. Aproximacion (Ajuste de datos)
   5. Integracion numerica
   6. Re-Soluciones de ecuaciones lineales
   7. Programacion lineal

## Requisitos

Tener instalado *__Git__* y  *__Python__* (en lo posible Python3 cualquier version).
Ademas se recomienda tener instaladas las librerias anteriormente instaladas (Si no sabe hacerlo, mas abajo se lo explicamos).

## Instrucciones

Primero descargar el repositorio __analisis-numerico-2020__:

1) Abrir una terminal:

        git clone https://github.com/00santiagob/analisis-numerico-2020.git

2) Para correr algun ejercicio entrar en algun archivo **Lab_x.py**, donde _x_ es el numero correspondiente a cada practico.

3) En la parte inferior cambiar la llamada a la funcion **ejx()** por el que deseen, donde _x_ es el numero de ejercicio.

### Como Instalar

Hara falta tener instalado Git en su dispositivo, pero no es parte de este repositorio enseñarles a hacerlo, asi que queda en sus manos hacerlo.

#### Python en Windows

Descargar [Python 3.x.x](https://www.python.org/downloads/) de la pagina oficial.

#### Python Ubuntu

Abrir la terminal y correr el siguiente comando:

        sudo apt install python3 python3-dev python3-pip
        pip3 install --upgrade pip
        sudo apt update && sudo apt upgrade

#### Evitar errores

Chequear que esten instaladas las librerias *Numpy* y *Matplotlib*, en caso de no estarlo correr lo siguiente en la terminal (powershell en caso de usar Windows):

        pip3 install numpy
        pip3 install matplotlib

> **Nota:** en caso de ya tenerlos instalados es suficientes (no importa la version).
>
> **Errores:**
Posiblemente en linux aparezcan errores al instalar la libreria *Matplotlib*, dado que depende de otras librerias: *libfreetype6*, *libpng12* y *libqhull*. Tambien puede que aparezcan con otros nombres similares, pero son las mismas librerias.
>
> **Soluciones:**
>
> * Error al instalar Matplotlib:
>
>       sudo apt install libfreetype6-dev
>       sudo apt install pkg-config
>       sudo apt install libpng12-dev
>       sudo apt install pkg-config
>       sudo apt install libqhull
>       sudo apt update && sudo apt upgrade
>       pip3 install matplotlib
>
> **Cualquier otro error se agradece que lo comenten abriendo una issu nueva.**
>
> **Gracias y disfruten**
