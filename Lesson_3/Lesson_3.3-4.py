'''
Задание 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имён, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
 thesaurus("Иван", "Мария", "Петр", "Илья")
{
"И": ["Иван", "Илья"],
"М": ["Мария"],
"П": ["Петр"]
}

Задание 4. Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате «Имя Фамилия» и
возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари, реализованные по схеме
предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы. Например:
 thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр
Алексеев", "Илья Иванов", "Анна Савельева")
{
"А": {
"П": ["Петр Алексеев"]
},
"И": {
"И": ["Илья Иванов"]
},
"С": {
"И": ["Иван Сергеев", "Инна Серова"],
"А": ["Анна Савельева"]
}
}
'''
# task 3
print('FIRST PART'.center(100, '-'), '\n')


def thesaurus(*names):
    """Returns dictionary with first name letters as keys and lists of names as values"""
    result = {}
    for name in names:
        key = name[0].capitalize()
        if key not in result:
            result[key] = []
        result[key].append(name)
    return result


print(thesaurus('Bethany', 'Ian', 'Theodor', 'Dora', 'Bob', 'Daniel'))

# task 4
print('\n', 'SECOND PART'.center(100, '-'))


def thesaurus_adv(*personal_data):
    """Returns dictionary with first surname letter as a key and a (dictionary with first name letter as a keys and
    list of names and surnames as a value) as a value"""
    result = {}
    for name_surname in personal_data:
        name, surname = name_surname.split(' ')
        surname_key = surname[0].capitalize()
        name_key = name[0].capitalize()
        if surname_key not in result:
            result[surname_key] = {}
        name_based = result[surname_key]
        if name_key not in name_based:
            name_based[name_key] = []
        name_based[name_key].append(name_surname)
    return result


print(thesaurus_adv('Bethany Sommers', 'Ian Valensis', 'Theodor Samsonite', 'Dora Explorer', 'Bob Sackland',
                    'Daniel Fufelshmertz'))
