# Analisis Numerico (2020)
# Parcial N°1
# Autor: @00santiagob (GitHub)

from matplotlib import pyplot as plt
from math import sqrt, exp


def fibonacci():
    # Inicializo la lista donde se almacenara la sucesion de fibonacci
    fb = []
    n = input("Ingresar el valor de n: ")
    if type(n) != int:
        print("El valor de 'n' debe ser un entero positivo")
    elif n < 0:
        print("El valor de 'n' no puede ser menor que 0")
    else:
        for i in range(2, n+1):
            if i <= 1:
                fb.append(i)
            else:
                fb.append(fb[i-2] + fb[i-1])
    print(fb)
    return fb


if __name__ == "__main__":
    fibonacci()
