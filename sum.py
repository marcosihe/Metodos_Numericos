import decimal


def sum():
    sum = 0
    for i in range(1, 11):
        sum += 0.1
    return sum


def exact_sum():
    sum = 0
    for i in range(1, 11):
        sum += decimal.Decimal("0.1")
    print(sum)


def run():
    print('*** Sin usar el módulo "Decimal" ***')
    print(sum())
    print('\n*** Usando el módulo "Decimal" ***')
    exact_sum()


if __name__ == '__main__':
    run()
