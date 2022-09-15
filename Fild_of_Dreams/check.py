import random

list = ['Мама', 'Папа', 'Дедушка', 'Бабушка']


def randon_world():
    return random.choice(list)


input('введите слово')

if __name__ == '__main__':
    print(randon_world())
