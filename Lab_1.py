# Analisis Numerico (2020)
# Trabajo de Laboratorio N°1
# Autor: @00santiagob (GitHub)

import numpy as np
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

def ej2():
    # epsilon-maquina: 2**(-52) = 2.2204e-16 aprox
    epsilon_maquina = 2**(-52)
    print("epsilon-maquina: 2**(-52)=", epsilon_maquina)

    a = 1 + 2**(-53)
    b = a - 1
    print("a=", a, "b=", b)
    
    a = 1 + 2**(-52)
    b = a - 1
    print("a=", a, "b=", b)

def ej3():
    """
    Overflow: cuando se trata de representar un numero grande que tiende a infinito y la maquina no lo soporta.

    Underflow: cuando se trata de representar un numero muy chico que tiende a 0 y la maquina no lo soporta.
    
    Para este ejercicio se usa isinf de la libreria numpy.
    """
    i = 0
    try:
        #while not np.isinf(2**i):
        while not math.isinf(2**i):
            i = i + 1
    except OverflowError:
        print("Overflow con 2**("+str(i)+")=", 2**i+1)
    
    i = 0
    while 1/(2**i) != 0:
        i = i + 1
    print("UnderFlow con 1/(2**"+str(i)+")")

def ej4():
    # Incrementando x en 0.1
    x = 0
    while x != 10 and x < 15:
        x = x + 0.1
        print("x =", x)
    # Incrementando x en 0.5
    x = 0
    while x != 10 and x < 15:
        x = x + 0.5
        print("x =", x)

def ej5():
    """
    fact = 1
    for i in range(7):
        if i == 0:
            fact = fact * 1
        else:
            fact = fact * i
    print("Factorial de 6 =", fact)
    """
    # Usando math.factorial()
    n = int(input("Ingrese un valor n: "))
    fact = math.factorial(n)
    print("Factorial de n =", fact)

def ej6():
    x = int(input("Ingrese el valor x: "))
    y = int(input("Ingrese el valor y: "))
    if x == y:
        print("Ambos 'x' e 'y' son iguales")
    else:
        print("El mas grande es: ", max(x,y))

def ej7():
    x = int(input("Ingrese el valor x: "))
    n = int(input("Ingrese el valor n: "))
    for i in range(n+1):
        if i < 5:
            print(str(x)+"^("+str(i)+") = ", int(pow(x,i)))
        elif i == n:
            print(str(x)+"^("+str(n)+") = ", int(pow(x,n)))
        else:
            continue

def mala(a, b, c):
    if a != 0:
        delta = b**2 - 4*a*c
        x1 = (-b + delta**(.5)) / (2*a)
        x2 = (-b - delta**(.5)) / (2*a)
    else:
        x1 = math.nan
        x2 = math.nan
    return x1, x2

def buena(a, b, c):
    delta = b**2 - 4*a*c
    if b <= 0:
        x1 = (-b + delta**(.5)) / (2*a)
    else:
        x1 = (-b - delta**(.5)) / (2*a)
    x2 = c / (a*x1)
    return x1, x2

def ej8():
    a = int(input("Ingrese el valor a: "))
    b = int(input("Ingrese el valor b: "))
    c = int(input("Ingrese el valor c: "))
    x1, x2 = mala(a, b, c)
    print("Baskhara:\nx1=", x1, "\nx2=", x2)
    x1, x2 = buena(a, b, c)
    print("Evita cancelacion de digitos significativos:\nx1=", x1, "\nx2=", x2)

def horn(coefs, x):
    # Algoritmo de Horn (Multiplicacion encajada)
    n = len(coefs)
    res = coefs[0]
    for i in range(1,n):
        res = res * x + coefs[i]
    return res

def ej9():
    print("Ingresar los coeficientes separados por espacios:")
    str_arr = input().split(' ')
    coefs = [int(num) for num in str_arr]
    x = int(input("Ingresa el valor x: "))
    p = horn(coefs, x)
    print("Horn devuelve: ", p)

if __name__ == "__main__":
    # ejx() ejecutara la funcion del ejercicio n° x
    ej9()