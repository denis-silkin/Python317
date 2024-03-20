#  Homework_21


class Car:

    def __init__(self, model, year_of_release, manufacturer, engine_power, color, price):
        self.model = model
        self.year_of_release = year_of_release
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def print_info(self):
        print(' Данные автомобиля '.center(40, '*'))
        print(
            f'Название модели: {self.model}\nГод выпуска: {self.year_of_release}\nПроизводитель: {self.manufacturer}\n'
            f'Мощность двигателя: {self.engine_power}\nЦвет: {self.color}\nЦена: {self.price}')
        print('=' * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year_of_release(self, year_of_release):
        self.year_of_release = year_of_release

    def get_year_of_release(self):
        return self.year_of_release

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def get_engine_power(self):
        return self.engine_power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


c1 = Car('X7 M50i', '2021', 'BMW', '530 л.с.', 'white', '10790000')
c1.set_model('Kalina')
print(c1.get_model())
c1.set_engine_power('128 л.с.')
print(c1.get_engine_power())
c1.set_color('red')
print(c1.get_color())
c1.print_info()
