# Analisis Numerico (2020)
# Trabajo de Laboratorio N°2
# Autor: @00santiagob (GitHub)

from matplotlib import pyplot as plt
from math import sqrt, tan, exp


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
    if fun(a)*fun(b) < 0:
        i = 0
        # pm es el punto medio del intervalo
        # Hay una forma mas convergente que pm = (a + b) / 2
        pm = a + (b-a)/2
        while i < mit:
            i = i + 1
            if fun(a)*fun(pm) < 0:
                b = pm
            else:
                a = pm
            hx.append(pm)
            hf.append(fun(pm))
            """
            Se puede hacer mas robusto si se frena tambien cuando:
            abs(e: error en la variable x) < tolerancia para el error e
            """
            if abs(fun(pm)) < err:
                break
            pm = a + (b-a)/2
    else:
        print("Elegir otro intervalo")
    return hx, hf


def ej2_a():
    def fun_lab2ej2a(x): return 2*x - tan(x)  # 2*x = tan(x)
    i = [0.8, 1.4]
    err = 1e-5  # 10**(-5)
    mit = 100
    hx, hf = rbisec(fun_lab2ej2a, i, err, mit)
    print("Historial de puntos medios (hx):\n", hx)
    print("Historial de los respectivos puntos medios (hf):\n", hf)
    print("Fueron necesarias", len(hx), "iteraciones")
    return hx, hf


def ej2_b():
    def fun_lab2ej2b(x): return x**2 - 3  # sqrt(3)
    i = [1, 3]
    err = 1e-5  # 10**(-5)
    mit = 100
    hx, hf = rbisec(fun_lab2ej2b, i, err, mit)
    print("Historial de puntos medios:\n", hx)
    print("Historial de los respectivos puntos medios:\n", hf)
    print("sqrt(3) =", sqrt(3))
    return hx, hf


def ej2_c():
    hx_a, hf_a = ej2_a()
    hx_b, hf_b = ej2_b()
    plt.plot(hx_a, hf_a)
    plt.plot(hx_b, hf_b)
    plt.show()


def rnewton(fun, x0, err, mit):
    # Algoritmo de Newton
    # fun es una funcion que dado un x retorna f(x)
    # x0 es un punto inicial en los reales
    # err es la tolerancia deseada del error
    # mit es el numero maximo de iteraciones permitidas
    # Iniciamos las listas de puntos y evaluaciones
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


def ej4():
    a = int(input("Ingrese el valor de 'a' (mayor a 0): "))

    def sqrt3_a(x): return (x**3 - a, 3*(x**2))
    x0 = 1
    err = 1e-6  # 10**(-6)
    mit = 100
    hx, hf = rnewton(sqrt3_a, x0, err, mit)
    print("hx =", hx, "\nhf =", hf)
    return hx, hf


def ripf(fun, x0, err, mit):
    # Algoritmo de Iteracion de punto fijo
    # fun es una funcion que dado un x retorna f(x)
    # x0 es un punto inicial en los reales
    # err es la tolerancia deseada del error
    # mit es el numero maximo de iteraciones permitidas
    # Iniciamos la lista de puntos
    hx = []
    k = 0
    hx.append(x0)
    while k < mit:
        k = k + 1
        xn = fun(x0)
        hx.append(xn)
        if abs(xn - x0) < err:
            print("El paso es pequeño")
            break
        x0 = xn
    return hx


def ej6():
    def fun_lab2ej6(x): return 2**(x - 1)
    x0 = range(-5, 3, 1)  # Para x0 > 2 la funcion es exponencial, no converge
    err = 1e-5  # 10**(-5)
    mit = 100
    for x in x0:
        hx = ripf(fun_lab2ej6, x, err, mit)
        if len(hx) < mit:
            print("La funcion converje con x0 =", x)
            if hx[-1] < 0:
                print("Converje hacia los negativos")
            elif hx[-1] > 0:
                print("Converje hacia los positivos")
            else:
                print("Converje en cero (0)")
        else:
            print("La funcion no converje")
        print("hx =", hx)
    return hx


def ej7():
    list_x = []
    n, h = 100, 1.5
    for i in range(n+1):
        list_x.append(i*h/n)
    list_y_bisec = []
    list_y_newton = []
    list_y_ipf = []
    for x in list_x:

        def lab2ej7(y): return y - exp(-(1 - x*y)**2)

        def lab2ej7newton(y): return (lab2ej7(y),
                                      1 - 2*x*exp(-(1-x*y))*(1-x*y))
        # Biseccion
        hbisec = rbisec(lab2ej7, [0, 5], 1e-8, 100)
        list_y_bisec.append(hbisec[0][-1])  # hbisec = [hx,hf]
        # Newton
        hnewton = rnewton(lab2ej7newton, 1.2, 1e-8, 100)
        list_y_newton.append(hnewton[0][-1])  # hnewton = [hx,hf]
        # Iteracion de punto fijo
        hipf = ripf(lab2ej7, 3, 1e-8, 100)
        list_y_ipf.append(hipf[-1])  # hipf = hx
    print("list_y_bisec =", list_y_bisec)
    print("list_y_newton =", list_y_newton)
    print("list_y_ipf =", list_y_ipf)
    print(len(list_y_bisec), len(list_y_newton), len(list_y_ipf))
    plt.plot(list_x, list_y_bisec)
    plt.plot(list_x, list_y_newton)
    plt.plot(list_x, list_y_ipf)
    plt.show()


if __name__ == '__main__':
    """
    Comentando y descomentando las siguientes
    lineas puede ejecutar una funcion distinta.
    """
    ej2_a()
    # ej2_b()
    # ej2_c()
    # ej4()
    # ej6()
    # ej7()
