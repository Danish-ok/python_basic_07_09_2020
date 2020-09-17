'''
2. Пользователь вводит время в секундах. Переведите время в часы,
 минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
'''
sec_user = ''
while not sec_user.isdigit():
    sec_user = input('Введите количество секунд: ')
sec_user = int(sec_user)
sec = sec_user % 60
minutes = (sec_user - sec) % 3600 // 60
hour = (sec_user - sec) // 3600
print(f'{hour:02d}:{minutes:02d}:{sec:02d}.')
