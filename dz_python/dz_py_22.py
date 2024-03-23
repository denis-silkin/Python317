# Homework_22


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    @age.deleter
    def age(self):
        del self.__age


p1 = Person('Denis', 21)
print(p1.__dict__)
p1.name = 'denis'
print(p1.name)
p1.age = 13
print(p1.age)
del p1.name
# del p1.age

print(p1.__dict__)




