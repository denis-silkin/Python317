# name = "admin"
# print("Hello", name)
# # import keyword
# # keyword.kwlist
# age = 20
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a, id(a))
# print(b, id(b))

# a = 5; b = 3
# print(a); print(b)
#
# PI = 3.14
# print(PI)
# PI = 2  # нарушение соглашения
# print(PI)

# a = 5
# b = '7'
# print(a + int(b))

# a = 1
# b = 2
# print('a:', a)
# print('b:', b)
# a, b = b, a
# # c = a
# # a = b
# # b = c
# print('a:', a)
# print('b:', b)

# print('строка \n'
#       'символов')
# print('     строка символов')
# print('\'program\'\rC:\\folder\\file.txt')

# s1 = 'Hello'
# s2 = 'Python'
# s3 = s1 + ' ' + s2 + '___'
# print(s3)
# print(s3 * 3)

# print(4454545464564456464879451)
# print(4.454545464564456464879451324)

# print(6 + 2)
# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(6 ** 2)
# print(6 % 2)
# print(6 // 2)

# a, b, c = 5, 7, 3
# print('Сумма:', a + b + c)
# print('Произведение:', a * b * c)
# print('Среднее арифметическое:', (a + b + c) / 3)

# numbers = 6 + 4 * 5 ** 2 + 7
# print(numbers)
#
# numbers = (6 + 4) * (5 ** 2 + 7)
# print(numbers)

# num = 10
# num += 5
# print(num)
#
# num -= 3
# print(num)
#
# num *= 4
# print(num)


# Занятие 2


# num = 4321
# a = num % 10
# b = (num // 10) % 10
# c = (num // 100) % 10
# d = (num // 1000) % 10
# print('num: ', a, b, c, d, sep='')

# num = 9753
# res = num % 10 * 1000
# num //= 10
# res += num % 10 * 100
# num //= 10
# res += num % 10 * 10
# num //= 10
# res += num % 10
# print(res)

# print(int(3.8))
# a = round(3.84568, 3)
# print(round(a))
# print(a, type(a))

# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# name = 'Виктор'
# age = 20
# print('Меня зовут', name, '. Мне', age, 'лет.')
# print('Меня зовут ' + name + '. Мне ' + str(age) + ' лет.')
# print('Меня зовут', name, '. Мне', age, 'лет.', sep='', end=' ')
# print('Hello')

# name = input('Введите имя: ')
# city = input('Введите город: ')
# print(name, city)

# num = int(input('Введите число: '))
# power = int(input("Введите степень: "))
# res = num ** power
# print('Число', num, 'в степени', power, 'равно:', res)

# a = int(input('Введите первое число:'))
# b = int(input('Введите второе число:'))
# c = int(input('Введите третье число:'))
# d = int(input('Введите четвертое число:'))
# num1 = a + b
# num2 = c + d
# res = round(num1 / num2, 2)
# print(res)

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)
# print(type(b1))

# print(bool('python'))
# print(bool(''))  # False - пустые кавычки. Или 0

# print(7 == 7)
# print('7' == 7)
# print(2 + 5 == 7)
# print(8 > 5)
# print(8 < 5)
# print(8 <= 5)
# print(8 <= 5)
# print('Hello' < 'hello')

# print(2 < 4 < 9)
# print(2 < 4 > 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(3 * 3 <= 7 >= 2)

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 or 1 + 3 < 4)
# print(not 9 - 5)
# print(not 9 - 9)

# cnt = 15
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input('Ведите свой возраст: '))
# if age >= 18:
#     print('Доступ на сайт разрешен')
# else:
#     print('Доступ запрещен')

# a = 35
# b = 25
# if a > b:
#     print('a > b')
# elif b > a:
#     print('a < b')
# else:
#     print('b == a')

# a = input('Введите первую сторону: ')
# b = input('Введите вторую сторону: ')
# c = input('Введите третью сторону: ')
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or b == c or c == b:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <= 5:
#     print('Рабочий день - ', end='')
#     if day == 1:
#         print('Понедельник')
#     if day == 2:
#         print('Вторник')
#     if day == 3:
#         print('Среда')
#     if day == 4:
#         print('Четверг')
#     if day == 5:
#         print('Пятница')
# elif day == 6 or day == 7:
#     print("Выходной день - ", end='')
#     if day == 3:
#         print('Суббота')
#     if day == 3:
#         print('Воскресенье')
# else:
#     print('Такого днф недели не существует!')

