import numpy as np


def run():
    a = np.array([(1, 0, 3), (4, 5, 6)])
    b = np.array([(1, 0, 3), (4, 5, 0)])

    # Operacione matemáticas
    print('El valor mínimo que hay en la matriz "a" es el: ' + str(a.min()))
    print('El valor máximo que hay en la matriz "a" es el: ' + str(a.max()))
    print('La suma de todos los elementos de la matriz "a" es: ' + str(a.sum()))

    # Raíz cuadrada de los elementos de la matriz
    print('\n*** Raíz cuadrada de todos los elementos de la matriz "a" ***')
    print(np.sqrt(a))

    # Desviación estándar de la matriz
    print('\n*** Desviación estándar de la matriz "a" ***')
    print(np.std(a))

    # Suma, resta, multiplicación, y división de dos matrices
    print('\n*** Suma de matrices: a + b ***')
    print(a+b)

    print('\n*** Resta: a - b ***')
    print(a-b)

    print('\n*** Producto de dos matrices: a . b ***')
    print(a*b)

    print('\n*** Cociente de dos matrices: a / b ***')
    print(a/b)

    # Observar los resultados en los casos: 0/0 y num/0


if __name__ == '__main__':
    run()
