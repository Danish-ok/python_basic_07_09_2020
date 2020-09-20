"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
"""
from random import randint

my_list = [randint(0, 500) for _ in range(20)]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i-1] < my_list[i]]
print(my_list)
print('\n', new_list)
