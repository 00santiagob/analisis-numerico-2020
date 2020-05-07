# Analisis Numerico (2020)
# Trabajo de Laboratorio N°2
# Autor: @00santiagob (GitHub)


import numpy as np
import matplotlib.pyplot as plt


def ej1_a():
    # Aproximacion discreta por cuadrados minimos
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
    xi = np.linspace(0, 6, 100)
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
    xi = np.random()
    yi = []
    for i in xi:
        yi.append(f(i))
    coef = np.polyfit(xi, yi, 1)
    x = np.linspace(0, 10, 20)
    y = []
    for i in xi:
        y.append(np.polyval(coef, i))
    # Grafico
    plt.style.use('dark_background')
    plt.plot(xi, y, 'r', label="Polinomio generado")
    plt.plot(xi, yi, '.y', label="Valores generados")
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")
    plt.title("Aproximacion por cuadrados minimos (polyval y polyfit)")
    plt.legend
    plt.grid()
    plt.show()


if __name__ == "__main__":
    ej1_b()
