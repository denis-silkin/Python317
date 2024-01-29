# Homework_6

import math


def triangle():
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    c = int(input("Введите число c: "))
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print('Площадь фигуры:', s)


def rectangle():
    a = int(input("Введите число a: "))
    b = int(input("Введите число b: "))
    s = a * b
    print('Площадь фигуры:', s)


def circle():
    a = int(input("Введите число a: "))
    s = math.pi * (a ** 2)
    print('Площадь фигуры:', s)


fig = int(input('Выбор фигуры: '))

if fig == 1:
    triangle()
elif fig == 2:
    rectangle()
elif fig == 3:
    circle()
else:
    print('Введите число от 1 до 3')
