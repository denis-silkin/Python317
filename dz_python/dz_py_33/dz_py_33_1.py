# Homework_33_1


from dz_py_33 import Book


def main():
    pars = Book(
        'https://www.bookvoed.ru/?utm_medium=cpc&utm_source=yandex&utm_campaign=y_search_brand_szfo&utm_term=---'
        'autotargeting&utm_content=k50id%7C0100000047531455433_47531455433%7Ccid%7C90306904%7Cgid%7C5236578699%7Caid%7C'
        '14559639389%7Cadp%7Cno%7Cpos%7Cpremium1%7Csrc%7Csearch_none%7Cdvc%7Cdesktop%7Creg18%7Cmain&k50id=0100000047531'
        '455433_47531455433&yclid=10091717739736203263',
        'active.txt')
    pars.run()


if __name__ == '__main__':
    main()
