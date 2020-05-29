# Analisis Numerico (2020)
# Parcial de Laboratorio N°1
# Autor: @00santiagob (GitHub)

import numpy as np
from matplotlib import pyplot as plt
from math import log, cos, factorial, pi


def fibonacci():
    # Metodo de Fibonacci (Iterativo)
    # Inicializo la lista donde se almacenara la sucesion de fibonacci
    fb = []
    # Ingresamos hasta que numero queremos que resuelva fibonacci
    n = int(input("Ingresar el valor de n: "))
    if type(n) != int:
        print("El valor de 'n' debe ser un entero positivo")
    elif n < 0:
        print("El valor de 'n' no puede ser menor que 0")
    elif n == 0 or n == 1:  # Casos base
        fb.append(n)  # fibonacci(0) = 0 y fibonacci(1) = 1
    else:
        fb.append(1)  # fibonacci(1) = 1
        fb.append(1)  # fibonacci(2) = 1
        if n > 2:
            for i in range(2, n):
                fb.append(fb[i-2] + fb[i-1])
    print("Los primeros {} elementos:\n".format(n), fb)
    return fb


def rnewton(fun, x0, err, mit):
    # Algoritmo de Newton
    # fun es una funcion que dado un x retorna f(x)
    # x0 es un punto inicial en los reales
    # err es la tolerancia deseada del error
    # mit es el numero maximo de iteraciones permitidas
    # Inicializo las listas de puntos y evaluaciones
    hx = []
    hf = []
    k = 0
    v, dv = fun(x0)
    hx.append(x0)
    hf.append(v)
    xn = x0 - v/dv
    # Seria conveniente controlar que fun(x) != 0 en cada iteracion
    while k < mit and abs(v) >= err and abs((xn - x0)/xn) >= err:
        k = k + 1
        x0 = xn
        v, dv = fun(x0)
        hx.append(x0)
        hf.append(v)
        xn = x0 - v/dv
    if dv == 0:
        print("La derivada es nula en tal punto")
    if abs((xn - x0)/xn) < err:
        print("El paso es muy pequeno")
    return hx, hf


def ej2_a():
    x0 = 1.4  # Punto inicial
    err = 1e-6  # 10**(-6)
    mit = 100  # Maximo de iteraciones

    def f(x): return (log(x)-(1/x), (x+1)/(x**2))  # f(x) y su derivada f'(x)
    hx, hf = rnewton(f, x0, err, mit)
    print("hx =", hx, "\nhf =", hf)
    return hx, hf


def rsteff(fun, x0, err, mit):
    # Algoritmo de Steffensen
    # fun es una funcion que dado un x retorna f(x)
    # x0 es un punto inicial en los reales
    # err es la tolerancia deseada del error
    # mit es el numero maximo de iteraciones permitidas
    # Inicializo las listas de puntos y evaluaciones
    hx = []
    hf = []
    k = 0
    f = fun(x0)
    g = (f**2)/(fun(x0+f)-f)
    hx.append(x0)
    hf.append(f)
    xn = x0 - g
    # Seria conveniente controlar que fun(x) != 0 en cada iteracion
    while k < mit and abs(f) >= err and abs((xn - x0)/xn) >= err:
        k = k + 1
        x0 = xn
        f = fun(x0)
        g = (f**2)/(fun(x0+f)-f)
        hx.append(x0)
        hf.append(f)
        xn = x0 - g
    if abs((xn - x0)/xn) < err:
        print("El paso es muy pequeno")
    return hx, hf


def ej2_c():
    def f(x): return log(x)-(1/x)

    def f_f1(x): return (log(x)-(1/x), (x+1)/(x**2))
    list_x = [1.39, 1.40, 1.41, 3]  # Puntos iniciales alrededor
    res_newton = []
    res_steff = []
    ite_newton = []
    ite_steff = []
    for x0 in list_x:
        # Newton
        hnx, _ = rnewton(f_f1, x0, 1e-8, 100)
        ite_newton.append(len(hnx))
        res_newton.append(hnx)
        # Steffensen
        hsx, _ = rsteff(f, x0, 1e-8, 100)
        ite_steff.append(len(hsx))
        res_steff.append(hsx)
    # Raices resultantes para cada x0
    print("Resultados de Newton para cada x0:", *res_newton, sep='\n')
    print("Resultados de Steffensen para cada x0:", *res_steff, sep='\n')
    # Cantidad de pasos para cada x0
    print("Cantidad de pasos de Newton para cada x0:", ite_newton)
    print("Cantidad de pasos de Steffensen para cada x0:", ite_steff)


def error_cos(I, n):
    # El error de interpolar el polinomio para la funcion cos(x):
    """
    f_n = cos(x+(n+1)*pi/2)  # f n-esima de cos(x)
    productoria = 1
    for i in range(n+1):
        productoria = productoria*(x-x[i])
    err_cos = f_n/factorial(n+1).productoria
    """
    # En un intervalo [0,1], va a pasar lo siguiente
    # productoria <= 1
    # f_n <= 1
    # Entonces abs(cos(x) - lagrange(x)) = 1/factorial(n+1)
    # Pero nosotros lo queremos ver para un intervalo [a,b] con a,b culquieras
    err_cos = abs(I[1]-I[0])**n/factorial(n+1)
    return err_cos


def ej3_b():
    i = [0, 1]
    error = 1e-6
    puntos = 1  # n es la cantidad de puntos
    err_cos = 1
    while err_cos >= error:
        puntos = puntos + 1
        err_cos = error_cos(i, puntos)
    print("Se necesitan {} puntos".format(puntos))


if __name__ == "__main__":
    """
    Comentando y descomentando las siguientes
    lineas puede ejecutar una funcion distinta.
    """
    fibonacci()
    # ej2_a()
    # ej2_c()
    # ej3_b()
