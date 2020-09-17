'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
 Для решения используйте цикл while и арифметические операции.
'''
user_num = ''
while not user_num.isdigit():
    user_num = input('Введите положительное целое число: ')
max_num = 0
val = int(user_num)
while val:
    if max_num < val % 10:
        max_num = val % 10
    val //= 10
print(max_num)
