"""
Input: date 1990.08.31
Result: 31 august 1990
"""
import re

MONTHS = {
    '01': 'january',
    '02': 'february',
    '03': 'march',
    '04': 'april',
    '05': 'may',
    '06': 'june',
    '07': 'july',
    '08': 'august',
    '09': 'september',
    '10': 'october',
    '11': 'november',
    '12': 'december'
}

pattern = re.compile(r'^\d{4}\.[0-12].[0-31]$')
user_input = str(input('type required date in format YYYY.MM.DD:'))
if re.fullmatch(pattern, user_input) is None:
    print('Oopsie, wrong format')
else:
    year = user_input.split('.')[0]
    month = MONTHS[user_input.split('.')[1]]
    day = user_input.split('.')[2]
    print(f'{day} {month} {year}')
