"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def max_sum(arg1, arg2, arg3):
    """
    Возвращает сумму ТОР-2
    :param arg1: int or float
    :param arg2: int or float
    :param arg3: int or float
    :return: int or float
    """
    # var = sorted([arg1, arg2, arg3]) # доп вариант решения
    # return(var[1] + var[2])
    return sum([arg1, arg2, arg3]) - min([arg1, arg2, arg3])


print(max_sum(3, -5.2, 7))
