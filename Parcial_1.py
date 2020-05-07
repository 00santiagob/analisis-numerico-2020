# Analisis Numerico (2020)
# Parcial N°1
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
        print("El paso es muy pequeño")
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
    g = (fun(x0)**2)/(fun(x0+fun(x0))-fun(x0))
    hx.append(x0)
    hf.append(f)
    xn = x0 - g
    # Seria conveniente controlar que fun(x) != 0 en cada iteracion
    while k < mit and abs(f) >= err and abs((xn - x0)/xn) >= err:
        k = k + 1
        x0 = xn
        f = fun(x0)
        g = (fun(x0)**2)/(fun(x0+fun(x0))-fun(x0))
        hx.append(x0)
        hf.append(f)
        xn = x0 - g
    if abs((xn - x0)/xn) < err:
        print("El paso es muy pequeño")
    return hx, hf


def ej2_c():
    def f(x): return log(x)-(1/x)
    def f_f1(x): return (log(x)-(1/x), (x+1)/(x**2))
    list_x = [1.39, 1.40, 1.41, 3]  # Puntos iniciales alrededor
    list_y = []
    res_newton = []
    res_steff = []
    ite_newton = []
    ite_steff = []
    for x0 in list_x:
        # f(x)
        list_y.append(f(x0))
        # Newton
        hnx, _ = rnewton(f_f1, x0, 1e-8, 100)
        ite_newton.append(len(hnx))
        res_newton.append(hnx[-1])
        # Steffensen
        hsx, _ = rsteff(f, x0, 1e-8, 100)
        ite_steff.append(len(hsx))
        res_steff.append(hsx[-1])
    # Raices resultantes para cada x0
    print("Raices resultantes de Newton:", res_newton)
    print("Raices resultantes de Steffensen:", res_steff)
    # Cantidad de iteraciones en cada x0
    print("Cantidad de iteraciones de Newton:", ite_newton)
    print("Cantidad de iteraciones de Steffensen:", ite_steff)
    # Graficos
    plt.plot(list_x, list_y, ".", label="Puntos f(x)")
    plt.plot(list_x, res_newton, ".r", label="Puntos Newton")
    plt.plot(list_x, res_newton, label="Newton")
    plt.plot(list_x, res_steff, label="Steffensen")
    plt.plot(list_x, res_steff, ".g", label="Puntos Steffensen")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.legend()
    plt.grid()
    plt.show()


def error_cos(I, n):
    # El error de interpolar el polinomio para la funcion cos(x):
    """
    f_n = cos(x+(n+1)*pi/2)  # f n-esima de cos(x)
    productoria = 1
    for i in range(n+1):
        productoria = productoria*(x-x[i])
    err_cos = f_n/factorial(n+1).productoria
    """
    # En un intervalo [0,1]
    # Se que productoria <= 1
    # Se que f_n <= 1
    # Entonces abs(cos(x) - lagrange(x)) = 1/factorial(n+1)
    err_cos = 1/factorial(n+1)
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
    """ Ejercicio 1 """
    # fibonacci()
    """ Ejercicio 2 """
    # ej2_a()
    ej2_c()
    """ Ejercicio 3 """
    # ej3_b()
