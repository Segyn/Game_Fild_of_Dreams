randon_word = 'мама'
litter_user = []


def test(litter_user):
    a = input('введите букву ')
    litter_user.append(a)
    return litter_user


def test_litter_in_word():
    word = []
    for i in randon_word:

        if i in litter_user:
            word.append(i)
        else:
            word.append('*')
    return word


if __name__ == '__main__':
    # print(test_litter_in_word())
    print(litter_user)
    test(litter_user)
    print(litter_user)
    test(litter_user)
    print(litter_user)