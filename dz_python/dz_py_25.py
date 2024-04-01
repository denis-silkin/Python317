# Homework_25

class Student:
    def __init__(self, name):
        self.name = name
        self.lp = self.Laptop()

    def print_info(self):
        print(self.name, '=>', self.Laptop.comp())

    class Laptop:
        @staticmethod
        def comp():
            return 'hp', 'i7', '16'


st = Student('Roman')
st.print_info()
st1 = Student('Vladimir')
st1.print_info()

