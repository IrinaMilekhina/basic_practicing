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

    :param quantity: How many lame jokes do you want
    :return: Printed list of generated jokes in strings
    """
    jokes = []
    for i in range(quantity):
        jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    print(jokes)


get_jokes(3)

print('\n', 'SECOND PART'.center(100, '-'))


def get_jokes_flag(quantity=1, unique=False):
    """
    Generates random 3-word jokes

    :param quantity: How many lame jokes do you want
    :param unique: Word repeating: True or False. True - words can not be repeated; False - words can be repeated
    :return: Printed list of generated jokes in strings
    """
    jokes = []
    if unique is False:
        for i in range(quantity):
            jokes.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')
    else:
        if quantity not in range(len(nouns)+1):
            print('Error. There can not be more jokes than elements in list of nouns')
        else:
            used_words = []
            for i in range(quantity):
                jokes_element = []
                noun = choice(nouns)
                while noun in used_words:
                    noun = choice(nouns)
                jokes_element.append(noun)
                used_words.append(noun)
                adverb = choice(adverbs)
                while adverb in used_words:
                    adverb = choice(adverbs)
                jokes_element.append(adverb)
                used_words.append(adverb)
                adjective = choice(adjectives)
                while adjective in used_words:
                    adjective = choice(adjectives)
                jokes_element.append(adjective)
                used_words.append(adjective)
                jokes.append(' '.join(jokes_element))
    print(jokes)


get_jokes_flag(5, True)
