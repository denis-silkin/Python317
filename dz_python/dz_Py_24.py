# Homework_24

class Pair:
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    @property
    def st_a(self):
        return self.__a

    @st_a.setter
    def st_a(self, a):
        if a > 0:
            self__a = a
        else:
            raise ValueError('Сторона а должна быть положительным числом')

    @property
    def st_b(self):
        return self.__b

    @st_b.setter
    def st_b(self, b):
        if b > 0:
            self__b = b
        else:
            raise ValueError('Сторона b должна быть положительным числом')

    def multiplication(self):
        return self.__a * self.__b

    def sum(self):
        return self.__a + self.__b


class Triangle(Pair):
    def __init__(self, a, b):
        super().__init__(a, b)

    def hypo(self):
        return round((self.st_a ** 2 + self.st_b ** 2) ** 0.5, 2)

    def info_triangle(self):
        print(f"Прямоугольный треугольник ABC ({self.st_a}, {self.st_b}, {self.hypo()})")

    def area(self):
        s = (self.st_a + self.st_b + self.hypo()) / 2
        return round((s * (s - self.st_a) * (s - self.st_b) * (s - self.hypo())) ** 0.5, 2)


t1 = Triangle(5, 8)
print(f'Гипотенуза АВС: {t1.hypo()}')
t1.info_triangle()
print(f'Площадь АВС: {t1.area()}')
print()
print(f'Сумма: {t1.sum()}')
print(f'Произведение: {t1.multiplication()}')
t1.st_a = 9
t1.st_b = 9
print()
print(f'Гипотенуза АВС: {t1.hypo()}')
t1.st_a = 10
t1.st_b = 20
print(f'Гипотенуза АВС: {t1.hypo()}')
print(f'Сумма: {t1.sum()}')
print(f'Произведение: {t1.multiplication()}')
print(f'Площадь АВС: {t1.area()}')
