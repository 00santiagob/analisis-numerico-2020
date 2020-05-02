# Analisis Numerico (2020)
# Parcial N°1
# Autor: @00santiagob (GitHub)

import numpy as np
from matplotlib import pyplot as plt
from math import log, cos, factorial, pi


def fibonacci():
    # Inicializo la lista donde se almacenara la sucesion de fibonacci
    fb = []
    # Ingresamos hasta que numero queremos que resuelva fibonacci
    n = input("Ingresar el valor de n: ")
    if type(n) != int:
        print("El valor de 'n' debe ser un entero positivo")
    elif n < 0:
        print("El valor de 'n' no puede ser menor que 0")
    else:
        for i in range(n+1):
            if i <= 1:
                fb.append(i)
            else:
                fb.append(fb[i-2] + fb[i-1])
    print(fb)
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
    x0 = 1.4
    err = 1e-6  # 10**(-6)
    mit = 100
    def f(x): return (log(x)-(1/x), (x+1)/(x**2))
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
    list_x = [1.39, 1.40, 1.41, 3]
    list_y_newton = []
    list_y_steff = []
    for x0 in list_x:
        def f_newton(x): return (log(x)-(1/x), (x+1)/(x**2))
        def f_steff(x): return log(x)-(1/x)
        # Newton
        hnewton = rnewton(f_newton, x0, 1e-8, 100)
        list_y_newton.append(hnewton[0][-1])  # hnewton = [hx,hf]
        # Steffensen
        hsteff = rsteff(f_steff, x0, 1e-8, 100)
        list_y_steff.append(hsteff[0][-1])  # hsteff = [hx,hf]
    print("list_y_newton =", list_y_newton)
    print("list_y_steff =", list_y_steff)
    print("Cantidad de iteraciones de Newton:", len(list_y_newton))
    print("Cantidad de iteraciones de Steffensen:", len(list_y_steff))
    plt.plot(list_x, list_y_newton, label="Newton")
    plt.plot(list_x, list_y_newton, ".r", label="Puntos Newton")
    plt.plot(list_x, list_y_steff, label="Steffensen")
    plt.plot(list_x, list_y_steff, ".g", label="Puntos Steffensen")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    plt.legend()
    plt.grid()
    plt.show()


def ilagrange(x, y, z):
    # Algoritmo de Interpolacion de Lagrange
    # x,y son los pares a interpolar
    # x,y pertenecen a los reales^n
    # p(x_i)=y_i con i=1...n
    # z pertenece a los reales^m
    # z son valores para evaluar p
    # w pertenece a los reales^m
    # w sera la salida tal que w_j = p(z_j) con j=1...m
    # Inicializo la salida w
    w = []
    if len(x) != len(y):
        print("x,y no tienen el mismo largo")
        return w
    n = len(x)
    m = len(z)
    for k in range(m):
        # p es la forma de Lagrange del polinomio interpolante
        p = 0
        for i in range(n):
            # L es el polinomios asociados a los puntos distintos x_1...x_n
            L = 1
            for j in range(n):
                if i != j:
                    L = L*((z[k] - x[j]) / (x[i] - x[j]))
            p = p + y[i]*L
        w.append(p)
    return w


def error_cos(I, n):
    x = np.linspace(I[0], I[1], n)
    y = []
    for punto in x:
        y.append(cos(punto))
    lagrange = ilagrange(x, y, x)  # No se que valor darle a z
    err_cos = 1/factorial(n+1)  # No me doy cuenta de que otra forma hacerlo
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
    return err_cos


def ej3_b():
    i = [0, 1]
    error = 1e-6
    puntos = 1
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
    # ej2_c()
    """ Ejercicio 3 """
    # ej3_b()
