'''
Задание 1. Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)
next(odd_to_15)
1
next(odd_to_15)
3
...
next(odd_to_15)
15
next(odd_to_15)
...StopIteration...
Задание 2. Решить задачу генерации нечётных чисел от 1 до n (включительно), не используя ключевое слово yield
'''
# task 1
print('FIRST PART'.center(100, '-'), '\n')


def odd_nums(till):
    for number in range(1, till + 1, 2):
        yield number


odd_to_15 = odd_nums(15)
for test in list(odd_nums(15)):
    print(next(odd_to_15))
# print(next(odd_to_15))    # returns Stop iteration error

# task 2
print('\n', 'SECOND PART'.center(100, '-'))


def odd_nums_no_yield(till):
    return (number for number in range(1, till + 1, 2))


odd_to_15_no_yield = odd_nums_no_yield(15)
for test in list(odd_nums_no_yield(15)):
    print(next(odd_to_15_no_yield))
# print(next(odd_to_15_no_yield))    # returns Stop iteration error
