import random

mylist = ['мама', 'папа', 'дедушка', 'бабушка']

randon_word_create = random.choice(mylist)


def hide_word(litter_user):
    a = input('введите букву ')
    litter_user.append(a)
    test_litter_in_word(litter_user)


def test_litter_in_word(litter_user):
    word = []
    for i in randon_word_create:
        if i in litter_user:
            word.append(i)
        else:
            word.append('*')
    word = ''.join(word)
    if word == randon_word_create:
        return print(word + '\nПобеда!')
    else:
        print(word)
        hide_word(litter_user)
