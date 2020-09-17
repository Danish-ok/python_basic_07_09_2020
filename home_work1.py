'''
1. Поработайте с переменными, создайте несколько, выведите на экран,
 запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
'''

var_str1 = 'сто'
var_str2 = 'пятьдесят'
print(var_str1, '+', var_str2, end=' = ')
print(''.join(var_str1 + var_str2))
var_int = 100
var_int2 = 50
print(var_int2 + var_int)
print(f'{var_str1 + var_str2} это {var_int + var_int2}')

user_name = input('Введите ваше имя: ')
user_age = ''
while not user_age.isdigit():
    user_age = input('Введите ваш возраст: ')
user_age = int(user_age)
print(user_name, 'вы родились в', 2020 - user_age, 'году.')
