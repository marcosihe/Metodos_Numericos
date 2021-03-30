import numpy as np


# Función y1
def function_y1(number):
    return (np.emath.power((20 + np.emath.power(number, 2)), (1/3)) - np.emath.log10(number))


def run():
    num = float(input("Ingrese el valor donde quiera evaluar la función y1: "))
    result = function_y1(num)
    print('y(' + str(num) + ') = ' + str(result))


if __name__ == '__main__':
    run()
