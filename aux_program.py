import numpy as np


def f(x):
    return x**-1 - np.tan(x)


def g_1(x):
    if x > -1.5:
        return np.sqrt(2*x+3)
    else:
        print("\nEl valor ingresado '" + str(x) +
              "' no pertenece al dominio de la función\n")


def g_2(x):
    return (x**2 - 3)/2


def g_3(x):
    if x != 2:
        return 3/(x-2)
    else:
        print("\nEl valor ingresado '" + str(x) +
              "' no pertenece al dominio de la función\n")


def approximate_error(x0, x1):
    if x1 != 0:
        return np.abs((x1-x0)/x1)


def convergence_control(index, max_iterations, current_zero):
    if index > max_iterations:
        print("\nEl metodo no converge con el error deseado en " +
              str(max_iterations) + " iteraciones")
        print("\nUltimo valor obtenido para la raiz: " + str(current_zero))
    else:
        print("\nLa raiz de la funcion dada es: " + str(current_zero))
        print("Y converge a la misma en " + str(index) + " iteraciones")


def fixed_point_iteration(x0, max_iterations, error):
    index = 0
    previous_x = x0
    current_x = g_1(previous_x)
    while (index < max_iterations and approximate_error(previous_x, current_x) > error):
        if index == 0:
            print("\nX" + str(index+1) + " = " + str(g_1(previous_x)))
            print("Error aproximado de la iteracion " +
                  str(index+1) + ": " + str(approximate_error(previous_x, current_x)))

        previous_x = current_x
        current_x = g_1(previous_x)
        index += 1
        if index > 0:
            print("\nX" + str(index+1) + " = " + str(g_1(previous_x)))
            print("Error aproximado de la iteracion " +
                  str(index+1) + ": " + str(approximate_error(previous_x, current_x)))

    convergence_control(index+1, max_iterations, current_x)


def run():
    #a = float(input("Ingrese el valor para a: "))
    #b = float(input("Ingrese el valor para b"))
    #zero = b - f(b) * (b-a) / (f(b) - f(a))
    #print("zero = " + str(zero))

    x = float(input("Ingrese el valor inicial para Xo: "))
    iterations = int(
        input("Establecer el maximo numero de iteraciones deseado: "))
    error = 10**-3

    fixed_point_iteration(x, iterations, error)


if __name__ == "__main__":
    run()
