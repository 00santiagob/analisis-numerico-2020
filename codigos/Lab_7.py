# Analisis Numerico (2020)
# Trabajo de Laboratorio N°7
# Autor: @00santiagob (GitHub)

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog


# EJERCICIO 1

# 1 kg de fertilizante alcanza para 10 m^2
# Por cada kg:
#   cantidad de fosforo   (P) >= 3
#   cantidad de nitrogeno (N) >= 1.5
#   cantidad de potasio   (K) >= 4

# _Tipo_|_P_|_N_|_K_|_$
#   T1  | 3 | 1 | 8 | 10
#   T2  | 2 | 3 | 2 | 8

# x : Kg de fertilizante T1 en 1 Kg de fertilizante Nuevo
# y : Kg de fertilizante T2 en 1 Kg de fertilizante Nuevo

# x + y = 1

# minimizar el costo total cubriendo requerimientos del suelo
# Costo total de 1 Kg de fertilizante Nuevo: 10*x + 8*y

# Requerimientos:
# 3*x + 2*y >= 3
# 1*x + 3*y >= 1.5
# 8*x + 2*y >= 4

# minimizar 10*x + 8*y
# sujeto a:
#    x*3 + y*2 >= 3
#    x + 3*y >= 1.5
#    x*8 + y*2 >= 4

# Transformar los requerimientos en funciones
# y1 = (3 - 3*x) * (1/2)
# y2 = (1.5 - x) * (1/3)
# y3 = (4 - 8*x) * (1/2)

def ej1():
    x = np.arange(0, 2.01, 0.01)
    y1 = (3 - 3*x) * (1/2)
    y2 = (1.5 - x) * (1/3)
    y3 = (4 - 8*x) * (1/2)
    y4 = np.maximum(y1, np.maximum(y2, y3))
    plt.style.use('dark_background')
    plt.plot(x, y1, label='y1 = (3 - 3*x) * (1/2)')
    plt.plot(x, y2, label='y2 = (1.5 - x) * (1/3)')
    plt.plot(x, y3, label='y3 = (4 - 8*x) * (1/2)')
    plt.plot(x, y4, 'r', label='Limite')
    # plt.fill_between(x, y1, 2.5, alpha=0.5, hatch='/')
    # plt.fill_between(x, y2, 2.5, alpha=0.5, hatch='|')
    # plt.fill_between(x, y3, 2.5, alpha=0.5, hatch='-')
    plt.fill_between(x, y4, 2.5, alpha=0.5, color='g')
    plt.ylim(0, 2.5)
    plt.xlim(0, 2)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Region Factible del Ej1')
    plt.legend()
    plt.grid()
    plt.show()


# EJERCICIO 2

# maximizar x + y
# sujeto a:
#    50*x + 24*y <= 2400
#    30*x + 33*y <= 2100
#    x >= 0
#    y >= 0

# Transformar los requerimientos en funciones
# y1 = (2400 - 50*x) * (1/24)
# y2 = (2100 - 30*x) * (1/33)


def ej2():
    # Para la curva de nivel vamos a necesitar z = x + y
    # entonces usaremos y = z - x
    x = np.arange(0, 50.5, 0.5)
    y1 = (2400 - 50*x) * (1/24)
    y2 = (2100 - 30*x) * (1/33)
    y3 = np.minimum(y1, y2)
    plt.style.use('dark_background')
    plt.plot(x, y1, label='y1 = (2400 - 50*x) * (1/24)')
    plt.plot(x, y2, label='y2 = (2100 - 30*x) * (1/33)')
    for z in range(0, 15, 5):
        y = z - x
        plt.plot(x, y, '-', label='z = {}'.format(z))
    for z in range(65, 80, 5):
        y = z - x
        plt.plot(x, y, '-', label='z = {}'.format(z))
    plt.fill_between(x, y3, -5, alpha=0.5, color='g')
    plt.ylim(-5, 100)
    plt.xlim(0, 50)
    plt.title('Region factible y curvas de nivel del ej2')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    # plt.grid()
    plt.show()


# EJERCICIO 3

# ______________|_A_|_B_|_curar
# medicamento 1 | 3 | 2 |  25
# medicamento 2 | 4 | 1 |  20

# total:         25   10

# Ejercicio 3 - a)
# x: unidad de medicina 1
# y: unidad de medicina 2
# funcion objetivo f = 25*x + 20*y
# 3*x + 4*y <=25
# 2*x + y <= 10
# x,y >= 0


def ej3_b(sol=None):
    x = np.arange(0, 5.01, 0.1)
    y1 = (25 - 3*x) / 4
    y2 = 10 - 2*x
    y3 = np.minimum(y1, y2)
    plt.style.use('dark_background')
    plt.plot(x, y1, label='y1 = (25 - 3*x) / 4')
    plt.plot(x, y2, label='y2 = 10 - 2*x')
    plt.plot(x, y3, 'r', label='Limite')
    if sol is not None:
        plt.plot(sol[0], sol[1], '.y', label='Solucion')
    plt.fill_between(x, 0, y3, alpha=0.5, color='g')
    plt.title('Region factible y curvas de nivel del ej3')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid()
    plt.show()


