import function

randon_word = function.create_randon_word()
print('Угадайте слово')


def hide_word(litter_user):
    a = input('введите букву ')
    litter_user.append(a)
    test_litter_in_word(litter_user)


def test_litter_in_word(litter_user):
    word = []
    for i in randon_word:
        if i in litter_user:
            word.append(i)
        else:
            word.append('*')
    word = ''.join(word)
    if word == randon_word:
        return print(word + '\nПобеда!')
    else:
        print(word)
        hide_word(litter_user)


if __name__ == '__main__':
    test_litter_in_word([])
