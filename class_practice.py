"""
Написать класс для описания машины
У каждого экземпляра класса будут атрибуты "цвет", "марка", "модель" - строки, "не бита", "не крашена" - булевы значения
(по умолчанию true)
у класса будет метод "авария", который будет менять булевы значения на false

создать 2 экземпляра класса, напечатать их характеристики
у одной машины вызвать аварию и опять напечатать характеристики
"""

from typing import Optional


class Car:
    """Information about cars"""

    def __init__(self, color: str, brand: str, model: str, no_accidents: Optional[bool] = True,
                 no_repainting: Optional[bool] = True):
        self.color = color
        self.brand = brand
        self.model = model
        self.no_accidents = no_accidents
        self.no_repainting = no_repainting

    def accident(self):
        self.no_accidents = False
        self.no_repainting = False

    def characteristics(self):
        print(f'Color: {self.color}, Brand: {self.brand}, Model: {self.model}\n\
        Additional: no accidents - {self.no_accidents}, no repainting - {self.no_repainting}\n')


###
# car_1 = Car(color='blue', brand='Volvo', model='Cx3')
car_1 = Car('blue', 'Volvo', 'Cx3')
car_2 = Car('red', 'BMW', 'MF14')

car_1.characteristics()
car_2.characteristics()

car_2.accident()

car_1.characteristics()
car_2.characteristics()
