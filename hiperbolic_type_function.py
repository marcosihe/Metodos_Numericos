import numpy as np


def hiperbolic_type_function(x):
    return np.sinh(x)/x


def run():
    for index in range(1, 21):
        test_variable = (10 ** (-index))
        print(hiperbolic_type_function(test_variable))


if __name__ == '__main__':
    run()