# num = int(input('Введите количество ворон от 0 до 9: '))
# if 0 <= num <= 9:
#     print('На ветке', end=' ')
#     if num == 1:
#         print(num, 'Ворона')
#     elif num == 2 or num == 3 or num == 4:
#         print(num, "Вороны")
#     else:
#         print(num, 'Ворон')
# else:
#     print('от 0 до 9!')


# m = int(input('Введите номер месяца: '))
# if m == 1 or m == 2 or m == 12:
#     print('Зима')
# elif 3 <= m <= 5:
#     print('Весна')
# elif 6 <= m <= 8:
#     print('Лето')
# elif 9 <= m <= 11:
#     print('Осень')
#
# else:
#     print('Ошибка ввода данных')

# password = 'admin1'
#
# match password:
#     case 'admin':
#         print('Администратор')
#     case 'user':
#         print('Пользователь')
#     case _:
#         print('Пароль неверен')

# day = 'Понедельник'
# time = 15
#
# match day:
#     case 'Понедельник' | 'Вторник' | 'Среда' | 'Четверг'  'Пятница' if 9 <= time <= 16:
#         print('Рабочий день')
#     case 'Суббота' | 'Воскресенье' if 9 <= time <= 12:
#         print('Рабочий день')
#     case 'Суббота' | 'Воскресенье':
#         print('Выходной день')
#     case _:
#         print('Такого дня недели не существует или не рабочее время')

# a, b = 30, 20
#
# minim = a if a < b else b
# print(minim)

# a, b = 10, 20
#
# print('a == b' if a == b else 'a > b' if a > b else 'b > a')

# a, b = int(input('Введите первое число')), int(input('Введите второе число'))
# print('на ноль делить нельзя' if b == 0 else a / b)

# try:
#     n = int(input('Введите целое число: '))
#     print(n * 2)
# except ValueError:
#     print('Что-то пошло не так')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except ValueError:
#     print('нельзя вводить строки')
# except ZeroDivisionError:
#     print('нельзя делить на ноль')

# try:
#     n = int(input('Введите делимое: '))
#     m = int(input('Введите делитель: '))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print('нельзя вводить строки и нельзя делить на ноль')
# else:
#     print('Все нормально. Вы ввели числа', n, 'и', m)
# finally:
#     print('конец программы')


# n = input('Введите первое число: ')
# m = input('Введите второе число: ')
# try:
#     n = int(n)
#     m = int(m)
#     print(n + m)
# except ValueError:
#     print(n + m)

# n = input('Введите первое число: ')
# m = input('Введите второе число: ')
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

# Цикл

# i = 0
# while i < 5:
#     print('i =', i)
#     i += 1

# i = 10
# while i > 0:
#     print('i =', i)
#     i -= 2


# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print('i =', i)
#     i += 1

# i = int(input('Укажите кол-во символов: '))
# print('/' * i)
# print('+-' * int(i / 2))

# n = int(input('Укажите кол-во символов: '))
# i = 0
# while i < n:
#     if i % 2 == 0:
#         print('+', end='')
#     else:
#         print('-', end='')
#     i += 1

# n = int(input('Укажите кол-во символов: '))
# i = 0
# while n > 0:
#     print('*', end='')
#     n -= 1

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
# summ = 0
# if a > b:
#     a, b = b, a
# while a <= b:
#     if a % 2:
#         summ += a
#     a += 1
# print('Сумма целых нечетных чисел:', summ)


# n = input('Введите целое число: ')
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое!')
#         n = input('Введите целое число: ')
# if n % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=' ')
#     if i == 5:
#         break
#     i += 1
# print('\nЦикл завершен')

# i = 0
# while True:
#     print(i)
#     if i == 5:
#         break
#     i += 1

# while True:
#     n = int(input('Введите положительное число: '))
#     if n < 0:
#         break

# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print('Внешний цикл: i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл: j =', j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if i % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:  # строка
#     j = 0
#     while j < 16:  # столбец
#         if j % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(' ', end='')
#         j += 1
#     print('*')
#     i += 1

# j = 0
# while j < 5:
#     print(' ' * j, '*')
#     j += 1

# for i in 'Hello':
#     print(i)

# for i in 'Hello':
#     print(i)

# for color in 'red', 'yellow', 'green', 1, 20, 0.3:
#     print(color)