def ej3_c():
    # Para utilizar 'linprog' de scipy.optimize debemos:
    # expresar el problema en su forma estandar.
    # 'linprog' solo minimiza, y nosotros queremos maximizar
    # entonces al vector de c=(25,20) lo transformamos en -c
    c = np.array([-25, -20])
    A = np.array([[3, 4], [2, 1]])
    b = np.array([25, 10])
    # None es porque no tiene cota hacia el infinito
    x_bounds = (0, None)  # 0 <= x
    y_bounds = (0, None)  # 0 <= y
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x_bounds, y_bounds])
    print(res)
    return res.get('x')


# EJERCICIO 4

# variables de decicion: x1(rubia), x2(negra) y x3(baja graduacion)

# _________|_rubia_|_negra_|_baja g._|_disponibilidad
# malta    |   1   |   2   |    2    |     30
# levadura |   2   |   1   |    2    |     45
# -----------------------------------|
# $$$      |   7   |   4   |    3    |

# maximizar z = 7*x1 + 4*x2 + 3*x3
# sujeto a:
#       x1 + 2*x2 + 2*x3 <= 30
#       2*x1 + x2 + 2*x3 <= 45

#       x1, x2, x3 >= 0

def ej4():
    # 'linprog' solo minimiza, y nosotros queremos maximizar
    # entonces al vector de c=(25,20) lo transformamos en -c
    c = np.array([-7, -4, -3])
    A = np.array([[1, 2, 2], [2, 1, 2]])
    b = np.array([30, 45])
    # None es porque no tiene cota hacia el infinito
    x1_bounds = (0, None)  # 0 <= x1
    x2_bounds = (0, None)  # 0 <= x2
    x3_bounds = (0, None)  # 0 <= x3
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x1_bounds, x2_bounds, x3_bounds])
    print(res)


# EJERCICIO 5

# Minimizar el costo total = Costo1 + Costo2 + Costo3 + Costo4
# Costo total = 68.3*Horas1 + 69.5*Horas2 + 71*Horas3 + 71.2*Horas4

# Horas1 = M1 + N1 + P1 + Q1
# Horas2 = M2 + N2 + P2 + Q2
# Horas3 = M3 + N3 + P3 + Q3
# Horas4 = M4 + N4 + P4 + Q4

# Costo total = (M1+N1+P1+Q1)*68.3 + (M2+N2+P2+Q2)*69.5
#               + (M3+N3+P3+Q3)*71 + (M4+N4+P4+Q4)*71.2

# Observar que en el costo total habra que aplicar las multiplicaciones
# por lo que luego deberemos hacer 4 veces el vector c = (68.3, 69.5, 71, 71.2)

# Completar la Tarea M
# (M1/52) + (M2/57) + (M3/51) + (M4/56) >= 1
# Completar la Tarea N
# (N1/212) + (N2/218) + (N3/201) + (N4/223) >= 1
# Completar la Tarea P
# (P1/25) + (P2/23) + (P3/26) + (P4/21) >= 1
# Completar la Tarea Q
# (Q1/60) + (Q2/57) + (Q3/54) + (Q4/55) >= 1

# Horas disponibles
# M1 + N1 + P1 + Q1 <= 220
# M2 + N2 + P2 + Q2 <= 300
# M3 + N3 + P3 + Q3 <= 245
# M4 + N4 + P4 + Q4 <= 190

# Función objetivo: Costo total
# Restricciones:
#   Completar las tareas (4 restricciones)
#   Horas disponibles (4 restricciones)

# Notar que quedaron 16 incognitas
# M1 M2 M3 M4 N1 N2 N3 N4 ... Q4


def ej5():
    # np.tile repite el vector en bloques, nosotros lo queremos repedido por 4
    c = np.tile(np.array([68.3, 69.5, 71, 71.2]), 4)
    # Tareas
    tabla = np.array([52, 57, 51, 56, 212, 218, 201, 223,
                      25, 23, 26, 21, 60, 57, 54, 55])
    tabla = 1/tabla
    A1 = np.zeros((4, 16))
    # np.repeat repite cada elemento x cantidad de veces en su lugar
    I = np.repeat(np.arange(4), 4)
    J = np.arange(16)
    # Numpy no funciona con (>=), hay que transformarlo en (<=)
    # aplicamos: (-1)* de ambos lados de la desigualdad (>=)
    A1[I, J] = -tabla
    b1 = -np.ones(4)
    # Horas disponibles
    A2 = np.tile(np.eye(4), 4)
    b2 = np.array([220, 300, 245, 190])
    A_ub = np.vstack([A1, A2])
    b_ub = np.hstack([b1, b2])
    res = linprog(c, A_ub=A_ub, b_ub=b_ub)
    print(res)
    # M_1 M_2 M_3 M_4 N_1 N_2 N_3 N_4 ... Q_4
    x = np.round(res.x)
    for i in range(4):
        solucion = x[np.arange(4)*4 + i]
        print("el equipo {} debe ocupar: {}".format(i+1, solucion))


# EJERCICIO 6


if __name__ == "__main__":
    """
    Comentando y descomentando las siguientes
    lineas puede ejecutar una funcion distinta.
    """
    # ej1()
    # ej2()
    # ej3_b(ej3_c())  # Aca le estamos pasando la solucion
    # ej3_c()
    # ej4()
    # ej5()
