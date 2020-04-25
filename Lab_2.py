# Analisis Numerico (2020)
# Trabajo de Laboratorio N°2
# Autor: @00santiagob (GitHub)

import numpy as np
import math


def rbisec(fun, I, err, mit):
    # Algoritmo de Biseccion
    # fun es una funcion que dado un x retorna f(x)
    # I = [a,b] es un intervalo en los reales
    # err es la tolerancia deseada del error
    # mit es el numero maximo de iteraciones permitidas

    a = I[0]
    b = I[1]

    # Iniciamos las listas de puntos y evaluaciones
    hx = []
    hf = []
    
    # Si el signo de a y b son distintos podemos comenzar
    # En vez de fun(a)*fun(b)<0 para calcular el signo usaremos sign()
    if sign(fun(a)) != sign(fun(b)):
        i = 0
        # pm es el punto medio del intervalo
        # Hay una forma mas convergente que pm = (a + b) / 2
        pm = a + (b-a)/2
        while i < mit and abs(fun(pm)) > err:
        	i = i + 1
            if fun(a)*fun(pm) < 0:
                b = pm
            elif fun(a)*fun(pm) > 0:
                a = pm
            else:
                # Entra si fun(pm)=0
                if abs(fun(pm)) < err:
                    hx.append(pm)
                    hf.append(fun(pm))
                    break
            hx.append(pm)
            hf.append(fun(pm))
            pm = a + (b-a)/2
    else:
    	print("Elegir otro intervalo")
    return hx, hf


def ej2_a():
	a, b = map(int(),
		input("Donde empiza y termina el intervalo: ").split(" "))
	I = [a,b]
	err = int(input("Tolerancia deseada del error: "))
	mit = int(input("Numero maximo de iteraciones: "))
    hx, hf = rbisec(fun,I,err,mit)
    print("Historial de puntos medios:", hx,
    	"\sHistorial de los respectivos puntos medios:", hf)


if __name__ == '__main__':
    # ejx() ejecutara la funcion del ejercicio n° x
    ej1()
