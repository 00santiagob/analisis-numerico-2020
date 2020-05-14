# Analisis Numerico (2020)
# Trabajo de Laboratorio N°5
# Autor: @00santiagob (GitHub)


import numpy as np
import matplotlib.pyplot as plt


def intenumcomp(fun, a, b, N, regla):
    # fun es la funcion R->R a ser integrada
    # a,b pertenecen a R, son los extremos de integracion
    # N es la cantidad de subintervalos a usar
    # String regla = "trapecio", "pm" o "simpson"
    # S va a ser la salida
    S = 0
    h = (b - a)/N
    x = [a]
    for i in range(1, N):
        x.append(a + i*h)
    x.append(b)
    if regla == "trapecio":
        suma = (fun(x[0]) + fun(x[N]))/2
        for i in range(1, N):
            suma = suma + fun(x[i])
        S = suma * h
    elif regla == "pm":
        pass
    elif regla == "simpson":
        sx0 = fun(x[0]) + fun(x[N])
        sx1, sx2 = 0, 0
        n = N/2
        for i in range(1, n):
            if i % 2 == 0:
                sx1 = sx1 + fun(x[2*i - 1])
            else:
                sx2 = sx2 + fun(x[2*i])
        S = (sx0 + 4*sx1 + 2*sx2) * h/3
    else:
        print("Regla invalida")
    return S


def ej2():
    def f(x): return np.exp(-x)
    subint = [4, 10, 20]
    a = 0
    b = 1
    res_trapecio = []
    res_pm = []
    res_simpson = []
    for s in subint:
        res_trapecio.append(intenumcomp(f, a, b, s, "trapecio"))
        res_pm.append(intenumcomp(f, a, b, s, "pm"))
        res_simpson.append(intenumcomp(f, a, b, s, "simpson"))
    print("Trapecio:", res_trapecio)
    print("Punto Medio:", res_pm)
    print("Simpson:", res_simpson)


if __name__ == "__main__":
    ej2()
