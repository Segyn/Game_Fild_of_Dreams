import random

mylist = ['Мама', 'Папа', 'Дедушка', 'Бабушка']


def create_randon_word() -> str:
    randon_word_create = random.choice(mylist)
    return randon_word_create
