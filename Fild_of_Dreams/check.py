randon_word = 'мама'
litter_user = ['а', 'c', 'м']


def test_litter_in_word():
    word = []
    for i in randon_word:

        if i in litter_user:
            word.append(i)
        else:
            word.append('*')
    return word


if __name__ == '__main__':
    print(test_litter_in_word())
