from requests import get, utils


def currency_rates(*currency, date=False):
    """
     Gets exchange rate of the requested currency(ies)

    :param currency: international character code
    :param date: True if date data is needed
    :return: string(s) with information about the date and/or exchange rate of the requested currency to the
    ruble (RUB)
    """
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings).split('><')[4:]
    all_currencies = {}
    index_delta = 3    # разница в индексах между названием валюты и курсом
    for i, el in enumerate(content):
        if el.find('CharCode') == 0:
            code_name = el.strip('CharCode').strip('>').strip('</')
            value_i = i + index_delta
            all_currencies[code_name] = float(content[value_i].strip('Value').strip('>').strip('</').replace(',', '.'))
    requested_data = []
    if date is True:
        date_in_response = ' '.join(response.headers.get('Date').split(' ')[:4])  # dropping out time and time zone info
        requested_data.append(f'Request date: {date_in_response}')
    for character_code in currency:
        value = all_currencies.get(character_code.upper())
        if value is None:
            requested_data.append(f'{character_code.upper()}: None')
        else:
            requested_data.append(f'{character_code.upper()}: {value} RUB')
    return ';\n'.join(requested_data)


if __name__ == '__main__':
    print(currency_rates('usd', 'eUr', 'GBP', 'LOH'))
