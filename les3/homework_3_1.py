"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(arg1=0.0, arg2=1.0):
    """
    Возвращает частное от деления.
    :param arg1: делимое (по умолчанию 0.0)
    :param arg2: делитель (по умолчанию 1.0)
    :return: частное
    """

    result = (arg1 / arg2) if arg2 else 'На ноль делить нельзя'
    return result


def in_float():
    """
    Возвращает число пользователя с проверкой ввода.
    :return: float
    """
    num = None
    while not num:
        try:
            num = float(input('Введите число: '))
        except ValueError:
            print('Вы ввели не число')
        else:
            return num


num1 = in_float()
num2 = in_float()
print(division(num1, num2))
