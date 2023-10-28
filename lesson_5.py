# словари - dict множества - set
# {ключ: значание}

# int str bool list tuple dict set

people2 = {
    'name': 'mishkat',
    'surname': 'sulaimanov',
    'age': 18,
    'hobbi': ['football', 'volleyball', 'tenis']
}

people = {
    'name': 'abbaz',
    'surname': 'Imataliev',
    'age': 18,
    'hobbi': ['football', 'volleyball', 'tenis']
}
people['age'] += 2
people['salam'] = ['hi', 'fj', 'df']
people['hobbi'].append('hello')
people['hobbi'].insert(2,'programmer')
people.update(people2)
people['age'] += 2
people2['hobbi'][1] = 'xex'
people.pop('salam')

counter = 1
for i in people:
    print(counter, ')', i, ':', people[i])
    counter += 1

# print(people)




# menu = {
#     'lagman': {'meat', 'dough', 'pepper'},
#     'plov': {'rice', 'carrot', 'meat'},
#     'sup': {'carrot', 'water', 'potato'},
#     'steak': {'meat'},
#     'samsa': {'dough', 'onion', 'potato'}
# }
#
# enter_eat = input('Какое блюдо вы хотите?: ')
# print(menu.get(enter_eat))

