'''
5. Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
 (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
 Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
 (соотношение прибыли к выручке). Далее запросите численность сотрудников фирмы
  и определите прибыль фирмы в расчете на одного сотрудника.
'''
per = input('Введите отчетный период (месяц, кварлтал...):')
revenue, cost = '', ''
while not revenue.isdigit():
    revenue = input(f'Введите выручку компании за {per}: ')
while not cost.isdigit():
    cost = input(f'Введите издержки компании за {per}: ')
profit = int(revenue) - int(cost)
if profit >= 0:
    print(f'\n\tПрибыль компании за {per} составила {profit}.')
    if int(revenue) == 0:
        revenue = 1
    profitability = profit / int(revenue) * 100
    print(f'\n\tРентабельность выручки за {per} составила {profitability}%.\n')
    working = ''
    while not working.isdigit():
        working = input('Введите численность сотрудников фирмы: ')
    if int(working) == 0:
        working = '1'
    efficiency_working = profit / int(working)
    print(f'\n\tПрибыль фирмы в расчете на одного сотрудника за {per} составила {efficiency_working}.')
else:
    print(f'\n\tК сожалению, за {per} убытки компании составили {profit}.')
