import numpy as np

# El control de convergencia debe corregirse para el método de regula falsi, en cuanto al print
# que dice en cuantas iteraciones converge


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
# approximate_error me devuelve el error aproximado, el cual es el error que hay entre dos iteraciones
# sucesivas


def iterative_function(x0, x1):
    return (x1 - (f(x1)*(x1 - x0) / (f(x1) - f(x0))))
# La función iterativa se emplea en el método de la secante y de Regula Falsi para calcular el siguiente
# valor de la raíz


def convergence_control(index, max_iterations, current_zero, method):
    if index > max_iterations:
        print("\nEl metodo no converge con el error deseado en " +
              str(max_iterations) + " iteraciones")
        print("Ultimo valor obtenido para la raiz: " + str(current_zero))
    else:
        if method:
            index -= 1
        print("\nLa raiz de la funcion dada es: " + str(current_zero))
        print("Y converge a la misma en " + str(index) + " iteraciones")
# El control de convergencia recibe como parámetros: la cantidad de iteraciones realizadas, la cantidad
# máxima de iteraciones permitidas y el último valor calculado para la raíz
# el último parámetro sirve para identificar los métodos, donde 0 indica Secante o Fixed_Position y 1 es
# para el método de regula falsi


def secant_method(a, b, max_iterations, error):
    index = 1
    z_previous = a
    z_current = b
    z_next = iterative_function(a, b)
    while (approximate_error(z_current, z_next) > error and index < max_iterations):
        z_previous = z_current
        z_current = z_next
        z_next = iterative_function(z_previous, z_current)
        index += 1
    convergence_control(index, max_iterations, z_next, 0)

# En estos dos métodos máx_iterations es la cantidad máxima de iteraciones permitidas y error es el error
# predefinido mínimo que se desea. En el caso de la secante, a y b son los valores iniciales para estimar
# el valor de la pendiente de la función. En el caso del método regula falsi, estos valores corresponden a
# los extremos del intervalo que encierra a la raíz.


def regula_falsi_method(a, b, max_iterations, error):
    if f(a)*f(b) > 0:
        print("El intervalo ingresado no contiene a la raiz de la funcion dada")
    else:
        index = 1
        zero = iterative_function(a, b)
        print("\nX" + str(index) + " = " + str(zero))
        print("\nNo se puede calcular el error aproximado en la primera iteracion")

        z0 = zero
        z1 = b  # Le asigno b para que cumpla inicialmente con la condición del while
        while(index < max_iterations and approximate_error(z0, z1) > error):
            index += 1
            if f(a)*f(zero) > 0:
                a = zero
            else:
                b = zero

            z0 = zero
            # calculo la nueva raíz para el nuevo intervalo (a,b)
            zero = iterative_function(a, b)
            z1 = zero

            print("\nX" + str(index) + " = " + str(zero))
            print("Error aproximado de la iteracion " +
                  str(index) + ": " + str(approximate_error(z0, z1)))
        index += 1
        convergence_control(index, max_iterations, zero, 1)


def fixed_point_iteration(x0, max_iterations, error, g):
    index = 0
    previous_x = x0
    current_x = g(previous_x)
    while (index < max_iterations and approximate_error(previous_x, current_x) > error):
        if index == 0:
            print("\nX" + str(index+1) + " = " + str(g(previous_x)))
            print("Error aproximado de la iteracion " +
                  str(index+1) + ": " + str(approximate_error(previous_x, current_x)))

        previous_x = current_x
        current_x = g(previous_x)
        index += 1
        if index > 0:
            print("\nX" + str(index+1) + " = " + str(g(previous_x)))
            print("Error aproximado de la iteracion " +
                  str(index+1) + ": " + str(approximate_error(previous_x, current_x)))

    convergence_control(index+1, max_iterations, current_x, 0)
# El parámetro g que recibe la función es la función de prueba que se desea analizar: g1(x), g(2x) y g3(x)...


def run():
    print("*** METODOS NUMERICOS ***\nFuncion de prueba: f(x) = x^(-1) - tg x\n")
    error = 10**-3  # valor predefinido para el error que servirá como criterio de paro de los métodos
    x = float(input(
        "Ingrese el valor del limite inferior del interavalo que contiene a la raiz: "))
    y = float(input(
        "Ingrese otro valor del limite superior del intervalo que contiene a la raiz: "))
    iterations = int(
        input("Establecer el maximo numero de iteraciones deseado: "))
    print("\n*** Datos ***\nSe quiere calcular la raiz de la funcion:\nf(x) = x^(-1) - tg x\nen el intervalo [" + str(
        x) + "," + str(y) + "]\ncon un maximo de " + str(iterations) + " iteraciones y con un error menor a " + str(error) + "\n")
    # Aplicación del método de la Falsa Posición
    print("\n*** Metodo Regula Falsi ***")
    regula_falsi_method(x, y, iterations, error)

    # Aplicación del método de la Secante
    print("\n*** Metodo de la Secante ***")
    secant_method(x, y, iterations, error)

    # Aplicación del método de punto fijo
    print("\n*** Iteracion de punto fijo ***")
    x0 = float(input("Ingrese el valor inicial para Xo: "))
    iterations_2 = int(
        input("Establecer el maximo numero de iteraciones deseado: "))

    fixed_point_iteration(x0, iterations_2, error, g_3)


if __name__ == "__main__":
    run()
