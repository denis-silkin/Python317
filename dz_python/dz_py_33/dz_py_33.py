# Homework_33

from bs4 import BeautifulSoup
import requests


class Book:
    html = ''
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, 'lxml')

    def parsing(self):
        active_1 = self.html.find('div', class_='fn dob').text.split()
        print(active_1[0], active_1[1])
        rating = self.html.find('div', class_='fn dob').text.split()
        print(rating[-1])

    def run(self):
        self.get_html()
        self.parsing()

