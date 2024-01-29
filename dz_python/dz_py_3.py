# Homework_3

kol = int(input('Введите количество символов(цифрами): '))
tip = input('Введите тип символов: ')
line = int(input('Введите ориентацию линии(0 ил 1): '))
# 0 - горизонтальная
# 1 - вертикальная
if line == 0:
    print(kol * tip)
elif line == 1:
    print(kol * (tip + '\n'))
else:
    print('0 или 1')
