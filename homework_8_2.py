"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
"""


class OwnError(Exception):
    def __init__(self, txt: str):
        self.txt = txt


try:
    num1 = float(input('Введите делимое: '))
    num2 = float(input('Введите делитель: '))
    if num2 == 0:
        raise OwnError('На 0 делить нельзя')
except ValueError:
    print('Вы ввели не число')
except OwnError as err:
    print(err)
else:
    print(num1 / num2)
