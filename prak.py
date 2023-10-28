# цикл
# i = 1
# while i <= 10:
#     if i != 8:
#         print(i)
#     i += 1
#     continue
#
# # списки
# # name = ['abbas', 'mishkat', 'alish', 2]
# # name1 = ['roza', 'abbazz']
# # name[1] = 'samara'
# # name[3] += 10
# # print(name)
# # print(name1)
#
# # word = 'abbas'
# # print(word[0:5])
# # print(word[1:5])
# # print(word[::-1])
# # print(word[:-1])
#
# # rus = "йцукенгшщзхъфывапролджэячсмитьбю"
# # eng = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
# # enter_word = input('Введите слово: ')
# # for i in rus:
# #     if
#
# osen = int(input('Введите оценку: '))
# for osen in range[1::]:
#     if osen == 5:
#         break
#

# Импортируем необходимые библиотеки
import operator

# Читаем данные из файла
with open('results.txt', 'r') as f:
    lines = f.readlines()

# Создаем словарь
results = {}
for line in lines:
    name, score = line.strip().split()
    results[name] = int(score)

# Сортируем словарь по значению в убывающем порядке
sorted_results = dict(sorted(results.items(), key=operator.itemgetter(1), reverse=True))

# Выводим топ-3 лучших студента по оценке
print('Топ-3 студентов:')
for i, (name, score) in enumerate(sorted_results.items()):
    if i == 3:
        break
    print(f'{name}: {score}')

# Выводим среднюю оценку
average_score = sum(sorted_results.values()) / len(sorted_results)
print(f'Средняя оценка: {average_score}')

# Создаем новый текстовый файл на основе отсортированного словаря
with open('sorted_results.txt', 'w') as f:
    for name, score in sorted_results.items():
        f.write(f'{name} {score}\n')
