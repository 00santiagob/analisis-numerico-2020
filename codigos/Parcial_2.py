# Analisis Numerico (2020)
# Parcial de Laboratorio N°2
# Autor: 00santiagob

import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import CubicSpline
from scipy.optimize import linprog


# EJERCICIO 1


def spline_velocidad(ts, vs):
    n = len(ts)
    new_ts = []
    k = -1  # Index de ts
    for i in range(2*n - 1):
        if i % 2 == 0:
            k += 1
            new_ts.append(ts[k])  # Son los viejos puntos de ts
        else:
            new_ts.append((ts[k] + ts[k+1])/2)  # Son los puntos medios de ts
    # CubicSpline genera el polinomio interpolante por spline cubico
    # Necesitaremos extrapolar, podemos usar extrapolate (si no se rompe)
    polinomio = CubicSpline(ts, vs, extrapolate=True)
    # Evaluamos el polinomio en la nueva particion generada.
    new_vs = polinomio(new_ts)
    return new_ts, new_vs


def trapecio_adaptativo(v, p):
    # v: valores de la funcion R->R a ser integrada
    # p: particion del intervalo
    # N es la cantidad de subintervalos a usar
    N = len(p)
    trap = 0  # Calcula el trapecio en un intervalo
    for i in range(N - 1):
        h = (p[i+1] - p[i])
        trap = trap + ((v[i] + v[i+1]) * h / 2)
    return trap


def posicion_particula():
    # Datos originales
    ts = np.array([0, 0.22, 0.85, 1, 1.5, 1.6, 1.99])
    vs = np.array([0, 0.1, -0.15, -0.03, 0.75, -0.3, 0.01])
    # Se calculan los nuevos datos
    new_ts, new_vs = spline_velocidad(ts, vs)
    # Se hace la aproximacion de la integral por trapecio
    Itrap = []
    for pos in range(len(new_ts)):
        Itrap.append(trapecio_adaptativo(new_vs[:pos+1], new_ts[:pos+1]))
    # Grafico
    plt.style.use('dark_background')
    plt.plot(new_ts, Itrap, label='Tiempo-Posicion')
    plt.title('Posicion de la particula')
    plt.xlabel('Tiempo en seg.')
    plt.ylabel('Posicion de la particula')
    plt.legend()
    plt.grid()
    plt.show()


# EJERCICIO 2


def soltrinf(A, b, x):
    # Resolucion de sistema con matriz triangular inferior
    # A matriz R^(nxn)
    # b matriz (vector) R^n
    # Retorna x matriz (vector) tal que Ax=b
    if np.linalg.det(A) == 0:
        print("El determinante es 0 => la matriz A es singular")
    n = A.shape[0]
    for i in range(n):
        suma = 0
        if i != 0:
            for j in range(i):
                suma = suma + (A[i][j]*x[j])
        x[i] = (b[i] - suma) / A[i][i]
    return x


def gseidel(A, b, err, mit):
    # Metodo iterativo de Gauss-Seidel adaptado con solucion triangular inf
    # A es una matriz R^nxn
    # b es un vector R^n
    # err es la tolerancia de error
    # mit es la cantidad maxima de iteraciones
    n = A.shape[0]
    LD = np.zeros((n, n))  # Matriz triangular inferior
    # Extraigo la matriz triangular inferior
    for i in range(n):
        for j in range(i+1):
            LD[i][j] = A[i][j]
    b_aux = np.zeros(n)  # Nos ayuda a no modificar la b original
    # x y u seran las soluciones aproximadas
    x = np.zeros(n)
    u = np.zeros(n)
    # k es la cantidad de iteraciones realizadas
    for k in range(mit):
        # Sumamos la triangular superior y se la restamos a b
        for i in range(n):
            soltrsup = 0
            for j in range(i+1, n):
                soltrsup = soltrsup + (A[i][j] * x[j])
            b_aux[i] = b[i] - soltrsup
        # Calculamos solucion triangular inferior
        u = soltrinf(LD, b_aux, u)
        if np.max(abs(np.add(u, (-1)*x))) < err:
            return u, k
        for i in range(n):
            x[i] = u[i]
    return x, k


