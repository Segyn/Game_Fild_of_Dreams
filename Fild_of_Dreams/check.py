import random

list = ['Мама', 'Папа', 'Дедушка', 'Бабушка']


def randon_word():
    randon_word = random.choice(list)
    print(randon_word)
    return len(randon_word) * '*'


# input('введите слово')

if __name__ == '__main__':
    print(randon_word())
