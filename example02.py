import numpy as np


def run():
    print('*** Matriz 3x4 de unos ***')
    # En los parámetros se le indica las filas y las columnas, respectivamente
    ones_array = np.ones((3, 4))
    print(ones_array)

    print('\n*** Matriz 4x2 de ceros  ***')
    zeros_array = np.zeros((4, 2))
    print(zeros_array)

    print('\n*** Matriz 2x6 de números aleatorios ***')
    random_array = np.random.random((2, 3))
    print(random_array)

    print('\n*** Matriz vacía de 3x3 ***')
    empty_array = np.empty((3, 3))
    print(empty_array)

    # Matriz con un valor determinado en todas las posiciones
    print('\n*** Matriz 3x2 con un valor determinado en todas las posiciones ***')
    full_array = np.full((3, 2), 7)
    print(full_array)

    # Matriz con valores espaciados uniformemente
    print('\n*** Matriz con saltos de 5 desde 0 hasta 30 ***')
    arange_array = np.arange(0, 31, 5)
    # El primer parámetro indica desde donde
    # El segundo parámetro indica hasta donde (excluye a ese valor)
    # El tercer parámetro indica el espaciad o los saltos
    print(arange_array)

    print('\n*** Matriz con número entre 0 y 2 con saltos de 0.5 ***')
    arange_array_2 = np.arange(0, 2, 0.5)
    print(arange_array_2)

    print('\n*** Matriz identidad 4x4 ***')
    identity_array = np.eye(4, 4)
    print(identity_array)

    # Al ser una matriz cuadrada, la matriz identidad, se le puede pasar el parámetro de la siguiente forma
    print('\n*** Matriz identidad 4x4 ***')
    identity_array_2 = np.eye(4)
    print(identity_array_2)


if __name__ == '__main__':
    run()
