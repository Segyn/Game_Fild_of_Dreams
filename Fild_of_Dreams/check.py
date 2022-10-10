import random
from langdetect import detect

mylist = ['мама', 'папа', 'дедушка', 'бабушка']

randon_word_create = random.choice(mylist)


def hide_word(litter_user):
    a = input('введите букву ')
    print(detect(a))
    litter_user.append(a)
    return litter_user


#     test_litter_in_word(litter_user)


# def test_litter_in_word(litter_user):
#     word = []
#     for i in randon_word_create:
#         word.append(i) if i in litter_user else word.append('*')
#
#     word = ''.join(word)
#     return print(word + '\nПобеда!') if word == randon_word_create else (print(word), hide_word(litter_user))


if __name__ == '__main__':
    print(hide_word([]))
