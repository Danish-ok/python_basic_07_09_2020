'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них.
'''
my_list = [7, 5, 3, 3, 2]
user_num = int(input('Введите рейтинг: '))
ind = True
for j, num in enumerate(my_list):
    if my_list[j] <= user_num:
        my_list.insert(j, user_num)
        ind = False
        break
if ind:
    my_list.append(user_num)
print(my_list)
# Вариант проще.
my_list = [7, 5, 3, 3, 2]
my_list.append(user_num)
my_list.sort(reverse=True)
print(my_list)
