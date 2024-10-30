"""
Написать функцию, которая будет возвращать список случайных чисел.
Параметрами можно передать длину массива, минимальное и максимальное значения.
Добавить в блок if __name__ == "main" тесты
"""
import random as r


def math_wizard(length: int = 10, minimum: int = 0, maximum: int = 1000):
    """
    Returns a list of random numbers
    :param length: number of elements
    :param minimum: minimal number
    :param maximum: maximal number
    :return:
    """
    magic_spell = [r.randrange(minimum, maximum) for i in range(length)]
    return magic_spell


if __name__ == "main":
    print(math_wizard())
    print(math_wizard(2, 4, 6))
    print(math_wizard(22, -1, 80))
