import numpy as np


def hyperbolic_type_function(x):
    return np.sinh(x)/x


def run():
    for index in range(1, 21):
        test_variable = (10 ** (-index))
        print(hyperbolic_type_function(test_variable))


if __name__ == '__main__':
    run()
