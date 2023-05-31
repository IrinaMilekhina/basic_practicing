'''
Задание 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 с английского на русский язык.
Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"
Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
перевода: какой тип данных выбрать, в теле функции или снаружи.

Задание 2. Обработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
'''
# task 1
print('FIRST PART'.center(100, '-'), '\n')


def num_translate(number):
    """
    Translates english numbers from 0 to 10 into russian

    :param number: number you want to translate. ONLY word form
    :return: printed translation
    """
    translations = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number in translations.keys():
        print(translations[number])
    else:
        print('None')


num_translate('zero')
num_translate('eleven')

# task 2
print('\n', 'SECOND PART'.center(100, '-'))


def num_translate_adv(number):
    translations = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number.lower() in translations.keys():
        if number.istitle():
            number = number.lower()
            print(translations[number].capitalize())
        elif number.islower():
            print(translations[number])
        else:
            print('None')
    else:
        print('None')


num_translate_adv('one')
num_translate_adv('Two')
num_translate_adv('tHree')
num_translate_adv('twelve')
