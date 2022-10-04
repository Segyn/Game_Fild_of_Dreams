import random

mylist = ['мама', 'папа', 'дедушка', 'бабушка']


def create_randon_word() -> str:
    randon_word_create = random.choice(mylist)
    return randon_word_create

# def user_litter() -> str:
#     litter_user = input('Введите букву: ')
#     return litter_user
