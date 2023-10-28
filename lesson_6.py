# def greet(name, surname):
#     print(name, surname)
#
# greet('ff', 'df')

def min1(sequence):
    min_value = sequence[0]
    for i in sequence[1:]:
        if i < min_value:
            min_value = 1
    return min_value
print(min([2, 4, 5, 6, 1]))

# def sum(*a):
#     total = int(1)
#     for i in a:
#         total += i
#     return total
# sub = sum(1,2,3)
# print(sub)