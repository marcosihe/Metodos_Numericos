import numpy as np


def run():
    a = np.array([1, 2, 3, 4, 5, 6])
    print(a)

    # Creando una copia de 'a' en un vector llamado 'b'
    b = a.copy()

    # Modificando el primer elemento de 'a'
    a[0] = 21

    # Verificando que 'b' no se haya modificado y que el vector 'a' sí lo haya hecho
    print(b)
    print(a)


if __name__ == '__main__':
    run()
