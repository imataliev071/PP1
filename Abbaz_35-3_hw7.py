ten = list(range(1, 11))
evens = list(filter(lambda num: num % 2 == 0, ten))
print(list(map(lambda num1: num1 ** 2, evens)))
def index(lst=ten):
    while True:
        try:
            enter_index = int(input("Введите индекс от 1 до 9: "))
            if enter_index == 00:
                break
            if 0 <= enter_index < len(lst):
                print(f"Элемент по индексу {enter_index}: {lst[enter_index]}")
            else:
                print(f"Неверный индекс. Индекс должен быть от 0 до {len(lst) - 1}.")
        except ValueError:
            print("Пожалуйста, введите целое число.")

index()



