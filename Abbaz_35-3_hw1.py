expenditure1 = int(input("Введите расход первого дня: "))
expenditure2 = int(input("Введите расход второго дня: "))
expenditure3 = int(input("Введите расход треьего дня: "))
expenditure4 = int(input("Введите расход четвертого дня: "))
expenditure5 = int(input("Введите расход пятого дня: "))
expenditure6 = int(input("Введите расход шестого дня: "))
expenditure7 = int(input("Введите расход седьмого дня: "))
summ_expenditure = expenditure1 + expenditure2 + expenditure3 + expenditure4 \
                    + expenditure5 + expenditure6 + expenditure7

days = 7
cred_summ_expenditure = round(summ_expenditure / days, 1)
if cred_summ_expenditure >= 10000:
    print('Вы протратили слишком много!')
elif 0 < cred_summ_expenditure <= 10000:
    print('Вы потратили достаточно денег!')
else:
    print('Вы не потратили денег!')
print(f'Общая сумма: {summ_expenditure} ')
print(f'Средний расход в день:  {cred_summ_expenditure}')