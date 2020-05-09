# Analisis Numerico (2020)
# Trabajo de Laboratorio N°2
# Autor: @00santiagob (GitHub)


import numpy as np
import matplotlib.pyplot as plt
from math import asin, cos, pi


def ej1_a():
    # Aproximacion discreta por cuadrados minimos
    # Cargamos los datos
    datos = np.loadtxt('./datos/datos1a.dat')
    m = datos.shape[1]  # Cantidad de datos
    xd = datos[0]
    yd = datos[1]
    # Coeficientes del Polinomio Lineal
    a = m * sum(xd*yd) - sum(xd)*sum(yd)
    a = a / (m*sum(xd**2) - sum(xd)**2)
    b = sum(xd**2)*sum(yd) - sum(xd)*sum(xd*yd)
    b = b / (m*sum(xd**2) - sum(xd)**2)
    # Polinomio Lineal (grado 1)

    def polinomio_lineal(x): return a*x + b
    # Nuevos valores a evaluar en el polinomio
    xi = np.linspace(0, 5, 100)
    yi = []
    for i in xi:
        yi.append(polinomio_lineal(i))
    # Grafico
    plt.style.use('dark_background')
    plt.plot(xd, yd, '.y', label="datos1a.dat")
    plt.plot(xi, yi, 'r', label="Polinomio Lineal")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Aproximacion por cuadrados minimos")
    plt.legend
    plt.grid()
    plt.show()


def ej1_b():
    def f(x): return (3/4)*x - (1/2)
    xi = np.linspace(0, 10, 20)  # 20 puntos en [0, 10]
    # y es el arreglo con los f(x)
    yi = []
    for i in xi:
        yi.append(f(i))
    # y_norm son los puntos en el eje y con dispersion normal
    y_norm = yi + np.random.normal(size=20)
    # Coeficientes del ajuste lineal para los y_norm
    coef = np.polyfit(xi, y_norm, 1)
    # y es el arreglo de los xi valuados con los coef
    y = []
    for i in xi:
        y.append(np.polyval(coef, i))
    # Grafico
    plt.style.use('dark_background')
    plt.plot(xi, y, 'g', label="Recta (polyval con")
    plt.plot(xi, yi, '.r', label="Valores f(x)")
    plt.plot(xi, y_norm, '.y', label="Polinomio generado")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Aproximacion por cuadrados minimos (polyval y polyfit)")
    plt.legend()
    plt.grid()
    plt.show()


def ej2_a():
    def f(x): return asin(x)
    x = np.linspace(0, 1, 50)
    y = []
    for i in x:
        y.append(f(i))
    residuos = []
    for n in range(6):
        coef, residuo, _, _, _ = np.polyfit(x, y, n, full=True)
        residuos.append(residuo)
    print("Residuos", *residuos, sep='\n')
    sumR = 0
    for i in residuos:
        sumR = sumR + sum(i)
    print("Suma Residual:", sumR)


def ej2_b():
    def f(x): return cos(x)
    x = np.linspace(0, 4*pi, 50)
    y = []
    for i in x:
        y.append(f(i))
    residuos = []
    for n in range(6):
        coef, residuo, _, _, _ = np.polyfit(x, y, n, full=True)
        residuos.append(residuo)
    print("Residuos", *residuos, sep='\n')
    sumR = 0
    for i in residuos:
        sumR = sumR + sum(i)
    print("Suma Residual:", sumR)


def ej3_a():
    data = np.loadtxt('datos/datos3a.dat')
    # y = C * x**A --> ln(y) = ln(C) + A*ln(x)
    # y_hat = c_hat + A**x_hat, donde y_hat=ln(y), c_hat=ln(C), x_hat=ln(x)
    x = data[0]
    y = data[1]
    x_hat = np.log(x)
    y_hat = np.log(y)
    coef = np.polyfit(x_hat, y_hat, 1)
    A = coef[0]
    C = np.exp(coef[1])  # c_hat = coef[1]
    print("C =", C)
    print("A =", A)
    y_new = []
    for i in x:
        y_new.append(C*(i**A))
    plt.style.use('dark_background')
    plt.plot(x, y_new, 'r', label='funcion')
    plt.plot(x, y, '.y', label='datos')
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Ajuste de los datos3a.dat")
    plt.legend()
    plt.grid()
    plt.show()


def ej3_b():
    data = np.loadtxt('datos/datos3b.dat')
    # y = x / (A*x + B) --> (1/y) = A + (1/x)*B
    # y_hat = A + x_hat*B, donde y_hat = 1/y, x_hat = 1/x
    x = data[0]
    y = data[1]
    x_hat = 1/x
    y_hat = 1/y
    coef = np.polyfit(x_hat, y_hat, 1)
    B = coef[0]
    A = coef[1]
    print("B =", B)
    print("A =", A)
    y_new = []
    for i in x:
        y_new.append(i / (A*i + B))
    plt.style.use('dark_background')
    plt.plot(x, y_new, 'g', label='funcion')
    plt.plot(x, y_new, '.r', label='funcion')
    plt.plot(x, y, '.y', label='datos')
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Ajuste de los datos3b.dat")
    plt.legend()
    plt.grid()
    plt.show()


def ej4():
    # y = a*(e**(b*x)) --> ln(y) = ln(a) + b*x
    # y_hat = a_hat + b*x, donde y_hat = ln(y), a_hat = ln(a)
    datos = np.genfromtxt('datos/covid_italia.csv', delimiter=',')
    filas = datos.shape[0]
    x, y = [], []
    for fila in range(filas):
        xAux, yAux = datos[fila]
        x.append(xAux)
        y.append(yAux)
    y_hat = np.log(y)
    coef = np.polyfit(x, y_hat, 1)
    b = coef[0]
    a = np.exp(coef[1])
    print("a =", a)
    print("b =", b)
    y_new = []
    for i in x:
        y_new.append(a*np.exp(b*i))
    # Graficos
    plt.style.use('dark_background')
    plt.plot(x, y_new, 'r', label='Funcion')
    plt.plot(x, y, '.y', label='Datos')
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Covid-19 Italia")
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    ej4()