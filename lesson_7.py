# lambda_funk = lambda a, b: a + b
# print(lambda_funk(2, 3))

# сключение
# try: - что проверять
# except: - ошибка найдена
# finally: - проверка завершена

# isinstance() - проверяет тип данных

from random import choice

students = [16, 4, 10, 13, 9, 2, 12, 11, 19]
topics = tuple(range(1, 8))
result = {}

while students:
    print(students)
    choice_students = choice(students)
    name = input(f'enter name for {choice_students}: '.title())
    rate = int(input(f'topic: {choice(students)}, rate for {name}: '))
    result[name] = rate
    students.reverse(choice_students)
    print(result)

print(sum(result))