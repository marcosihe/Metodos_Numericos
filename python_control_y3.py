import numpy as np


def function_y3(number):
    return np.exp(1+number)/(2*number)


def run():
    num_3 = float(
        input('\nIngrese el valor donde quiera evaluar la función y3: '))
    result_3 = function_y3(num_3)
    print('y(' + str(num_3) + ') = ' + str(result_3))


if __name__ == '__main__':
    run()
