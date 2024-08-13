"""
Использовать функцию из 3 задания на вход.
Удалить в массиве все числа, которые повторяются более двух раз.
Результат записать в txt файл.
"""
from func import math_wizard

file_name = 'altered_list.txt'
# list generation
initial_list = math_wizard(10, 0, 10)
print(initial_list)
# list transformation
initial_list = list(set(initial_list))
print(initial_list)
# writing down the file
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(str(initial_list))
