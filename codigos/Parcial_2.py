# Analisis Numerico (2020)
# Parcial de Laboratorio N°2
# Alumno: Santiago Balog

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline

# EJERCICIO 1


def spline_velocidad(ts, vs):
    n = len(ts)
    h = (np.round(ts[-1]) - ts[0]) / (2*n - 1)  # distancia equitativa
    puntos = []
    k = -1
    for i in range(2*n - 1):
        print(i, k)
        if i % 2 == 0:
            k += 1
            puntos.append(ts[k])
        else:
            puntos.append((ts[k] + ts[k+1])/2)
    print('puntos =', puntos)
    # intervalos = np.arange(0, 2, 0.01)
    # CubicSpline genera el polinomio interpolante por spline cubico
    # Necesitaremos extrapolar, podemos usar extrapolate (si no se rompe)
    polinomio = CubicSpline(ts, vs, extrapolate=True)
    # Evaluamos el polinomio en los puntos generados.
    final = polinomio(puntos)
    print('final =', final)
    plt.style.use('dark_background')
    plt.plot(puntos, final, label='SplineCubico')
    plt.plot(ts, vms, '.', label='Datos')
    plt.title('Velocidad de una particula')
    plt.xlabel('Tiempo en seg.')
    plt.ylabel('Velocidad en m/seg')
    plt.legend()
    plt.show()
    return puntos, final


def trapecio_adaptativo(fun, a, b, N):
    # fun es la funcion R->R a ser integrada
    # a,b pertenecen a R, son los extremos de integracion
    # N es la cantidad de subintervalos a usar
    # S va a ser la salida
    S = 0
    h = (b - a)/N
    x = [a]
    for i in range(1, N):
        x.append(a + i*h)
    x.append(b)
    suma = (fun(x[0]) + fun(x[N]))/2
    for i in range(1, N):
        suma = suma + fun(x[i])
    S = suma * h
    return S


def posicion_particula():
    pass


if __name__ == "__main__":
    """
    Comentando y descomentando las siguientes
    lineas puede ejecutar una funcion distinta.
    """
    # ts = np.array([0, 0.22, 0.85, 1, 1.5, 1.6, 1.99])  # Tiempo en segundos (s)
    # vms = np.array([0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01])  # Velocidad m/s
    # spline_velocidad(ts, vms)
    
