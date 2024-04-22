# Homework_30


import json
from random import choice


def gen_person():
    name = ''
    tel = ''
    dz = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    while len(dz) != 10:
        dz += choice(nums)

    person = {dz: {
            'name': name,
            'tel': tel
    }
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data = data | person_dict
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())


# def add_db(self):
# try:
# data = json.load(open('db.json'))
# except FileNotFoundError:
# data = {}

# js = [{student.name: student.marks} for student in self.students]
# data[self.group] = js
# with open("db.json", "w+") as f:
# json.dump(data, f, indent=2)
# print(f"Группа {self.group} добавлена в файл")
