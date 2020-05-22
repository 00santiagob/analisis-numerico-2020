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


def ej4():
    # a = 0  y  b = 1
    """ Error del Trapecio
    Et(f) = - f²(µ) * ((b-a)³) / (12*n²)
    ==> Et(f) = - f²(µ) / (12*n²)
    """
    """ Error de Simpson
    Es(f) = - f⁴(µ) * ((b-a)⁵) / (180*n⁴)
    ==> Es(f) = - f⁴(µ) / (180*n⁴)
    """
    # a < µ < b
    # Queremos que f²(µ) y f⁴(µ) maximicen el error
    """ a)
    f²(µ) = (-2+x) * e**(-x)
    ==> f²(a) = -2, f²(b) = -0.37
    f⁴(µ) = (-4+x) * e**(-x)
    ==> f⁴(a) = -4, f⁴(b) = -1.10
    """
    """ b)
    f²(µ) = 2*cos(x) - x*sen(x)
    ==> f²(a) = 2, f²(b) = 1.98
    f⁴(µ) = -4*cos(x) - x*sen(x)
    ==> f⁴(a) = -4, f⁴(b) = -4.02
    """
    """ c)
    f²(µ) = (3 + 6*(x**2)) * (1 + (x**2))**(-1/2)
    ==> f²(a) = 3, f²(b) = 6.36
    f⁴(µ) = 9 * (1 + (x**2))**(-5/2)
    ==> f⁴(a) = 9, f⁴(b) = 1.59
    """
    """ d)
    f²(µ) = NO LO HICE
    f⁴(µ) = NO LO HICE
    """
    error = 1e-5


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
    print("a) con Trapecio", trapz(ya, xa))
    print("a) con Simpson", simps(ya, xa))
    print("b) con Trapecio", trapz(yb, xb))
    print("b) con Simpson", simps(yb, xb))


def ej6(x):
    pass


if __name__ == "__main__":
    ej3()
