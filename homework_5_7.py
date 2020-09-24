"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
"""


def get_diff(param: list):
    """
    Вычисляет прибыль
    :param param:
    :return:
    """
    if param[2].isdigit() and param[3].isdigit():
        diff = float(param[2]) - float(param[3])
    else:
        diff = False
        print(param[0], 'Некорректные данные')
    return diff


comp_dict, su, count = {}, 0, 0
try:
    with open('task7.txt', 'r', encoding='UTF-8') as file:
        for line in file:
            var = line.split()  # [2:]
            profit = get_diff(var)
            if profit > 0:
                count += 1
                su += profit
            comp_dict[var[0]] = profit
    dict_prof = {'average_profit': su / count}
    end_list = [comp_dict, dict_prof]
    print(end_list)
except (NameError, FileNotFoundError):
    print('файл не существует')
