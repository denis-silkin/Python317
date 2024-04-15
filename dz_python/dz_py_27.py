# Homework_27

import abc
import math
import random


class Shape(abc.ABC):
    @abc.abstractmethod
    def fig_perimetr(self):
        pass

    @abc.abstractmethod
    def fig_sq(self):
        pass

    @abc.abstractmethod
    def print_info(self):
        pass

    @abc.abstractmethod
    def fig_paint(self):
        pass


# Прямоугольник
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def fig_perimetr(self):
        return f'Периметр: {2 * (self.w + self.h)}'

    def fig_sq(self):
        return f'Площадь: {self.w * self.h}'

    def fig_color(self):
        rgb = random.choice(['blue', 'red', 'green'])
        return f'Цвет: {rgb}'

    def fig_paint(self):
        for i in range(self.w):
            for y in range(self.h):
                print('*', end=' ')
            print()

    def print_info(self):
        print('=' * 3, 'Прямоугольник', '=' * 3, sep='')
        print('Длина:', self.w)
        print('Ширина:', self.h)
        print(self.fig_color())
        print(self.fig_sq())
        print(self.fig_perimetr())
        self.fig_paint()


# Квадрат
class Square(Shape):
    def __init__(self, a):
        self.a = a

    def fig_perimetr(self):
        return f'Периметр: {4 * self.a}'

    def fig_sq(self):
        return f'Площадь: {self.a * self.a}'

    def fig_color(self):
        rgb = random.choice(['blue', 'red', 'green'])
        return f'Цвет: {rgb}'

    def fig_paint(self):
        for i in range(self.a):
            for y in range(self.a):
                print('*', end=' ')
            print()

    def print_info(self):
        print('=' * 3, 'Квадрат', '=' * 3, sep='')
        print('Сторона:', self.a)
        print(self.fig_color())
        print(self.fig_sq())
        print(self.fig_perimetr())
        self.fig_paint()


# Треугольник
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def fig_perimetr(self):
        return f'Периметр: {0.5 * (self.a + self.b + self.c)}'

    def fig_sq(self):
        p = (self.a + self.b + self.c) / 2
        return f'Площадь: {round(math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)), 2)}'

    def fig_color(self):
        rgb = random.choice(['blue', 'red', 'green'])
        return f'Цвет: {rgb}'

    def fig_paint(self):
        for i in range(1, self.b + 1):
            print(' ' * (self.b - i) + '*' * (2 * i - 1))

    def print_info(self):
        print('=' * 3, 'Треугольник', '=' * 3, sep='')
        print('Сторона1:', self.a)
        print('Сторона2:', self.b)
        print('Сторона3:', self.c)
        print(self.fig_color())
        print(self.fig_sq())
        print(self.fig_perimetr())
        self.fig_paint()


s1 = Rectangle(3, 7)
s1.print_info()
print()
s2 = Square(3)
s2.print_info()
print()
s3 = Triangle(11, 6, 6)
s3.print_info()



