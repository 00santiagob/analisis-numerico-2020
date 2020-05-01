# Analisis Numerico (2020)
# Parcial N°1
# Autor: @00santiagob (GitHub)

from matplotlib import pyplot as plt
from math import log


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
    # plt.plot(list_x, list_y_newton)
    plt.plot(list_x, list_y_steff)
    plt.show()


if __name__ == "__main__":
    """ Ejercicio 1 """
    # fibonacci()
    """ Ejercicio 2 """
    # ej2_a()
    ej2_c()
    """ Ejercicio 3 """
