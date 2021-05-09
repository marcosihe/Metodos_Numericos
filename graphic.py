import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**-1 - np.tan(x)


def run():
    x = np.linspace(0.5, 1.5, 10000)
    plt.plot(x, f)

    plt.title("Grafica")
    plt.grid()
    plt.legend(('f'), loc='upper left')
    plt.show()


if __name__ == '__main__':
    run()
