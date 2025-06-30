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
if __name__ == '__main__':
    p1 = Process(target=calcular_factorial,args=(10,))
    p2 = Process(target=calcular_multiplicacion,args=([2,4,6,10,5],))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
