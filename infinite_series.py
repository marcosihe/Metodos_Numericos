import numpy as np
import math as m


def series(n):
    index = 1
    sum = 0
    while index <= n:
        sum = np.single(sum + 1/(index ** 4))
        index += 1
    return sum


def series_reverse_process(n):
    index = n
    sum = 0
    while index >= 1:
        sum = np.single(sum + 1/(index ** 4))
        index -= 1
    return sum


def relative_error(true_value, approx_value):
    return (np.absolute(true_value - approx_value)/approx_value)*100


def run():
    print('\n*** Ejercicio: SERIE INFINITA ***')
    n_elements = int(input('Ingrese la cantidad de elementos: '))
    true_value = np.single(m.pi**4/90)

    print('\n *** Valor verdadero ***')
    print(true_value)

    print('\n*** Realizando la suma desde 1 hasta ' + str(n_elements) + ' ***')
    print(series(n_elements))
    print('El error relativo en esta forma es de: ' +
          str(relative_error(true_value, series(n_elements))) + '%')

    print('\n*** Realizando la suma desde ' + str(n_elements) + ' hasta 1 ***')
    print(series_reverse_process(n_elements))
    print('El error relativo en esta forma es de: ' +
          str(relative_error(true_value, series_reverse_process(n_elements))) + '%')


if __name__ == '__main__':
    run()
