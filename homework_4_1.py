"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета
заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных
значений необходимо запускать скрипт с параметрами.
"""

from sys import argv


def wages_fun(prod: str, rat: str, pri: str):
    """
    Вычисляет зарплату
    :param prod: выработка в часах
    :param rat: ставка
    :param pri: премия
    :return: зарплата
    """
    return float(prod) * float(rat) + float(pri)


script, production, rates, prize = argv
wages = wages_fun(prod=production, rat=rates, pri=prize)
print(wages)
