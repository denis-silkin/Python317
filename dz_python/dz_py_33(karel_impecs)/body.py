from bs4 import BeautifulSoup
import requests
import csv


class Tyre:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        tyres = self.html.find_all('div', class_='item_info TYPE_1')
        for ty in tyres:
            price = ty.find('span', class_='price_value').text.strip()
            tyre = ty.find('div', class_='item-title').find('span').text
            # print(f'Название: {price} => Цена: {tyre} руб.')
            self.res.append({
                'tyre': tyre,
                'price': price
            })
            # print(self.res)

    def save_csv(self):
        with open(self.path, 'w') as f:
            writer = csv.writer(f, delimiter=';', lineterminator='\r')
            for i in self.res:
                f.write(f'Шина: {i["tyre"]} => Цена: {i["price"]}\n')

    def run(self):
        self.get_html()
        self.parsing()
        self.save_csv()
