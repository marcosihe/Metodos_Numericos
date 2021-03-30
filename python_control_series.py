import numpy as np
import math as m


def series(n):
    index = 1
    sum = 0
    while(index <= n):
        sum = sum + 1/(np.emath.power(index, 4))
        index += 1
    return sum


def run():
    print('\n*** Ejercicio: SERIE INFINITA ***')
    n_elements = int(input('Ingrese la cantidad de elementos: '))
    print(m.pi**4/90)
    print(series(n_elements))


if __name__ == '__main__':
    run()
