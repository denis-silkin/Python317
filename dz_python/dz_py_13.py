# Homework_13

# Вариант глобальный


def para(a, b, c):
    s = 2 * (a * b + a * c + b * c)
    print('Площадь параллелепипеда:', s)

    def rect():
        nonlocal a, b
        sr = a * b
        print('Площадь прямоугольника:', sr)
    rect()


print(para(2, 4, 6))


# Вариант локальный


# def para():
#     a = int(input('Введите значение: '))
#     b = int(input('Введите значение: '))
#     c = int(input('Введите значение: '))
#     s = 2 * (a * b + a * c + b * c)
#     print('Площадь параллелепипеда:', s)
#
#     def rect():
#         a = int(input("Введите число a: "))
#         b = int(input("Введите число b: "))
#         sr = a * b
#         print('Площадь прямоугольника:', sr)
#     return rect
#
#
# res = para()
# print(res())

