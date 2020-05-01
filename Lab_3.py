# Analisis Numerico (2020)
# Trabajo de Laboratorio N°2
# Autor: @00santiagob (GitHub)


import numpy as np
import matplotlib.pyplot as plt


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


def inewton(x, y, z):
    # Algoritmo de Interpolacion de Newton anidada
    # Utilizando Diferencia Divididas
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
    c = np.zeros((n, n))
    # Tabla de las diferencias divididas
    for i in range(n):
        # Almacenamos todos los f[x_i]=y_i en la primera columna
        c[i][0] = y[i]
    for j in range(1, n):
        for i in range(n-j):
            c[i][j] = (c[i+1][j-1] - c[i][j-1]) / (x[i+j] - x[i])
    print(np.matrix(c))
    for k in range(m):
        # p es la forma de Newton del polinomio interpolante
        p = 0
        for i in range(n):
            # s es la productoria de los puntos (x-x_0)...(x-x_i-1)
            s = 1
            if i != 0:
                for j in range(i-1):
                    s = s * (z[k] - x[j])
            p = p + (c[0][i] * s)
        w.append(p)
    return w


def ej3():
    def f(x): return 1/x
    x = []
    y = []
    z = []
    w = []
    for i in range(1, 6):
        x.append(i)
        y.append(f(i))
    for j in range(1, 102):
        z.append((24 + j)/25)
        w.append(f(z[j-1]))
    lagrange = ilagrange(x, y, z)
    newton = inewton(x, y, z)
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.plot(x, y, ".r", label="f(x)=y")
    ax.plot(z, w, "-g", label="f(z)")
    ax.plot(z, lagrange, "b", label="Lagrange")
    ax.plot(z, newton, "y", label="Newton")
    ax.set_xlabel("Eje X")
    ax.set_ylabel("Eje Y")
    ax.set_title("f(x), f(z), Lagrange y Newton")
    ax.legend()
    ax.grid()
    plt.show()


def ej4():
    def f(x): return 1/(1+25*(x**2))
    z = []
    z = np.linspace(-1, 1, 200)
    plt.style.use('dark_background')
    fig, ax = plt.subplots(3, 5)
    n = 0
    for m in range(3):
        for k in range(5):
            n = n + 1
            x = []
            y = []
            for i in range(1, n+1):
                x.append((2*(i-1)/n)-1)
                y.append(f(x[i-1]))
            lagrange = ilagrange(x, y, z)
            ax[m][k].plot(x, y, ".r", label="f(x)=y")
            ax[m][k].plot(z, lagrange, "g", label="Lagrange")
            ax[m][k].set_title("n = {}".format(n))
    plt.show()


if __name__ == "__main__":
    ej4()
