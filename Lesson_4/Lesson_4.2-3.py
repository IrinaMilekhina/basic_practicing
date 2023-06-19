'''
Задание 2.
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP,
...) и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от
того, в каком регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
Задание 3.
Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся в ответе
сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
использовать в ответе функции?
'''
from requests import get, utils

from datetime import datetime


def currency_rates(valuta: str, date_flag=False):
    """
     Gets exchange rate of the requested currency(ies)

    :param valuta: international character code
    :param date_flag: True if date data is needed
    :return: list [date (type date), exchange rate of the requested currency to the RUB (type float)]
    """
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings).split('Valute ID=')
    date, currency = None, None
    # ----- for task 3 -----
    if date_flag is True:
        date = datetime.strptime(content[0].split('"')[-4], '%d.%m.%Y').date()
    # ----------------------
    for el in content:
        if valuta.upper() in el:
            currency = float(el.split('Value>')[-2].strip('</').replace(',', '.'))
    return [date, currency]


if __name__ == '__main__':
    print(currency_rates('usd'))
    print(currency_rates('eUr'))
    print(currency_rates('GBP'))
    print(currency_rates('LOH'))
    print(currency_rates('GbP', True))
    print(currency_rates('PIDR', True))
