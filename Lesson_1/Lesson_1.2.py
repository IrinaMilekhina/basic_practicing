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
added_amount = 17    # число, которое надо добавить к эелементам списка
number = 0
odd_list = []
iterated_list = []
desired_summ = 0

# forming list of powered odd numbers in range list_till
for number in range(1, list_till + 1, 2):
    odd_list.append(number ** raising_power)

print("Desired list of powered odd numbers: " + str(odd_list))

# finding desired summ in point A
for i, v in enumerate(odd_list):
    internal_summ = 0
    while v > 0:
        internal_summ += v % 10
        v //= 10
    if internal_summ % summ_divider == 0:
        desired_summ += odd_list[i]

print("Desired summ: " + str(desired_summ) + "\n")

# iterating the list and again finding desired summ
desired_summ = 0
for m in odd_list:
    iterated_list.append(m + added_amount)

for i, v in enumerate(iterated_list):
    internal_summ = 0
    while v > 0:
        internal_summ += v % 10
        v //= 10
    if internal_summ % summ_divider == 0:
        desired_summ += iterated_list[i]

print("New list after iteration: " + str(iterated_list))
print("Desired summ after list iteration: " + str(desired_summ) + "\n")

# iterating the list without creating a new one and again finding desired summ
desired_summ = 0
for i in range(len(odd_list)):
    odd_list[i] += 17

for i, v in enumerate(odd_list):
    internal_summ = 0
    while v > 0:
        internal_summ += v % 10
        v //= 10
    if internal_summ % summ_divider == 0:
        desired_summ += odd_list[i]

print("List after iteration: " + str(odd_list))
print("Desired summ after list iteration: " + str(desired_summ))
