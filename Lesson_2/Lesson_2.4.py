'''
Дан список, содержащий искажённые данные с должностями и именами сотрудников:
['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
'токарь высшего разряда нИКОЛАй', 'директор аэлита']
Известно, что имя сотрудника всегда в конце строки. Сформировать из этих имён и вывести на
экран фразы вида: 'Привет, Игорь!' Подумать, как получить имена сотрудников из элементов
списка, как привести их к корректному виду. Можно ли при этом не создавать новый список?
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
