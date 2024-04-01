# Homework_23

from math import sqrt


class Figure:
    count = 0

    @staticmethod
    def get_count():
        return f'Количество подсчетов площади:', Figure.count

    @staticmethod
    def ger(a, b, c):
        Figure.count += 1
        p = (a + b + c) / 2
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return f'Площадь треугольника по формуле Герона: ({a},{b},{c})', round(s, 2)

    @staticmethod
    def footing(b, h):
        Figure.count += 1
        s = b * h / 2
        return f'Площадь треугольника через основание и высоту: ({b},{h})', s

    @staticmethod
    def sq(a):
        Figure.count += 1
        s = a * a
        return f'Площадь квадрата: ({a})', s

    @staticmethod
    def rect(a, b):
        Figure.count += 1
        s = a * b
        return f'Площадь прямоугольника: ({a}, {b})', s


f = Figure()
print(f.ger(3, 4, 5))
print(f.footing(6, 7))
print(f.sq(7))
print(f.rect(2, 6))
# print(f.rect(2, 6))
print(Figure.get_count())
