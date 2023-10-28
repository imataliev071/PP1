counter = 10

while counter > 0:
    print(f'у вас осталось {counter} попыток')
    birthday = int(input('Введите день рождения: '))
    month = int(input('Введите месяц рождения: '))

    if (21 <= birthday <= 31 and month == 3) or (month == 4 and 1 <= birthday <= 20):
        print('Овен')
    elif (21 <= birthday <= 30 and month == 4) or (month == 5 and 1 <= birthday <= 21):
        print('Телец')
    elif (21 <= birthday <= 31 and month == 5) or (month == 6 and 1 <= birthday <= 21):
        print('Близнецы')
    elif (22 <= birthday <= 30 and month == 6) or (month == 7 and 1 <= birthday <= 22):
        print('Рак')
    elif (23 <= birthday <= 31 and month == 7) or (month == 8 and 1 <= birthday <= 21):
        print('Лев')
    elif (22 <= birthday <= 31 and month == 8) or (month == 9 and 1 <= birthday <= 23):
        print('Дева')
    elif (24 <= birthday <= 30 and month == 9) or (month == 10 and 1 <= birthday <= 23):
        print('Весы')
    elif (24 <= birthday <= 31 and month == 10) or (month == 11 and 1 <= birthday <= 22):
        print('Скорпион')
    elif (23 <= birthday <= 30 and month == 11) or (month == 12 and 1 <= birthday <= 22):
        print('Стрелец')
    elif (23 <= birthday <= 31 and month == 12) or (month == 1 and 1 <= birthday <= 20):
        print('Козерог')
    elif (21 <= birthday <= 31 and month == 1) or (month == 2 and 1 <= birthday <= 19):
        print('Водолей')
    elif (20 <= birthday <= 29 and month == 2) or (month == 3 and 1 <= birthday <= 20):
        print('Рыбы')
    elif birthday > 31 or month > 12:
        print('вы не правильно ввели')
    else:
        print('ошибка')
    counter -= 1
