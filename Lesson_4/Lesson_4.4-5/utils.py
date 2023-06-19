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
    print(currency_rates('GbP', True))
    print(currency_rates('PIDR', True))
