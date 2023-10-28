data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []

data_tuple == len(data_tuple)
data_tuple = list(data_tuple)

for i in data_tuple:
    letters.append(i) if type(i) == str else numbers.append(i)


numbers.remove(6.13)
res = letters.append(numbers.pop(numbers.index(1)))
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters[1] = "G"
letters[-2] = 'C'
numbers = ([i**2 for i in numbers if i > 0])
letters = tuple(letters)
numbers = tuple(numbers)
print(letters)
print(numbers)
