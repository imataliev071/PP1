domen = {
    'kg': {'red', 'yellow'},
    'kz': {'blue', 'yellow'},
    'ru': {'white', 'red', 'blue'},
    'uz': {'blue', 'white', 'green'}
}
while True:
    print('"Стоп" для выхода')
    enter_colors = input('Введите цвет флага: ').lower()
    if enter_colors == 'стоп':
        break
    fal = False
    for key, value in domen.items():
        if set(enter_colors.split()).issubset(value):
            print(key)
            fal = True
    if fal == False:
            print('Такого света нету')




















