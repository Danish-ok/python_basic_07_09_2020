"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает
учебный предмет и наличие лекционных, практических и лабораторных занятий
по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно были
все типы занятий. Сформировать словарь, содержащий название предмета и
общее количество занятий по нему. Вывести словарь на экран.
"""


def get_sum(param):
    for var in len(param.split('(')):
        print(var)


with open('task6.txt', 'r', encoding='UTF-8') as file:
    # print(file.readline().split()[2].split('('))
    for line in file:
        # get_sum(line.split()[1:])
        var = line.split()[1:]
        if '-' in var:
         var.remove('-')
        print(var)
