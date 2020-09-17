'''
6. * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
 Каждый кортеж хранит информацию об отдельном товаре.
  В кортеже должно быть два элемента — номер товара и словарь с параметрами
   (характеристиками товара: название, цена, количество, единица измерения).
    Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
'''
goods = ()
goods_list = []
result = {}
lot = int(input('Введите количество товара: '))
name_list = ['название', 'цена', 'количество', 'ед.']
for num in range(lot):
    price = {name: input(name + ': ') for name in name_list}
    goods = (num + 1, price)
    goods_list.append(goods)
print(goods_list)
for name in name_list:
    name_value = []
    for num in range(lot):
        name_value.append(goods_list[num][1][name])
    result[name] = list(set(name_value))
print(result)
