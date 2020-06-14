# Analisis Numerico (2020)
# Trabajo de Laboratorio N°5
# Autor: @00santiagob (GitHub)

import numpy as np
import matplotlib.pyplot as plt
from math import cos, sin, pi, sqrt, ceil
from scipy.integrate import quad as integral, trapz, simps


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
        suma = 0
        n = int((N/2) + 1)
        for i in range(1, n):
            suma = suma + fun(x[2*i])
        S = 2 * h * suma
    elif regla == "simpson":
        sx0 = fun(x[0]) + fun(x[N])
        sx1, sx2 = 0, 0
        n = int((N/2) + 1)
        for i in range(1, n):
            if i % 2 == 0:
                sx1 = sx1 + fun(x[2*i - 1])
            else:
                sx2 = sx2 + fun(x[2*i])
        S = (sx0 + 4*sx1 + 2*sx2) * h/3
    else:
        print("Regla invalida")
        S = None
    return S


def ej2():
    def f(x): return np.exp(-x)
    subint = [4, 10, 20]  # Subintervalos
    a, b = 0, 1
    res_integral, _ = integral(f, a, b)  # Integral de f(x)
    res_trapecio = []
    err_trapecio = []
    res_pm = []
    err_pm = []
    res_simpson = []
    err_simpson = []
    i = 0
    for s in subint:
        # Resultados de usar las reglas compuestas
        res_trapecio.append(intenumcomp(f, a, b, s, "trapecio"))
        res_pm.append(intenumcomp(f, a, b, s, "pm"))
        res_simpson.append(intenumcomp(f, a, b, s, "simpson"))
        # Error que se comete al usar las reglas compuesta
        err_trapecio.append(abs(res_integral - res_trapecio[i]))
        err_pm.append(abs(res_integral - res_pm[i]))
        err_simpson.append(abs(res_integral - res_simpson[i]))
        i = i + 1
    print("Integral de f(x):", res_integral)
    print("Trapecio:", res_trapecio)
    print("Punto Medio:", res_pm)
    print("Simpson:", res_simpson)
    print("Errores absolutos del Trapecio:", err_trapecio)
    print("Errores absolutos del Punto Medio:", err_pm)
    print("Errores absolutos del Simpson:", err_simpson)


def ej3():
    # x pertenece a los Reales^n
    def senint(xi):
        Ni = ceil(xi / 0.1) + 1
        return intenumcomp(cos, 0, xi, Ni, "trapecio")
    pi2 = 2 * pi
    x = np.arange(0, pi2+0.5, 0.5)  # Espaciados 0.5 desde 0 hasta pi2+0.5
    y_sin = []
    y_senint = []
    for i in x:
        y_sin.append(sin(i))
        y_senint.append(senint(i))
    print("x =", x)
    print("sin(x) =", y_sin)
    print("senint(x) =", y_senint)
    # Graficos
    plt.style.use('dark_background')
    plt.plot(x, y_sin, 'y', label="Seno")
    plt.plot(x, y_senint, '.r', label="Senint")
    plt.legend()
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()


def ej4_a(a, b):
    def f2(x): return (-2+x) * np.exp(-x)

    def f4(x): return (-4+x) * np.exp(-x)
    return max(f2(a), f2(b)), max(f4(a), f4(b))


def ej4_b(a, b):
    def f2(x): return 2*cos(x) - x*sin(x)

    def f4(x): return -4*cos(x) - x*sin(x)
    return max(f2(a), f2(b)), max(f4(a), f4(b))


def ej4_c(a, b):
    def f2(x): return (3+6*(x**2)) * (1+(x**2))**(-1/2)

    def f4(x): return 9 * (1 + (x**2))**(-5/2)
    return max(f2(a), f2(b)), max(f4(a), f4(b))


