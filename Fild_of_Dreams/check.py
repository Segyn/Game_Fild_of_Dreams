randon_word = 'мама'
litter_user = 'а'


def test_litter_in_word():
    word = []
    for i in randon_word:

        if i == litter_user:
            word.append(litter_user)
        else:
            word.append('*')
    return word


if __name__ == '__main__':
    print(test_litter_in_word())
