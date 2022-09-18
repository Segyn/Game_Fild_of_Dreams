import random

mylist = ['Мама', 'Папа', 'Дедушка', 'Бабушка']


def create_randon_word() -> str:
    randon_word_create = random.choice(mylist)
    return randon_word_create


randon_word = create_randon_word()
print(randon_word)


def hide_world(randon_word1):
    print('Угадайте слово')
    star = len(randon_word1) * '*'
    return star


def user_litter() -> str:
    litter_user = input('Введите букву: ')
    return litter_user


if __name__ == '__main__':
    print(hide_world(randon_word))
    # print(word_user())
