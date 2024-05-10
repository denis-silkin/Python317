# Homework_32

import requests
import json
import csv

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)


with open('data_dz.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter=';', lineterminator='\r', fieldnames=todos[0].keys())
    writer.writeheader()
    for row in todos:
        writer.writerow(row)

with open('data_dz.csv') as f:
    print(f.read())
