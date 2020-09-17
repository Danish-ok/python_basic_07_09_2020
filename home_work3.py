'''
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
 Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
'''

user_num = ''
while not user_num.isdigit():
    user_num = input('Введите положительное целое число: ')
num1 = int(user_num)
num2 = int(user_num + user_num)
num3 = int(user_num + user_num + user_num)
sum_num = num1 + num2 + num3
print(f'{num1} + {num2} + {num3} = {sum_num}')
