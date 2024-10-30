"""
Использовать функцию из 3 задания на вход.
Заменить все числа, меньшие последнего элемента массива, на первый элемент.
"""
from func import math_wizard

# list generation
initial_list = math_wizard(10, 0, 10)
print(initial_list)
# list transformation
for element in initial_list:
    if element < initial_list[-1]:
        initial_list[initial_list.index(element)] = initial_list[-1]
print(initial_list)