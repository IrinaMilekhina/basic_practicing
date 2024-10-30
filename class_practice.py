from typing import Optional


class Car:
    """Information about cars"""

    def init(self, color: str, brand: str, model: str, не_бита: Optional[bool] = True, не_крашена: Optional[
        bool] = True):
        self.color = color
        self.brand = brand
        self.model = model
        self.не_бита = не_бита
        self.не_крашена = не_крашена

    def accident(self):
        self.не_бита = False
        self.не_крашена = False

    def characteristics(self):
        print(f'Color: {self.color}, Brand: {self.brand}, Model: {self.model}\n \
        Additional: не бита - {self.не_бита}, не крашена - {self.не_крашена}')


###
car_1 = Car('blue', 'Volvo', 'Cx3')
car_2 = Car('red', 'BMW', 'MF14')

car_1.characteristics()
car_2.characteristics()

car_2.accident()

car_1.characteristics()
car_2.characteristics()
