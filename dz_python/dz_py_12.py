# Homework_12


lst = {}

num = int(input("Введите количество студентов: "))
n = 0


for i in range(num):
    name = input(str(i + 1) + ' -й студент: ')
    bal = int(input('Балл: '))
    lst[name] = bal
    n += bal

sr = n / num
print('Средний балл: ', round(sr))
for i in lst:
    if lst[i] > sr:
        print('Студенты с баллом выше среднего: ', i)





