"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка
на наличие только чисел. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока
пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только
числа и строки. При вводе пользователем очередного элемента необходимо
реализовать проверку типа элемента и вносить его в список, только если введено число.
Класс-исключение должен не позволить пользователю ввести текст (не число) и
отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
"""


class OwnError(Exception):
    def __init__(self, txt: str):
        self.txt = txt


my_list = []
while True:
    try:
        num = input('Введите число: ')
        if num == 'q':
            break
        if num.isalpha():
            raise OwnError('Вы ввели не число')
        num = float(num)
    except OwnError as err:
        print(err)
    else:
        my_list.append(num)
print(my_list)
