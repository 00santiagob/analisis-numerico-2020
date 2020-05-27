# Analisis Numerico (2020)
# Trabajo de Laboratorio N°6
# Autor: @00santiagob (GitHub)

import numpy as np
from scipy import linalg


def soltrsup(A, b):
    # Resolucion de sistema con matriz triangular superior
    # A matriz R^(nxn)
    # b matriz (vector) R^n
    # Retorna x matriz (vector) tal que Ax=b
    if np.linalg.det(A) == 0:
        print("El determinante es 0 => la matriz A es singular")
    n = A.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        suma = 0
        if i != n:
            for j in range(i+1, n):
                suma = suma + (A[i][j]*x[j])
        x[i] = (b[i] - suma) / A[i][i]
    return x


def soltrinf(A, b):
    # Resolucion de sistema con matriz triangular inferior
    # A matriz R^(nxn)
    # b matriz (vector) R^n
    # Retorna x matriz (vector) tal que Ax=b
    if np.linalg.det(A) == 0:
        print("El determinante es 0 => la matriz A es singular")
    n = A.shape[0]
    x = np.zeros(n)
    for i in range(n):
        suma = 0
        if i != 0:
            for j in range(i):
                suma = suma + (A[i][j]*x[j])
        x[i] = (b[i] - suma) / A[i][i]
    return x


def egauss(A, b):
    # Eliminacion Gaussiana sin estrategia de pivoteo
    # A matriz R^(nxn)
    # b matriz (vector) R^n
    # Retorna A (matriz triangular superior) y b (transformada)
    n = A.shape[0]
    if n != len(b):
        print("La cantidad de filas de A deben ser igual a las cantidad de b")
        print(A, b)
        return None
    U = np.array([a[:] for a in A])
    y = np.array([e for e in b])
    for k in range(n-1):
        for i in range(k+1, n):
            if U[k][k] == 0:
                print("No esta contemplado el intercambio entre filas")
                print("No puede haber elemento pivote igual a 0")
                return None
            m = U[i][k] / U[k][k]
            U[i][k] = 0
            for j in range(k+1, n):
                U[i][j] = U[i][j] - m*U[k][j]
            y[i] = y[i] - m*y[k]
    return U, y


def soleg(A, b):
    # Resuelve el sistema lineal A*x = b
    U, y = egauss(A, b)
    x = soltrsup(U, y)
    return x


def lu(A):
    # Factorizacion LU
    n = A.shape[0]
    U = np.zeros((n, n))
    L = np.eye(n)
    for k in range(n):
        for j in range(k, n):
            suma = 0
            for m in range(k):
                suma = suma + L[k][m]*U[m][j]
            U[k][j] = A[k][j] - suma
        if k != n:
            for i in range(k+1, n):
                suma = 0
                for m in range(k):
                    suma = suma + L[i][m]*U[m][k]
                L[i][k] = (1/U[k][k]) * (A[i][k] - suma)
    return L, U


def sollu(A, b):
    # La forma mas rapida seria
    # lu, piv = linalg.lu_factor(A)
    # x = linalg.lu_solve((lu, piv), b)
    # Pero la que se pide es:
    # L, U = lu(A) sin pivoteo ==> p = np.eyes(A.shape[0]) matriz identidad
    p, l, u = linalg.lu(A)  # con pivoteo
    y = soltrinf(l, p @ b)
    x = soltrsup(u, y)
    return x


def ej4():
    A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]], int)
    nI = (-1) * np.eye(3, dtype=int)
    b1 = np.hstack((np.ones(3, int), np.zeros(3, int)))
    b2 = np.ones(6, int)
    A = np.vstack((np.hstack((A, nI)), np.hstack((nI, A))))
    # A=np.array([[6,-2,2,4],[12,-8,6,10],[3,-13,9,3],[-6,4,1,-18]])
    # b1 = np.array([12, 34, 27, -38])
    x1_eg = soleg(A, b1)
    x2_eg = soleg(A, b2)
    x1_lu = sollu(A, b1)
    x2_lu = sollu(A, b2)
    print("soleg(A, b1) =", x1_eg)
    print("soleg(A, b2) =", x2_eg)
    print("sollu(A, b1) =", x1_lu)
    print("sollu(A, b2) =", x2_lu)


def jacobi(A, b, err, mit):
    # A es una matriz R^nxn
    # b es un vector R^n
    # err es la tolerancia de error
    # mit es la cantidad maxima de iteraciones
    # x es la solucion aproximada
    # k es la cantidad de iteraciones realizadas
    x, k = 0, 0
    return x, k


def gseidel(A, b, err, mit):
    # A es una matriz R^nxn
    # b es un vector R^n
    # err es la tolerancia de error
    # mit es la cantidad maxima de iteraciones
    # x es la solucion aproximada
    # k es la cantidad de iteraciones realizadas
    x, k = 0, 0
    return x, k


def ej6():
    mit = 100
    A1 = np.array([[3, 1, 1], [2, 6, 1], [1, 1, 4]])
    b1 = np.array([5, 9, 6])
    err1 = 1e-11
    x1_j, k1_j = jacobi(A1, b1, err1, mit)
    x1_gs, k1_gs = gseidel(A1, b1, err1, mit)
    print("Caso (1): se requirieron {} iteraciones utilizando Jacobi")
    print("Caso (1): se requirieron {} iteraciones utilizando Gauss-Seidel")
    A2 = np.array([[5, 7, 6, 5], [7, 10, 8, 7], [6, 8, 10, 9], [5, 7, 9, 10]])
    b2 = np.array([23, 32, 33, 31])
    err2 = 1e-4
    x2_j, k2_j = jacobi(A2, b2, err2, mit)
    x2_gs, k2_gs = gseidel(A2, b2, err2, mit)
    print("Caso (2): se requirieron {} iteraciones utilizando Jacobi")
    print("Caso (2): se requirieron {} iteraciones utilizando Gauss-Seidel")


if __name__ == "__main__":
    ej4()
