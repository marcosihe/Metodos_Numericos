import numpy as np


def run():
    # Conocer la dimensión de una matriz
    a = np.array([(1, 2, 3), (4, 5, 6)])

    print('La dimensión de la matriz "a" es: ' + str(a.ndim))

    # Conocer el tipo de dato almacenado en una matriz
    print('Los datos almacenados en la matriz "a" son de tipo: ' + str(a.dtype))

    # Conocer el tamaño y forma de la matriz
    print('Tamaño de la matriz "a": ' + str(a.size))
    print('Forma de la matriz "a": ' + str(a.shape))

    # Cambio de la forma de una matriz
    print('\n*** Matriz original ***')
    print(a)
    print('\n*** Matriz cambiada ***')
    print(a.reshape(3, 2))

    # Extraer un elemento de la matriz - Se debe especificar la fila y columna donde está ubicado
    print('\n*** Elemento de la fila 2 y columna 3 ***')
    print(a[1, 2])  # Las numeraciones de filas y columnas comienzan siempre en 0

    # Extraer todos los elementos de todas las filas de una determinada columna
    print(a[0:, 2])
    # Con el 0 se indica desde donde, y como no se aclara hasta donde, trae todos.
    # El parámetro '2' hace referencia a la columna deseada


if __name__ == '__main__':
    run()
