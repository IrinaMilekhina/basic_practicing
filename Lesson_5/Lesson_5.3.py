'''
Есть два списка:
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
('Иван', '9А')
('Анастасия', '7В')
...
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в
списке classes меньше элементов, чем в списке tutors, необходимо вывести последние
кортежи в виде: (<tutor>, None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.    #???
'''
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Goon', 'Sauron', 'Trololo']
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']


def pair_generator(names, formations):
    for i in range(len(names)):
        if i in range(len(formations)):
            klass = formations[i]
        else:
            klass = None
        yield names[i], klass


result = pair_generator(tutors, classes)
print(type(result))
for test in tutors:
    print(next(result))
# print(next(result))    # returns Stop iteration error
