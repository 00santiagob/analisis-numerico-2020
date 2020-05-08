# Analisis Numerico (2020)
# Trabajo de Laboratorio N°2
# Autor: @00santiagob (GitHub)


import numpy as np
import matplotlib.pyplot as plt


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
    pass


def ej2_b():
    pass


if __name__ == "__main__":
    ej2_a()
