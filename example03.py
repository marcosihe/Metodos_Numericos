import numpy as np


def run():
    # Conocer la dimensión de una matriz
    a = np.array([(1, 2, 3), (9, 8, 7)])
    print('La dimensión de la matriz "a" es: ' + str(a.ndim))


if __name__ == '__main__':
    run()
