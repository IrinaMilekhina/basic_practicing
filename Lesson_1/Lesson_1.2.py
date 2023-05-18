'''
Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
a. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
b. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
списка, сумма цифр которых делится нацело на 7.
c. * Решить задачу под пунктом b, не создавая новый список.
Ограничения: использовать только арифметические операции!
'''

list_till = 1000    # до какого числа составлять список
raising_power = 3    # степень возведения чисел в списке
summ_divider = 7    # число, на которое должна нацело делиться сумма цифр
added_amount = 17    # число, которое надо добавить к эелемнтам списка
number = 0
odd_list = []
iterated_list = []
idx = 0
internal_summ = 0
desired_summ = 0

# forming list of powered odd numbers in range list_till
for number in range(list_till):
    tmp = number % 2 > 0
    if tmp is True:
        odd_list.append(number ** raising_power)
    number += 1

print("Desired list of powered odd numbers: " + str(odd_list))

# finding desired summ in point A
for idx in range(len(odd_list)):
    number = odd_list[idx]
    while number > 0:
        internal_summ += number % 10
        number //= 10
    if internal_summ % summ_divider == 0:
        desired_summ += odd_list[idx]

print("Desired summ: " + str(desired_summ) + "\n")

# iterating the list and again finding desired summ
internal_summ = 0
desired_summ = 0
for idx in range(len(odd_list)):
    iterated_list.append(odd_list[idx] + added_amount)
    number = iterated_list[idx]
    while number > 0:
        internal_summ += number % 10
        number //= 10
    if internal_summ % summ_divider == 0:
        desired_summ += iterated_list[idx]

print("New list after iteration: " + str(iterated_list))
print("Desired summ after list iteration: " + str(desired_summ) + "\n")

# iterating the list without creating a new one and again finding desired summ
internal_summ = 0
desired_summ = 0
for idx in range(len(odd_list)):
    odd_list[idx] += added_amount
    number = odd_list[idx]
    while number > 0:
        internal_summ += number % 10
        number //= 10
    if internal_summ % summ_divider == 0:
        desired_summ += odd_list[idx]

print("List after iteration: " + str(odd_list))
print("Desired summ after list iteration: " + str(desired_summ))
