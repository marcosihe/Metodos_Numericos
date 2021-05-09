import numpy as np
# from error_calculator import *


def f(x):
    return x ** (-1) - np.tan(x)
    # return np.sin(x)


def approximate_error(x0, x1):
    return np.abs((x1-x0)/x1)


def convergence_control(index, max_iterations, current_zero):
    if index >= max_iterations:
        print("El metodo no converge con el error deseado en " +
              str(max_iterations) + " iteraciones")
        print("Ultimo valor obtenido para la raiz: " + str(current_zero))
    else:
        print("La raiz de la funcion dada es: " + str(current_zero))
        print("Y converge a la misma en " + str(index) + " iteraciones")


def bisection_method(a, b, max_iterations, error):
    z1 = b
    if f(a)*f(b) > 0:
        print("El intervalo ingresado no contiene a la raiz de la funcion dada")
    else:
        index = 1
        zero = (a+b)/2
        z0 = zero
        # while(index < max_iterations and np.abs(b-a) > error):
        while(index < max_iterations and approximate_error(z0, z1) > error):
            if f(a)*f(zero) > 0:
                a = zero
            else:
                b = zero
            if index > 1:
                print("\nError aproximado de la iteracion " +
                      str(index) + ": " + str(approximate_error(z0, z1)))
            zero = (a+b)/2
            z1 = zero
            index += 1
        convergence_control(index, max_iterations, zero)


def run():
    print('*** Metodo de biseccion ***\n\nIngrese el intervalo donde desea calcular la raiz de la funcion')
    error = 10**-3
    a = float(input('\nIngrese el primer valor del intervalo: '))
    b = float(input('\nIngrese el segundo valor del intervalo: '))
    iterations = int(input("Establecer el numero maximo de iteraciones: "))
    bisection_method(a, b, iterations, error)


if __name__ == '__main__':
    run()
