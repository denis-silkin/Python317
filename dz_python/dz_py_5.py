# Homework_5


a = int(input('Количество элементов списка: '))
count = []
for i in range(a):
    n = int(input('Введите число кратное 3: '))
    if n % 3 == 0:
        count.append(n)
    else:
        print(n, 'не делится на 3 без остатка.')
print(count)
