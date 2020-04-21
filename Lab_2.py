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
        e = 
        while i < mit:
            # r es el punto medio del intervalo
            # Hay una forma mas convergente que r = (a + b) / 2
            r = a + (b-a)/2
            if fun(a)*fun(r) < 0:
                b = r
            elif fun(a)*fun(r) > 0:
                a = r
            else:
                # Entra si fun(r)=0
                if abs(fun(r)) < err:
                    hx.append(r)
                    hf.append(fun(r))
                    break
            hx.append(r)
            hf.append(fun(r))
    return hx, hf


def ej1():
    return rbisec()


if __name__ == '__main__':
    # ejx() ejecutara la funcion del ejercicio n° x
    ej1()
