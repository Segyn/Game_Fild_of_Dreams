import random

mylist = ['мама', 'папа', 'дедушка', 'бабушка']
# Массив русских букв.
rus_letters = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п",
               "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
# создание случайного слова.
randon_word_create = random.choice(mylist)


def hide_word(litter_user):
    a = input('введите букву: ')
    # проверка является ли введенный символ буквой
    if a.isalpha():
        # проверка буква русская или нет
        litter_user.append(a) if a in rus_letters else print('Ошибка! Нужно вводить одну русскую букву.')
    else:
        print('Ошибка! Нужно вводить одну русскую букву.')
    test_litter_in_word(litter_user)


def test_litter_in_word(litter_user):
    word = []
    for i in randon_word_create:
        word.append(i) if i in litter_user else word.append('*')

    word = ''.join(word)
    return print(word + '\nПобеда!') if word == randon_word_create else (print(word), hide_word(litter_user))


if __name__ == '__main__':
    # print(hide_word([]))
    test_litter_in_word([])
