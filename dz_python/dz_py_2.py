# Homework_2

k = int(input('Введите число от 1 до 99: '))
if 1 <= k <= 99:
    if k % 10 == 1 and k != 11:
        print(k, 'копейка')
        if k == 11:
            print(k, 'копеек')
    elif k % 10 == 2 and k != 12 or k % 10 == 3 and k != 13 or k % 10 == 4 and k != 14:
        print(k, 'копейки')
        if k == 12 or k == 13 or k == 14:
            print(k, 'копеек')
    else:
        print(k, 'копеек')
else:
    print('От 1 до 99!!!')
