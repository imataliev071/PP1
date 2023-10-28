# w - write - записать
# a - add добавить
# x - уникальное название
# r - показывает файл через консоль
# sleep() - выводит по строкам

# file = open('new_file.txt', 'w')
# file.write('БИШКЕК, КЫРГЫЗСТАН')
# file.close()

# with open('new_file.txt', 'w') as file:
    # file.write('\nВТОРАЯ СТРОКА')

# with open('new_file1.txt', 'x') as file:
#     file.write('new file')

# with open('new_file1.txt', 'w') as file:
#     print(file.read())
#     print()

with open('new.txt', 'w') as file:
    file.write('Здравствуйте')