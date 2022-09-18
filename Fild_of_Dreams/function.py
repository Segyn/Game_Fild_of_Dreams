import random

mylist = ['Мама', 'Папа', 'Дедушка', 'Бабушка']


def create_randon_word() -> str:
    randon_word_create = random.choice(mylist)
    return randon_word_create

def user_litter() -> str:
    litter_user = input('Введите букву: ')
    return litter_user