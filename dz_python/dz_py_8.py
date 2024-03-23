#  Homework_8

from random import randint

tpl = tuple(randint(0, 9) for i in range(10))
print(tpl)
lst = []
for i in tpl:
    if i not in lst:
        lst.append(i)
for i in lst:
    print('Количество ', i, '=', tpl.count(i))

