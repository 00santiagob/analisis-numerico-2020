# Analisis Numerico (2020)
# Trabajo de Laboratorio N°1
# Autor: @00santiagob (GitHub)

import math

def ej1():
    x = int(input("Ingresa el valor de x: "))
    y = int(input("Ingresa el valor de y: "))
    z = int(input("Ingresa el valor de z: "))

    # Diferencia entre res1 y res2
    res1 = x / y + z
    res2 = x / (y + z)
    print("Diferencia entre: x/y+z=", res1, "y x/(y+z)=", res2)

    # Diferencia entre res3 y res4
    res3 = x / y * z
    res4 = x / (y * z)
    print("Diferencia entre: x/y*z=", res3, "y x/(y*z)=", res4)

if __name__ == "__main__":
    ej1()