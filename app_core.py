from multiprocessing import Process
import numpy

def calcular_factorial(n):
    f = n
    for i in reversed(range(1,f)):
        f = f*i
    return f
def calcular_multiplicacion(l):
    m = 1
    for i in l:
        m = m*i
    return m
