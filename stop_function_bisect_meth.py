"""
Funcion util para usar en el metodo de biseccion. Con ella se puede pedir al usuario que elija el 
la manera de terminar las iteraciones. Ya sea elijiendo la cantidad maxima de las mismas o estableciendo 
el error relativo maximo con el que se desea obtener el cero de la funcion dada.
"""

import numpy as np


def stop_function():
    count = 0
    while True:
        chosen_option = int(input('Ingrese por teclado una de las siguiente opciones (1 o 2), segun corresponda:\n'
                                  + '1. Para establecer la cantidad maxima de iteraciones\n'
                                  + '2. Para establecer el maximo error relativo del cero de la funcion\n'))
        count += 1
        if (chosen_option == 1 or chosen_option == 2 or count == 3):
            if count == 3:
                print('\nSupero la cantidad maxima de intentos.\n')
            break
    if count < 3:
        if chosen_option == 1:
            stop_variable = int(
                input('\nIngrese la cantidad de iteraciones: '))
        else:
            stop_variable = float(
                input('\nIngrese el maximo error relativo: '))
        stop_array = np.array([chosen_option, stop_variable])
        return stop_array
    else:
        return 'Fin del programa.'


def run():
    print(stop_function())


if __name__ == '__main__':
    run()
