"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
класса (метод __init__()), который должен принимать данные (список списков)
для формирования матрицы.
"""


# def creator(matr):
# def wrapper(itm):
# matr(itm)
# for i in itm:
#  for j in i:
# print(f'|  {j} ', end=' ')
#  print('\n')

# return wrapper


# @creator
class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        result = ''
        for itm in self.data:
            result += ' '.join(map(str, itm)) + '\n'
        return result


tab1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tab2 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
print(tab1)
print(tab2)
print(tab1 + tab2)
