from body import Tyre


def main():
    pars = Tyre(
        'https://koleso.ru/catalog/filter/tyres/?tyres_width=185&tyres_profile=75&tyres_diameter=16&tyres_developer='
        '&tyres_season%5B%5D=winter&tyres_thorn=1',
        'tyre.csv')
    pars.run()


if __name__ == '__main__':
    main()
