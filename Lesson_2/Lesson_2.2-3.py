'''
Задание 2. Дан список:
['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
Необходимо его обработать — обособить каждое целое число (вещественные не трогаем) кавычками (добавить кавычку до и
кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных разрядов:
['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']
Сформировать из обработанного списка строку: в "05" часов "17" минут температура воздуха была "+05" градусов
Подумать, какое условие записать, чтобы выявить числа среди элементов списка? Как модифицировать это условие для
чисел со знаком?

Задание 3. Решить задачу 2 не создавая новый список (как говорят, in place)
'''
phrase_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

# creating a new list
new_phrase_list = []

for i, v in enumerate(phrase_list):
    if v.isnumeric():
        new_phrase_list.extend(['"', f'{int(phrase_list[i]):02d}', '"'])
    elif v.startswith('+' or '-'):
        internal_list = list(v)
        number_sign = internal_list.pop(0)
        ''.join(internal_list)
        new_phrase_list.extend(['"', number_sign + f'{int(phrase_list[i]):02d}', '"'])
    else:
        new_phrase_list.append(phrase_list[i])

print(
    ' '.join(new_phrase_list[:2]) + new_phrase_list[2] + ' '.join(new_phrase_list[3:6]) + new_phrase_list[6] + ' '.join(
        new_phrase_list[7:13]) + new_phrase_list[13] + ' '.join(new_phrase_list[14:]))

# without creating a new list
for i, v in enumerate(phrase_list):
    if v.isnumeric():
        phrase_list[i] = f'{int(phrase_list[i]):02d}'
        phrase_list.insert(i + 1, '"')
    if v.startswith('+' or '-'):
        internal_list = list(v)
        number_sign = internal_list.pop(0)
        internal_number = ''.join(internal_list)
        phrase_list[i] = number_sign + f'{int(internal_number):02d}'
        phrase_list.insert(i + 1, '"')

phrase_list.reverse()

for i, v in enumerate(phrase_list):
    if v.isnumeric() or v.startswith('+' or '-'):
        phrase_list.insert(i + 1, '"')

phrase_list.reverse()
print(
    ' '.join(phrase_list[:2]) + phrase_list[2] + ' '.join(phrase_list[3:6]) + phrase_list[6] + ' '.join(
        phrase_list[7:13]) + phrase_list[13] + ' '.join(phrase_list[14:]))