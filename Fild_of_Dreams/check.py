randon_word = 'мама'
litter_user = []


def test(litter_user):
    a = input('введите букву ')
    litter_user.append(a)
    test_litter_in_word()


def test_litter_in_word():
    word = []
    for i in randon_word:

        if i in litter_user:
            word.append(i)
        else:
            word.append('*')
    new_word = ''.join(word)

    if new_word == randon_word:
        return print(new_word+'\nПобеда!')
    else:
        print(new_word)
        test(litter_user)


if __name__ == '__main__':
    test_litter_in_word()
