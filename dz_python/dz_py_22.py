# Homework_22


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def del_name(self):
        del self.__name


p1 = Person('Denis', 21)
print(p1.__dict__)
p1.name = 'denis'
print(p1.name)
p1.age = 25
print(p1.age)
del p1.name
print(p1.__dict__)


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def __check_value(self, a):
#         if isinstance(a, int) or isinstance(a, str):
#             return True
#         return False
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         if Person.__check_value():
#             self.__name = name
#
#     @name.deleter
#     def name(self):
#         del self.__name
#
#
# p1 = Person('Denis', 2)
# p1.name = 'Stas', 2
# print(p1.name)
# # print(p1.__dict__)
