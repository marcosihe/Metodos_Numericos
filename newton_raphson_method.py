import numpy as np


def f(x):
    return x**3 - x**2


def derivative(x):
    return 3*(x**2) - 2*x


def h(x):
    return x**10 - 1


def derivative_of_h(x):
    return 10*(x**9)


def f_2(x):
    if x >= 0:
        return np.sin(x) - 0.5*np.sqrt(x)
    else:
        print("\nEl valor pasado por parámetro no pertenece al dominio de la función f_2")


def derivative_of_f_2(x):
    if x >= 0:
        return np.cos(x) - 0.25/np.sqrt(x)
    else:
        print("\nEl valor pasado por parámetro no pertenece al dominio de la función derivada de f_2")


def g(x):
    return np.tan(x) - 0.5*x
# Se podría agregar un if para considerar los valores que no pertenecen al dominio de la tg x


def derivative_of_g(x):
    return 1/((np.cos(x))**2) - 0.5


def approximate_error(x0, x1):
    if x1 != 0:
        return np.abs((x1-x0)/x1)
# approximate_error me devuelve el error aproximado, el cual es el error que hay entre dos iteraciones
# sucesivas


def convergence_control(index, max_iterations, current_zero):
    if index > max_iterations:
        print("\nEl metodo no converge con el error deseado en " +
              str(max_iterations) + " iteraciones")
        print("Ultimo valor obtenido para la raiz: " + str(current_zero))
    else:
        print("\nLa raiz de la funcion dada es: " + str(current_zero))
        print("Y converge a la misma en " + str(index) + " iteraciones")
# El control de convergencia recibe como parámetros: la cantidad de iteraciones realizadas, la cantidad
# máxima de iteraciones permitidas y el último valor calculado para la raíz


def iterative_function(f, derivative, x0):
    if derivative(x0) != 0:
        return x0 - f(x0)/derivative(x0)


def newton_raphson_function(f, derivative, x0, max_iterations, error):

    index = 1
    x1 = iterative_function(f, derivative, x0)
    print("\n" + str(index) + "º iteración:\nRaiz: x = " + str(x1) +
          "\nError cometido: " + str(approximate_error(x0, x1)) + "\n")
    while (approximate_error(x0, x1) > error and index < max_iterations):

        x0 = x1
        x1 = iterative_function(f, derivative, x0)
        index += 1

        print("\n" + str(index) + "º iteración:\nRaiz: x = " + str(x1) +
              "\nError cometido: " + str(approximate_error(x0, x1)) + "\n")
    convergence_control(index, max_iterations, x1)


def run():

    print("*** METODOS NUMERICOS ***\n")
    error = 10**-3  # valor predefinido para el error que servirá como criterio de paro de los métodos
    max_iterations = int(
        input("Establecer el maximo numero de iteraciones deseado: "))
    x0 = np.sqrt(1/5)  # Valor inicial
    print("\nValor inicial: " + str(x0))

    #newton_raphson_function(f, derivative, x0, max_iterations, error)

    # newton_raphson_function(h, derivative_of_h, x0, max_iterations, error)

    newton_raphson_function(f_2, derivative_of_f_2, x0, max_iterations, error)

    #newton_raphson_function(g, derivative_of_g, x0, max_iterations, error)


if __name__ == '__main__':
    run()