def sor(A, b, omega, err, mit):
    # Metodo iterativo de Successive Over-Relaxation
    # A es una matriz R^nxn
    # b es un vector R^n
    # omega > 1 es el factor de relajacion
    # err es la tolerancia de error
    # mit es la cantidad maxima de iteraciones
    n = A.shape[0]
    LD = np.zeros((n, n))  # Matriz triangular inferior
    # Extraigo la matriz triangular inferior
    for i in range(n):
        for j in range(i+1):
            # Necesitamos que solo L este multiplicada por omega
            if j < i:
                LD[i][j] = A[i][j] * omega
            else:
                LD[i][j] = A[i][j]
    b_aux = np.zeros(n)  # Nos ayuda a no modificar la b original
    # x y u seran las soluciones aproximadas
    x = np.zeros(n)
    u = np.zeros(n)
    # k es la cantidad de iteraciones realizadas
    for k in range(mit):
        # Sumamos la triangular superior y se la restamos a b
        for i in range(n):
            soltrsup = 0
            for j in range(i+1, n):
                soltrsup = soltrsup + (omega * A[i][j])
            soltrsup = (soltrsup + ((omega - 1) * LD[i][i])) * x[j]
            b_aux[i] = (omega * b[i]) - soltrsup
        # Calculamos solucion triangular inferior
        u = soltrinf(LD, b_aux, u)
        if np.max(abs(np.add(u, (-1)*x))) < err:
            return u, k
        for i in range(n):
            x[i] = u[i]
    return x, k


def ejemplo2():
    # A modo de prueba para los algoritmos anteriores
    mit = 100
    A1 = np.array([[3, 1, 1], [2, 6, 1], [1, 1, 4]])
    b1 = np.array([5, 9, 6])
    err1 = 1e-11
    x1_gs, k1_gs = gseidel(A1, b1, err1, mit)
    print("Caso (1): se requirieron {} iteraciones ".format(k1_gs) +
          "utilizando Gauss-Seidel")
    print("x =", x1_gs)
    omega = 1.01
    x1_s, k1_s = sor(A1, b1, omega, err1, mit)
    print("Caso (1): se requirieron {} iteraciones ".format(k1_s) +
          "utilizando Successive over-relaxation con omega={}".format(omega))
    print("x =", x1_s)
    omega = 2
    x1_s, k1_s = sor(A1, b1, omega, err1, mit)
    print("Caso (1): se requirieron {} iteraciones ".format(k1_s) +
          "utilizando Successive over-relaxation con omega={}".format(omega))
    print("x =", x1_s)
    omega = 5
    x1_s, k1_s = sor(A1, b1, omega, err1, mit)
    print("Caso (1): se requirieron {} iteraciones ".format(k1_s) +
          "utilizando Successive over-relaxation con omega={}".format(omega))
    print("x =", x1_s)
    A2 = np.array([[5, 7, 6, 5], [7, 10, 8, 7], [6, 8, 10, 9], [5, 7, 9, 10]])
    b2 = np.array([23, 32, 33, 31])
    err2 = 1e-4
    x2_gs, k2_gs = gseidel(A2, b2, err2, mit)
    print("Caso (2): se requirieron {} iteraciones ".format(k2_gs) +
          "utilizando Gauss-Seidel")
    print("x =", x2_gs)
    omega = 1.01
    x2_s, k2_s = sor(A1, b1, omega, err2, mit)
    print("Caso (1): se requirieron {} iteraciones ".format(k2_s) +
          "utilizando Successive over-relaxation con omega={}".format(omega))
    print("x =", x2_s)
    omega = 2
    x2_s, k2_s = sor(A1, b1, omega, err2, mit)
    print("Caso (1): se requirieron {} iteraciones ".format(k2_s) +
          "utilizando Successive over-relaxation con omega={}".format(omega))
    print("x =", x2_s)
    omega = 2.7
    x2_s, k2_s = sor(A1, b1, omega, err2, mit)
    print("Caso (1): se requirieron {} iteraciones ".format(k2_s) +
          "utilizando Successive over-relaxation con omega={}".format(omega))
    print("x =", x2_s)
    # Se observo que es conveniente que omega este en el intervalo [1;3)


# EJERCICIO 3

# __________________________|_mesas_|_silla_|_disponibilidad
# tiempo de produccion (hs) |   2   |   1   |     40
# planchas de madera        |   1   |   2   |     50
# --------------------------|-------|-------|
# $$$                       |  500  |  300  |

# x: Cantidad de mesas producidas en una semana
# y: Cantidad de sillas producidas en una semana

# maximizar 500*x + 300*y
# sujeto a:
#           2*x + y <= 40
#           x + 2*y <= 50
#           x, y >= 0

# Transformamos los requerimientos en funciones
# y1 = 40 - 2*x
# y2 = (50 - x) * (1/2)