# print(range(5))

# range(start, stop, step)

# for i in range(0, 9):
#     print(i, end=' ')
#
# print()
#
# i = 0
# while i < 9:
#     print(i, end=' ')
#     i += 1

# a = int(input('Введите целое число: '))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=' ')


# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=' ')

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print('+++')
#     for j in range(2):
#         print('-----')

# w = int(input('Введите длину прямоугольника: '))
# h = int(input('Введите ширину прямоугольника: '))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h-1 or j == 0 or j == w - 1:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()

# print([i * 2 for i in "Python"])
# print([i for i in range(30) if i % 2 == 0])


#  Списки(list)
# num = [9, 3, 8, 4, 1, 'Hello', 2.3, True]
# print(num)
# print(type(num))
# print(num[0])
# print(num[2])
# print(num[-1])
# print(num[7])
# num[1] = 100
# num[2] += 50
# print(num[len(num) - 1])
# print(num [- 1])


# num = []
# print(num)
# print(type(num))

# nums = list(range(20, -5, -2))
# print(nums)
# print(type(nums))

# nums = list('Hello')
# num = nums * 2
# print(num + [1, 2, 3])

# nums = list(range(2, 100, 10))
# print(nums)
#
# for i in range(len(nums)):
#     print(nums[i])

#  генератор списков
# [выражение for переменная in последовательность]

# a = [0 for i in range(5)]
# print(a)
# b = [i ** 2 for i in range(1, 6)]
# print(b)
# c = [c * 3 for c in 'list']
# print(c)

# a = [0] * int(input('Введите количество элементов списка: '))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input('->'))
# print(a)

# a = [input('->') for i in range(int(input('n = ')))]
# print(a)

# print(range(5))
# print(list(range(5)))
# s = [2, 9, 8, 7, 4]
# for i in range(len(s)):
#     print(i, '->', s[i])

# a = [int(input('->')) for i in range(int(input('n = ')))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print(s)

# for i in a:
#     if i < 0:
#         s += i
# print(s)

# lst = list(range(10, 100, 10))
# print(lst)
# for i in range(len(lst)):
#     print(lst[i], end=' ')
# print()
# for i in lst:
#     print(i, end=' ')

# colors = ['red', 'blue', 'green']
# for i in range(len(colors)):
#     print(colors[i], end=' ')
# print()
# for i in colors:
#     print(i, end=' ')

# n = list(range(21, 41))
# print(n)
# count = s = 0
# # for i in range(len(n)):
# #     if n[i] % 2 == 0:
# #         count += 1
# #     else:
# #         s += n[i]
# for i in n:
#     if i % 2 == 0:
#         count += 1
#     else:
#         s += i
# print('Количество  четных элементов списка:', count)
# print('Сумма  нечетных элементов списка:', s)

# n = list(range(21, 41))
# print(n)
# i = 0
# print(n[i])
# print(n[i - 1])

# a = [int(input('-> ')) for i in range(int(input('n = ')))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=' ')

# a = [7, 9, 3, 1, 2]
# print(a)
# print(id(a[0]))
# print(id(a[1]))
# a[0], a[1] = a[1], a[0]
# print(a)
# print(id(a[0]))
# print(id(a[1]))

# Срезы
# s = [5, 9, 3, 7, 1, 8]
# b = s[0:4]
# print(b)

# s = 'Hello'
# print(s[0])

# s = list(range(1, 8))
# print(s)
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[4:1:-1])
# print(s[2:5])

# s = [1, 2, 3, 4, 5, 6, 7]
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[2:5] = []
# print(s)
# del s[1:3]
# print(s)

# s = [9, 3, 7, 8, 4, 6, 5]
# print(s)
# # s += [12]
# s.append(12)
# print(s)
# s.extend([1, 2, 3])
# print(s)
# s.extend("add")
# print(s)
# s.insert(3, "Hello")
# print(s)
# s.insert(20, 90)
# print(s)

# s = []
# n = int(input('Количество элементов списка: '))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []

# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)
# for element in a:
#     if element not in c and element in b:
#         c.append(element)
# print(c)


# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []

# if len(b) > len(b):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)
# if len(b) > len(b):
#     a, b = b, a
#
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])
# print(c)

