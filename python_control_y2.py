import numpy as np


def function_y2(number):
    return (np.sin(number + 2) + 2 * np.cos(3 * number))


def run():
    num_2 = float(
        input("\nIngrese el valor donde quiera evaluar la función y2: "))
    result_2 = function_y2(num_2)
    print('y(' + str(num_2) + ') = ' + str(result_2))


if __name__ == '__main__':
    run()
