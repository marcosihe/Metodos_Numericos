import numpy as np
from error_calculator import *


def test_function(x):
    return x ** (-1) - np.tan(x)


def range_control(a, b):
    if (test_function(a)*test_function(b) < 0):
        return True
    else:
        return False


def ask_for_data():
    count_1 = 0
    count_2 = 0

    while True:
        iterations = int(
            input('\nIngrese la cantidad maxima de iteraciones: '))
        count_1 += 1
        if (iterations > 0 or count_1 > 2):
            break
    if count_1 < 3:
        while True:
            error = float(input('\nIngrese el maximo error relativo: '))
            count_2 += 1
            if (error > 0 or count_2 > 2):
                break
    if count_1 > 2 or count_2 > 2:
        data_array = ([0, 0])
        return data_array
    else:
        data_array = np.array([iterations, error])
        return data_array


def bisection_function(a, b, iterations, error):
    zero = (a+b)/2
    index = 1
    while (index <= iterations and np.abs(test_function(zero)) > error):
        if test_function(a)*test_function(zero) < 0:
            a = zero
        else:
            b = zero
        #print('Erro de la ' + str(index) + 'º iteracion: ' + relative_error())
        index += 1
        zero = (a+b)/2
    if index > iterations:
        print('\nNo converge en ' + str(iterations) + ' iteraciones.')
    else:
        print('\nel cero de la funcion dada es: ' + str(zero))


def run():
    print('*** Metodo de biseccion ***\n\nIngrese el intervalo donde desea calcular la raiz de la funcion')
    a = float(input('\nIngrese el primer valor del intervalo: '))
    b = float(input('\nIngrese el segundo valor del intervalo: '))
    if range_control(a, b):
        data_array = ask_for_data()
        if data_array[0] == 0:
            print('Ingreso incorrecto de datos.\nFin del programa')
        else:
            bisection_function(a, b, data_array[0], data_array[1])
    else:
        print('\nIntervalo de la funcion no valido para el metodo de biseccion.')


if __name__ == '__main__':
    run()
