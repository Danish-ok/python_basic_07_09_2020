"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
"""

from itertools import count
from itertools import cycle

for num, el in enumerate(count(5)):
    if num - 10:
        print(el)
    else:
        break
my_list = ['A', 'B', 'C', 'ABC']
for var, itm in enumerate(cycle(my_list)):
    if var - 10:
        print(itm)
    else:
        break