# a = [1, 3, 2, 3, 4, 3, 5]
# print(a)
# # n = 7
# # if n in a:
# #     a.remove(n)  # удаление по значению, выбрасывают исключения ValueError - если элемента не существует
# print(a)
# last = a.pop()  # удаляет последний элемент из списка и возвращает удаленный элемент
# print(last)
# print(a)
# second = a.pop(1)  # удаляет элемент по заданному индексу (IndexError)
# print(second)
# print(a)
# a.clear()  # очищает список от элементов
# print(a)

# a = [int(input('Введите число: ')) for i in range(int(input('Введите количество чисел последовательности: ')))]
# b = int(input('Введите индекс: '))
# print(a.pop(b))
# print(a)

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# num = a.count(5)
# print(num)
# ind = a.index(2)  # возвращает индекс заданного значения
# print(ind)
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)
# a.sort(reverse=True)  # сортировка списка
# print(a)

# s = ['Виталий', 'Сергей', 'Александр', 'Анна']
# print(s)
# s.sort(key=len)
# print(s)

# a = [1, 5, 3, 2, 3, 4, 3, 5]
# print(a)
# # a.sort()
# n = sorted(a)
# print('n =', n)
# print(a)

# a = [1, 2, 3]
# b = a.copy()  # возвращает копию списка
# print('a =', a, id(a))
# print('b =', b, id(b))
# a.append(20)
# b.append(120)
# print('a =', a, id(a))
# print('b =', b, id(b))

# Генерация случайных данных


# print(random.random())  # от 0 до 1 (не включительно)
# print(random.randint(0, 9))  # от 0 до 9 (включительно)
# print(random.randrange(2, 9, 2))  # randrange(start, stop, step) randrange(2, 9)
# print(round(random.uniform(10.5, 25.5), 2))
# city_list = ['Москва', "Новосибирск", "Воронеж", "Сочи", "Екатеринбург"]
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
#
# s = [20, 30, 40, 50, 60, 70, 80, 90]
# print(random.choice(s))
# print(random.choices(s, k=3))
# random.shuffle(s)
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# mas = ['a', 'b', 'c']
# print(mas)
# print(len(mas))
# print(min(mas))
# print(max(mas))
# print(sum(mas))
# s = 0
# for i in mas:
#     s += i
# print(s)

# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# a = max(mas)
# print('Max:', a)
# mas.remove(a)
# mas.insert(0, a)
# print(mas)

# mas = [random.randint(-20, 20) for i in range(10)]
# print(mas)
# mas.sort(reverse=True)
# print(mas)

# mas = [random.randint(1, 20) for i in range(10)]
# print(mas)
# a = min(mas)
# print('Min', a)
# print('Index min: ', a)
# ind = mas.index(a)
# print(ind)
# print(mas[ind:])

# lst = [5, 6, 8, 9, 7]
# # # if len(lst) == 0:
# # if not lst:
# #     print('Список пустой')
# print(5 not in lst)


# n1 = int(input('Введите размер первого списка: '))
# n2 = int(input('Введите размер второго списка: '))
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print('Первый список: ', a)
# print('Второй список: ', b)
# c = a + b
# print(c)
#
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if i not in c:
#         c.append(b[i])
# print('Элементы обоих списков без повторений:', c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print('Элементы общие для двух списков:', c)
#
# c = [min(a), min(b), max(a), max(b)]
# print('Минимальное и максимальное значения из двух списков:', c)


# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end='\t')
#     print()
# print()
#
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end='\t')
#     print()

# w, h = 5, 3
# # matrix = [[0 for x in range(w)]for y in range(h)]
# # print(matrix)
# matrix = []
# for y in range(h):
#     new_row = []
#     for x in range(w):
#         new_row.append(0)
#     matrix.append(new_row)
# print(matrix)
# for row in matrix:
# # print(row)
#     for x in row:
#         print(x, end='\t')
#     print()

# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, '+', y, '=', x + y)

# import random
#
# w, h = 3, 5
# matrix = [[random.randint(-20, 10) for x in range(w)] for y in range(h)]
# print(matrix)
# count = 0
# for row in matrix:
#     # print(row)
#     for x in row:
#         print(x, end='\t\t')
#         if x < 0:
#             count += 1
#     print()
# print('Количество отрицательных элементов: ', count)

# Modules

# import math
#
# print(math.sqrt(4))
# print(math.pi)
# print(math.ceil(3.2))
# print(math.floor(3.8))

