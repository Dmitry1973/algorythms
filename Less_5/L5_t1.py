# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple


def input_factory_data() -> list:
    """
    :return: -  the list of entered factory data
    f - as factory name
    q1...q4 as profits for corresponding quarters"""

    while True:
        f = input('enter factory name ')
        try:
            q1 = float(input('enter Q1 profit '))
            q2 = float(input('enter Q2 profit '))
            q3 = float(input('enter Q3 profit '))
            q4 = float(input('enter Q4 profit '))
            break
        except ValueError:
            print('not a float was entered')

    avg = (q1 + q2 + q3 + q4) / 4

    return [f, q1, q2, q3, q4, avg]


def list_of_factories():
    """
    :return: - list of namedtuples with factories data
    """
    while True:
        try:
            amount = int(input('enter number of factories '))
            break
        except ValueError:
            print('not a int was entered!')

    factory = []

    for i in range(amount):
        Factory = namedtuple('Factory', 'Factory Q1 Q2 Q3 Q4 AVG', defaults=['noname', 0,0,0,0,0])
        a = Factory._make(input_factory_data())
        factory.append(a)

    return factory


def get_average_profit():
    avg_p = list_of_factories()
    # average by all factories
    avg = 0
    for i in avg_p:
        avg = avg + i[5]
    avg = avg / len(avg_p)

    # dict factory : average annual profit
    prof = {}
    for i in range(len(avg_p)):
        prof[avg_p[i][0]] = avg_p[i][5]

    bigger = []
    lower = []
    for key, value in prof.items():
        if value > avg:
            bigger.append(key)
        else:
            lower.append(key)

    # to get dicts -> uncomment code below
    # bigger = {}
    # lower = {}
    # for key, value in prof.items():
    #     if value > avg:
    #         bigger[key] = value
    #     else:
    #         lower[key] = value

    return print('-'*30, '\n', f'annular average profit = {avg}',
                 '\n', '-'*30, '\n', 'bigger than average: ', *bigger,
                 '\n', '-'*30, '\n', 'lower or equal than average: ', *lower,)


def main():

    return get_average_profit()


main()


