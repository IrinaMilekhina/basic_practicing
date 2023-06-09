'''
Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков
(по одному из каждого):
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
Например:
 get_jokes(2)
["лес завтра зеленый", "город вчера веселый"]
Документировать код функции.
Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы
слов в шутках (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы
сделать аргументы именованными?
'''
from random import choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

print('FIRST PART'.center(100, '-'), '\n')


def get_jokes(quantity=1):
    """
    Generates random 3-word jokes

    :param quantity: how many lame jokes do you want
    :return: list of generated jokes in strings
    """
    jokes = []
    for i in range(quantity):
        jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    return jokes


print(get_jokes(3))

print('\n', 'SECOND PART'.center(99, '-'), '\n')


def get_jokes_flag(quantity=1, unique=False):
    """
    Generates random 3-word jokes

    :param quantity: how many lame jokes do you want
    :param unique: word repeating: True or False. True - words can not be repeated; False - words can be repeated
    :return: list of generated jokes in strings
    """
    jokes = []
    changeable_noun_list = nouns.copy()
    changeable_adverb_list = adverbs.copy()
    changeable_adjective_list = adjectives.copy()
    limit_for_true = len(nouns) + 1
    if type(unique) is bool:
        for i in range(quantity):
            noun = choice(changeable_noun_list)
            adverb = choice(changeable_adverb_list)
            adjective = choice(changeable_adjective_list)
            jokes.append(f'{noun} {adverb} {adjective}')
            if unique is True:
                if quantity not in range(limit_for_true):
                    return 'Error. There can not be more jokes than elements in list of nouns'
                changeable_noun_list.remove(noun)
                changeable_adverb_list.remove(adverb)
                changeable_adjective_list.remove(adjective)
    else:
        return 'Error. Invalid value for "unique". True or False only'
    return jokes


print(get_jokes_flag(5, True))
print(get_jokes_flag(3))
