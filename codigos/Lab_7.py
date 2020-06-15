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
    x = np.arange(0, 1.01, 0.01)
    y1 = (3 - 3*x) * (1/2)
    y2 = (1.5 - x) * (1/3)
    y3 = (4 - 8*x) * (1/2)
    y4 = np.maximum(y1, np.maximum(y2, y3))
    plt.style.use('dark_background')
    plt.plot(x, y1, label='y1 = (3 - 3*x) * (1/2)')
    plt.plot(x, y2, label='y2 = (1.5 - x) * (1/3)')
    plt.plot(x, y3, label='y3 = (4 - 8*x) * (1/2)')
    # plt.fill_between(x, y1, 2.5, alpha=0.5, hatch='/')
    # plt.fill_between(x, y2, 2.5, alpha=0.5, hatch='|')
    # plt.fill_between(x, y3, 2.5, alpha=0.5, hatch='-')
    plt.fill_between(x, y4, 2.5, alpha=0.5)
    plt.ylim(0, 2.5)
    plt.xlim(0, 1)
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid()
    plt.show()


"""
# EJERCICIO 3

# ______________|_A_|_B_|_curar
# medicamento 1 | 3 | 2 |  25
# medicamento 2 | 4 | 1 |  20

# total:         25   10

def ej3_a():
    # x: unidad de medicina 1
    # y: unidad de medicina 2
    # funcion objetivo f = 25 * x + 20 * y
    # 3 * x + 4 * y <=25
    # 2 * x + y <= 10
    # x,y >= 0
    pass


def ej3_b():
    x = np.arange(0, 10, 0.1)
    y1 = (25 - 3*x)/4  # y = (25 - 3*x)/4
    y2 = 10 - 2 * x  # y = 10 - 2* x
    y3 = np.minimum(y1, y2)
    plt.ylim(0, 10)
    plt.plot(x, y1, x, y2, x, y3)
    plt.fill_between(x, 0, y3)
    plt.show()


def ej3_c():
    c = np.array([-25, -20])
    A = np.array([[3, 4], [2, 1]])
    b = np.array([25, 10])
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds])
    print(res)


# EJERCICIO 5

# Costo total = Costo_1 + Costo_2 + Costo_3 + Costo_4

# Costo total = Horas_1 * 68.3 + Horas_2 * 69.5 + Horas_3 * 71 + Horas_4 * 71.2

# Completar la Tarea M
# M_1 / 52 + M_2 / 57 + M_3 / 51 + M_4 / 56 >= 1

# Completar la Tarea N
# N_1 / 212 + N_2 / 218 + N_3 / 201 + N_4 / 223 >= 1

# Horas_1 = M_1 + N_1 + P_1 + Q_1

# Costo total = (M_1 + N_1 + P_1 + Q_1) * 68.3 + Horas_2 * 69.5 + Horas_3 * 71
                + Horas_4 * 71.2

# Horas disponibles
# M_1 + N_1 + P_1 + Q_1 <= 220

##############

# Función objetivo: Costo total
# Restricciones:
#   Completar las tareas (4 restricciones)
#   Horas disponibles (4 restricciones)

# M_1 M_2 M_3 M_4 N_1 N_2 N_3 N_4 ... Q_4

c = np.tile(np.array([68.3, 69.5, 71, 71.2]), 4)

# Tareas

tabla = np.array([52, 57, 51, 56, 212, 218, 201, 223,
                    25, 23, 26, 21, 60, 57, 54, 55])
tabla = 1/tabla

A1 = np.zeros((4, 16))
I = np.repeat(np.arange(4), 4)
J = np.arange(16)
A1[I, J] = -tabla

b1 = -np.ones(4)

# Horas disponibles

A2 = np.tile(np.eye(4), 4)
b2 = np.array([220, 300, 245, 190])

A_ub = np.vstack([A1, A2])
b_ub = np.hstack([b1, b2])

res = linprog(c, A_ub=A_ub, b_ub=b_ub)

# M_1 M_2 M_3 M_4 N_1 N_2 N_3 N_4 ... Q_4

x = np.round(res.x)

for i in range(4):
    print("el equipo {} debe ocupar: {}".format(i+1,x[np.arange(4)*4+i]))

# print(res)
"""

if __name__ == "__main__":
    """
    Comentando y descomentando las siguientes
    lineas puede ejecutar una funcion distinta.
    """
    ej1()
