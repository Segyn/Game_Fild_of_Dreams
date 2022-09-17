import random

mylist = ['Мама', 'Папа', 'Дедушка', 'Бабушка']


def randon_word():
    randon_word = random.choice(mylist)
    print(randon_word)
    return len(randon_word) * '*'


def word_user():
    user_word = input('Введите букву: ')
    return user_word


if __name__ == '__main__':
    print(randon_word())
    print(word_user())
