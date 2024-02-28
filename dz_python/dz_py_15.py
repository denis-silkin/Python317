# Homework_15


def decor(fn):
    def wrap(*args):
        zpt = ''
        for i in args:
            zpt += str(i) + ', '
        print('Среднее арифметическое:', zpt[:-2], '=', fn(*args) / len(args))

    return wrap


@decor
def lst(*args):
    print('Сумма чисел:', ', '.join(map(str, args)), '=', sum(args))
    return sum(args)


lst(2, 3, 3, 4)