def ej3a():
    # Para utilizar 'linprog' de scipy.optimize debemos:
    # expresar el problema en su forma estandar.
    # 'linprog' solo minimiza, y nosotros queremos maximizar
    # entonces al vector c=(500,300) lo transformamos en -c
    c = np.array([-500, -300])
    A = np.array([[2, 1], [1, 2]])
    b = np.array([40, 50])
    # None es porque no tiene cota hacia el infinito
    x_bounds = (0, None)  # 0 <= x
    y_bounds = (0, None)  # 0 <= y
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])
    x = np.round(res.x)
    print('Para maximizar el ingreso neto se debe fabricar:')
    print('Mesas =', x[0])
    print('Sillas =', x[1])
    print('Ingreso Maximo =', 500*x[0] + 300*x[1])
    return x


def ej3b(sol=None):
    x = np.arange(0, 22.5, 0.5)
    y1 = 40 - 2*x
    y2 = (50 - x) * (1/2)
    y3 = np.minimum(y1, y2)
    # Grafico
    plt.style.use('dark_background')
    # Rectas en el plano
    plt.plot(x, y1, label='y1 = 40 - 2*x')
    plt.plot(x, y2, label='y2 = (50 - x) * (1/2)')
    plt.plot(x, y3, 'r', label='Limite')
    # Regiones pintadas en el plano
    plt.fill_between(x, 0, y1, alpha=0.5, hatch='-')
    plt.fill_between(x, 0, y2, alpha=0.5, hatch='|')
    plt.fill_between(x, 0, y3, alpha=0.5, color='g', label='Region Factible')
    # Solucion encontrada
    if sol is not None:
        plt.plot(sol[0], sol[1], '.', label='Solucion')
    # Limitaciones para el grafico
    plt.ylim(0, 42)
    plt.xlim(0, 22)
    plt.xlabel('Eje X - Mesas')
    plt.ylabel('Eje Y - Sillas')
    plt.title('Region Factible')
    plt.legend()
    # plt.grid()
    plt.show()

# Al contratar al carpintero se genera un gasto de dinero $200xHORA
# Asumiendo que el ayudante no trabaja por si solo, siempre ayuda al carpintero
# y su tiempo de produccion es igual al del carpintero, entonces cada vez que
# ayuda al carpintero este reduce el tiempo de produccion a la mitad.

# x1: Cantidad de mesas producidas en una semana solo por el carpintero
# x2: Cantidad de sillas producidas en una semana solo por el carpintero
# x3: Cantidad de mesas producidas en una semana con el ayudante
# x4: Cantidad de sillas producidas en una semana con el ayudante

# __________________________|__x1_|__x2_|__x3_|__x4_|_disponibilidad
# tiempo de produccion (hs) |  2  |  1  |  1  | 0.5 |     40
# planchas de madera        |  1  |  2  |  1  |  2  |     50
# --------------------------|-----|-----|-----|-----|
# $$$                       | 500 | 300 | 300 | 200 |

# maximizar 500*x1 + 300*x2 + 300*x3 + 100*x4
# sujeto a:
#           2*x1 + x2 + x3 + (0.5)*x4 <= 40
#           x1 + 2*x2 + x3 + 2*x4 <= 50
#           x1, x2, x3, x4 >= 0


def ej3c():
    # Como en el ejercicio 3-a) debemos transformar el vector c a -c
    c = np.array([-500, -300, -300, -100])
    A1 = np.array([2, 1, 1, 0.5])
    A2 = np.array([1, 2, 1, 2])
    A = np.vstack([A1, A2])
    b = np.array([40, 50])
    res = linprog(c, A_ub=A, b_ub=b)
    x = np.round(res.x)
    print('Para maximizar el ingreso neto se debe fabricar:')
    print('Mesas hechas por el carpintero =', x[0])
    print('Sillas hechas por el carpintero =', x[1])
    print('Mesas hechas con ayuda =', x[2])
    print('Sillas hechas con ayuda =', x[3])
    print('Ingreso Maximo =', 500*x[0] + 300*x[1] + 300*x[2] + 100*x[3])
    hs = x[2] + (x[3] * 0.5)
    print('Si, le conviene contratar al ayudante por {} horas'.format(hs))


if __name__ == "__main__":
    """
    Comentando y descomentando las siguientes
    lineas puede ejecutar una funcion distinta
    dependiendo de el ejercicio que elija.
    """
    ###############
    # EJERCICIO 1 #
    ###############

    # posicion_particula()

    ###############
    # EJERCICIO 2 #
    ###############

    ejemplo2()

    ###############
    # EJERCICIO 3 #
    ###############

    # ej3b(ej3a())
    # ej3c()
