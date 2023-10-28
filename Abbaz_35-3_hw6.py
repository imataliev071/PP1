def numbers(*args):
    number = 1
    for i in args:
        number *= i
    return number
print(numbers(2, 3, 4, 5))



def word(letter='hello'):
    if letter == letter[::-1]:
        return True
    else:
        return False
print(word('hello'))



def calculate(number1, operator, number2):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '/':
        return number1 / number2
    elif operator == '*':
        return number1 * number2
    elif operator == '**':
        return number1 ** number2
    else:
        print('такого знака нету')

print(calculate(3,'**',3.99))