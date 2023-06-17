'''
Задание 4.
Написать свой модуль utils и перенести в него функцию currency_rates() из предыдущего
задания. Создать скрипт, в котором импортировать этот модуль и выполнить несколько вызовов
функции currency_rates(). Убедиться, что ничего лишнего не происходит.
Задание 5.
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли
'''
import sys

from utils import currency_rates as smart_af

print(smart_af('Eur', 'gbp', 'OMG', 'USD'))
# ---optionally uncomment for task 5 before running this in Terminal---
# print(smart_af(*sys.argv[1:], date=True))

# I ran this module in PyCharm Terminal with >>> python Lesson_4.4-5.py 'gbp' 'LSD' 'eur' uSd
