import random

mylist = ['Мама', 'Папа', 'Дедушка', 'Бабушка']


def create_randon_word() -> str:
    randon_word1 = random.choice(mylist)
    return randon_word1


randon_word = create_randon_word()


def hide_world(randon_word):
    star = len(randon_word) * '*'
    return star


# def word_user() -> str:
#     user_word = input('Введите букву: ')
#     return user_word


if __name__ == '__main__':
    print(create_randon_word())
    print(hide_world(randon_word))
    # print(word_user())