# import math as m
#
# print(m.ceil(3.2))
# print(m.floor(3.8))


# from math import ceil, floor
#
# print(ceil(3.2))
# print(floor(3.8))

# from math import *

# print(ceil(3.2))
# print(floor(3.8))


from math import pi

# radius = int(input('Введите радиус окружности: '))
# print('Длина окружности:', round(2 * pi * radius))

# from math import sqrt
# a = int(input('Катет 1: '))
# b = int(input('Катет 2: '))
# print('Длина гипотенузы:', sqrt(a**2 + b**2))

import time
import locale

# locale.setlocale(locale.LC_ALL, 'bel')  # ukr
#
# seconds = time.time()
# print(seconds)
# print(time.ctime())
# print(time.ctime(5512545))
# res = time.localtime()
# print(res)
# print(res.tm_mday, '.', res.tm_mon, '.', res.tm_year, sep='')
#
# print(time.strftime('Сегодня: %B %d, %Y'))
# print(time.strftime('%d/%m/%Y, %H:%M:%S'))

# pause = 5
# print('Программа запущена')
# time.sleep(pause)
# print(pause, 'секунд')

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)
# print()


# def hello(name):
#     print('Hello', name)
#
#
# hello('Irina')
# hello('Ivan')


# def get_sum(a, b):
#     print('Hello')
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# n = 6
# m = 3
# get_sum(n, m)
# get_sum('abc', 'def')


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# m = maximum(9, 6)
# print(m)


# def maxi(a, b):
#     if a > b:
#         return a - b
#     else:
#         return a + b
#
#
# m = maxi(int(input('Введите число: ')), int(input('Введите число: ')))
# print("Ответ:", m)


# def cube(a):
#     return a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))


# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))


# def func(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(func(10, 5))
# print(func(5, 10))
# a = 5
# b = 10
# if func(a, b):
#     print('Первое число больше второго')
# else:
#     print('Второе число больше первого')


# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#     for ch in password:
#         if 'A' <= ch <= 'Z':
#             has_upper = True
#         if 'a' <= ch <= 'z':
#             has_lower = True
#         if '0' <= ch <= '9':
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input('Введите пароль: ')
# if check_password(p):
#     print('Это надежный пароль')
# else:
#     print('Это ненадежный пароль')


# def get_sum(a, b, c=0, d=1):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))


# def set_param(c=20, s='-'):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(s='#')


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         if not even and cur_digit % 2 != 0:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print('Сумма четных цифр:')
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
#
# print('Сумма нечетных цифр:')
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age, nm):
#     print('Name', name, '\nAge:', age)
#
#
# display_info('Ira', 23)
# display_info(age=23, name='Ira')
# display_info(nm='Igor', age=23, name='Ira')


# a = 'Hello'
# b = 'Hello'
# print(a == b)  # True
# print(a is b)  # True
# print(a, id(a))
# print(b, id(b))
# lst1 = [1, 2, 3]
# lst2 = [1, 2, 3]
# print(lst1 == lst2)  # True
# print(lst1 is lst2)  # False
# print(lst1, id(lst1))
# print(lst2, id(lst2))

# Изменяемые объекты - list
# Неизменяемые объекты - int, float, bool, str, tuple

# lst1 = [1, 2, 3]
# print(lst1, id(lst1))
# lst1.append(4)
# print(lst1, id(lst1))

# Кортежи (tuple)

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = 'red', 'blue', 'green'
# print(a)
# print(type(a))

# a = (5,)
# print(a)
# print(type(a))

# a = tuple('Hello')
# a = tuple([1, 2, 3, 4])
# print(a)
# print(type(a))
# print(a[0])
# print(a[1:3])
# a[2] = 12
# print(a)


from random import randint


# s = tuple(i for i in range(5))
# s = tuple(input('-> ')for i in range(5))
# s = tuple(randint(20, 40) for i in range(5))
# print(s)


# res = tuple(2 ** i for i in range(1, 13))
# print(res)

# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# print(t3 * 2)
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 3))
# sh = 'a'
# try:
#     print(t3.index(sh))
# except ValueError:
#     print("Такого символа в кортеже не существует")

# for i in t3:
#     print(i, end=' ')


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return tpl[first:second]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))


# def kor(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = kor(0, 5)
# print(tpl1)
# tpl2 = kor(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0 =', tpl3.count(0))

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

print('Данные для добавления на GitHub')


