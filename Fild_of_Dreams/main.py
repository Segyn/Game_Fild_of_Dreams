import function

randon_word = function.create_randon_word()


def hide_word(randon_word1):
    print('Угадайте слово')
    print(randon_word)
    star = len(randon_word1) * '*'
    return star


def test_litter_in_word():
    litter_user = function.user_litter()
    word = []
    for i in randon_word:
        if i == litter_user:
            word.append(litter_user)
        else:
            word.append('*')
    return ''.join(word)


if __name__ == '__main__':
    print(hide_word(randon_word))
    print(test_litter_in_word())
