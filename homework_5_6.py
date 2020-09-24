"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий
по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были
все типы занятий. Сформировать словарь, содержащий название предмета и
общее количество занятий по нему. Вывести словарь на экран.
"""


def get_sum(param: list):
    """
    Get sum in line
    :param param:
    :return: int
    """
    su = 0
    for el in param:
        itm = ''.join(filter(str.isdigit, el))
        su += int(itm) if itm.isdigit() else 0
    return su


try:
    with open('task6.txt', 'r', encoding='UTF-8') as file:
        new_dict = {}
        for line in file:
            var = line.split()[1:]
            new_dict[line.split()[0]] = get_sum(var)
    print(new_dict)
except FileNotFoundError:
    print('файл не существует')
