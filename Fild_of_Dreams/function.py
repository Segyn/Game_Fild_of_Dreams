import random

mylist = ['мама', 'папа', 'дедушка', 'бабушка']
# Выбираем случайное слово из списка
randon_word_create = random.choice(mylist)


# Запрашиваем у пользователя букву и добавляем её в список введенных букв
def hide_word(litter_user):
    new_word = input('введите букву ')
    litter_user.append(new_word)
    test_litter_in_word(litter_user)


# основная функция по угадыванию случайного слова.
def test_litter_in_word(litter_user):
    # Создаем проверочное слово
    test_word = []
    # Проверяем список введенных букв, на наличие в нем букв из загаданного слова.
    # Если буква есть она записывается на свое место, если буквы в списки нет, то звездочка.
    for i in randon_word_create:
        test_word.append(i) if i in litter_user else test_word.append('*')

    # Сверяем проверочное слово с загаданным.
    # Если оно совпадает заканчиваем игру, иначе отправляем вводить новую букву.
    test_word = ''.join(test_word)
    return print(f'{test_word}\nПобеда!') if test_word == randon_word_create else (
    print(test_word), hide_word(litter_user))
