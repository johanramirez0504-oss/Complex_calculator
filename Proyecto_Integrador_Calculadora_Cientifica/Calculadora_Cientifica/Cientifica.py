import math as m
import random as rnd
def valor_absoluto(a):
    return m.fabs(a)
def radicacion(a, b,c):
    if c==None:
        c=1
    if a< 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    
    else:
        return a**(c/b)
def radianes(grados):
    return f"{grados} grados son {grados * (m.pi / 180)} radianes"

def grados(radianes):
    return radianes * (180 / m.pi)
def seno(x):
    return m.sin(x)
def coseno(x):
    return m.cos(x)
def tangente(x):
    return m.tan(x)
def secante(x):
    return 1/m.cos(x)
def cosecante(x):
    return 1/m.sin(x)
def cotangente(x):
    return 1/m.tan(x)
def logaritmo(x, base):
    if base== None:
        return m.log10(x)
    else:
        return m.log(x, base)
def factorial(n):
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    else:
        return m.factorial(n)
def teorema_pitagoras(a, b):
    return m.sqrt(a**2 + b**2)
def teorema_pitagoras_cateto(c, a):
    if c < a:
        return "Error: La hipotenusa debe ser mayor que el cateto."
    else:
        return m.sqrt(c**2 - a**2)
def numero_aleatorio(min_v,max_v):
    return rnd.randint(min_v,max_v)