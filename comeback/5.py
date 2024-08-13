"""
Использовать функцию из 3 задания на вход.
Удалить в массиве все числа, которые повторяются более двух раз.
Результат записать в txt файл.
"""
from func import math_wizard

# list generation
initial_list = math_wizard(10, 0, 10)
print(initial_list)
# list transformation
initial_list = list(set(initial_list))
print(initial_list)
