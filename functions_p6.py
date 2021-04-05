import numpy as np
from error_calculator import *


def traditional_function(x):
    return 1.01*np.exp(4*x) - 4.62*np.exp(3*x) - 3.11*np.exp(2*x) + 12.2*np.exp(x) - 1.99


def horner_function(x):
    return -1.99 + (12.2 + (-3.11 + (-4.62 + 1.01*x)*x)*x)*x


def run():
    print('Funcion original evaluada en x =')
    print(traditional_function(1.53))
    # Calculos de los errores en el punto 6
    # Apartado a
    print('\n*** Arpartado a ***')
    print('\nError absoluto = ' +
          str(absolute_error(traditional_function(1.53), -7.90)))
    print('\nError relativo = ' +
          str(relative_error(traditional_function(1.53), -7.90)) + ' %')

    # Apartado b
    print('\n*** Apartado b ***')
    print('\nError absoluto = ' +
          str(absolute_error(traditional_function(1.53), -7.99)))
    print('\nError relativo = ' +
          str(relative_error(traditional_function(1.53), -7.99)) + ' %')

    # Apartado c) i)
    print('\n*** Apartado c) i) ***')
    print('\nError absoluto = ' + str(absolute_error(horner_function(4.62), -7.07)))
    print('\nError relativo = ' +
          str(relative_error(horner_function(4.62), -8.44)) + ' %')

    # Apartado c) ii)
    print('\n*** Apartado c) ii) ***')
    print('\nError absoluto = ' + str(absolute_error(horner_function(4.61), -7.07)))
    print('\nError relativo = ' +
          str(relative_error(horner_function(4.61), -8.44)) + ' %')


if __name__ == '__main__':
    run()


"""
Resultados obtenidos en los apartados del punto 6:
a) f(1.53) = - 7.90
b) f(1.53) = - 7.99
c) i) f(4.62) = - 7.07 
   ii) f(4.61) = - 8.44
4.62 y 4.61 provienen del cambio de variable y = e^x siendo x = 1.53
"""
