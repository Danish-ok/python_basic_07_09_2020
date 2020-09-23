"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел,
разделенных пробелами. Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
from random import randint


def my_gen(val: int):
    for _ in range(val):
        yield randint(0, 30)


with open('task5.txt', 'w', encoding='UTF-8') as file:
    for var in my_gen(5):
        print(var, end=' ', file=file)
try:
    with open('task5.txt', 'r', encoding='UTF-8') as file:
        file = [int(num) for num in file.read().split()]
        print(f'Ряд чисел {file} дают сумму {sum(file)}')
except FileNotFoundError:
    print('файл не существует')
