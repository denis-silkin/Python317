# Homework_19


def negative(n):
    if not n:
        return 0
    count = 0
    if n[0] < 0:
        count += 1
    return count + negative(n[1:])


lst = [-2, 3, 8, -11, -4, 6]
print(negative(lst))


# chislo = int(input('Количество чисел: '))
# negative = 0
# for i in range(chislo):
#     num = int(input(f'Введите {i+1}-е число: '))
#     if num < 0:
#         negative += 1
# print(f'Вы ввели {negative} отрицательных чисел')
