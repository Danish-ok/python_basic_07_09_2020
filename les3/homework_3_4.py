"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать
в виде функции my_func(x, y). При решении задания необходимо обойтись
без встроенной функции возведения числа в степень.
"""


def my_func(x, y):
    """
    Возводит в отрицательную степень число
    :param x: положительное число
    :param y: отрицательная степень
    :return: float
    """
    result1 = x ** y
    var = x
    for _ in range(1, abs(y)):
        x *= var
    result2 = 1 / x
    return result1, result2


def num_input(arg, asc, type_arg):
    """
    Получает от пользователя положительное float  и (- int)
    :param arg: определяет знак числа
    :param asc: вопрос на ввод
    :param type_arg: тип данных
    :return: float or int
    """
    num = 0
    while num * arg <= 0:
        try:
            num = num if num * arg > 0 else type_arg(input(asc))
        except ValueError:
            print('Ошибка ввода')
    return num


x_pos_float = num_input(1, 'Введите положительное число: ', float)
y_neg_int = num_input(-1, 'Введите целое отрицательное число: ', int)
print(my_func(x_pos_float, y_neg_int))
