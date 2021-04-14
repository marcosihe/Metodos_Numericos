# This program is useful to calculate the relative and absolute errors
import numpy as np


def absolute_error(true_value, approx_value):
    return np.absolute(true_value - approx_value)


def relative_error(true_value, approx_value):
    return (np.absolute(true_value - approx_value)/np.absolute(approx_value))


def run():
    true_value = float(input('Ingrese el valor exacto o valor verdadero: '))
    approx_value = float(input('\nIngrese el valor medido o aproximado: '))

    print('\nEl error absoluto es: ' +
          str(absolute_error(true_value, approx_value)))
    print('\nEl error relativo es: ' +
          str(relative_error(true_value, approx_value)*100) + ' %')


if __name__ == '__main__':
    run()