def ej4_d(a, b):
    def f2(x):
        t1 = (12 * (x**6)) / ((1 + (x**4))**(5/2))
        t2 = (6 * (x**2)) / ((1 + (x**4))**(3/2))
        return 2*(t1 - t2)

    def f4(x):
        t1 = (612 * (x**4)) / ((1 + (x**4))**(5/2))
        t2 = 12 / ((1 + (x**4))**(3/2))
        t3 = (1680 * (x**12)) / ((1 + (x**4))**(9/2))
        t4 = (2160 * (x**3)) / ((1 + (x**4))**(7/2))
        return 2*(t1 - t2 + t3 - t4)
    return max(f2(a), f2(b)), max(f4(a), f4(b))


def ej4():
    # a < µ < b
    # Queremos que f2(µ) y f4(µ) maximicen el error
    """ Error del Trapecio
    Et(f) = - f2(µ) * ((b-a)**3) / (12*n**2)
    ==> Et(f) = - f2(µ) / (12*n**2)
    """
    """ Error de Simpson
    Es(f) = - f4(µ) * ((b-a)**5) / (180*n**4)
    ==> Es(f) = - f4(µ) / (180*n**4)
    """
    a, b = 0, 1
    error = 1e-5
    fa = ej4_a(a, b)
    fb = ej4_b(a, b)
    fc = ej4_c(a, b)
    fd = ej4_d(a, b)
    f_d = np.array([fa, fb, fc, fd])
    ej = ['a', 'b', 'c', 'd']
    for i in range(4):
        print("Ejercicio {})".format(ej[i]))
        puntos = 0  # n > 0 va a ser la cantidad de puntos
        n2, n4 = 0, 0
        err_f2, err_f4 = 1, 1  # ya es mayor a 1e-5
        while err_f2 >= error or err_f4 >= error:
            puntos = puntos + 1
            if err_f2 >= error:
                n2 = puntos
                err_f2 = abs(- f_d[i][0] * ((b-a)**3) / (12 * n2**2))
            if err_f4 >= error:
                n4 = puntos
                err_f4 = abs(- f_d[i][1] * ((b-a)**5) / (180 * n4**4))
        print("Se necesita n={} para el Error del Trapecio".format(n2))
        print("Se necesita n={} para el Error de Simpson".format(n4))


def ej5():
    def fa(x): return np.exp(-x**2)

    def fb(x): return (x**2 * np.log(x + sqrt(x**2 + 1)))
    xa = np.arange(-10000, 10000)  # Si usamos [-inf, inf] exedemos el limite
    xb = np.arange(0, 2)
    ya, yb = [], []
    for ia in xa:
        ya.append(fa(ia))
    for ib in xb:
        yb.append(fb(ib))
    print("a) con Trapecio =", trapz(ya, xa))
    print("a) con Simpson =", simps(ya, xa))
    # Como no se pudo usar trapz y simps con intervalo infinito, usare quad
    print("a) con scipy.integrate.quad =", integral(fa, -np.inf, np.inf)[0])
    print("b) con Trapecio =", trapz(yb, xb))
    print("b) con Simpson =", simps(yb, xb))
    # En este caso no hacia falta, pero es para que se note la diferencia
    print("b) con scipy.integrate.quad =", integral(fb, 0, 2)[0])


def pendulo(l, alfa):
    # Dado una longitud en metros y una amplitud alfa
    # devuelve el periodo de un pendulo
    alfa_rad = (alfa / 180) * pi  # Transforma el alfa en radianes

    def f(x): return (1 - sin(alfa_rad/2)**2 * sin(x)**2)**(-1/2)
    i, _ = integral(f, 0, pi/2)
    g = 9.8  # 9.8 m/s²
    T = 4 * sqrt(np.divide(l, g)) * i
    return T


def ej6():
    # Cuando alfa=0 el periodo=4*sqrt(l/g)*(pi/2)
    longitud = float(input("Introduce la longitud del pendulo en metros: "))
    for alfa in range(91):  # 0 <= alfa <= 90
        periodo = pendulo(longitud, alfa)
        print("El pendulo de longitud {} ".format(longitud) +
              "con amplitud {} ".format(alfa) +
              "tiene un periodo de {}".format(periodo))


if __name__ == "__main__":
    """
    Comentando y descomentando las siguientes
    lineas puede ejecutar una funcion distinta.
    """
    ej2()
    # ej3()
    # ej4()
    # ej5()
    # ej6()
