while True:
    enter_word = input('Введите слово: ').lower()
    if enter_word == 'стоп' or enter_word == 'stop':
        break
    glasn = 'aeiouyаеёиоуыэюя'
    soglasn = 'bсdfghklmnpqrstvxzбвгджзйклмнпрстфхцчшщ'
    letter = len(enter_word)
    how_glasn = len([i for i in enter_word.lower() if i in glasn])
    how_soglasn = len([i for i in enter_word.lower() if i in soglasn])
    glasn_pr = how_glasn / letter * 100
    soglasn_pr = how_soglasn / letter * 100
    print(f'символов: {letter}')
    print(f'гласный: {how_glasn}')
    print(f'согласный: {how_soglasn}')
    print(f'гласный: {glasn_pr}')
    print(f'согласный: {soglasn_pr}')
    print('Введите "стоп" чтобы выйти')