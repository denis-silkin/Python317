#  Homework_18
import re


# kazantip_11-@dgrger


s = input('Введите пароль: ')
reg = r'[a-zA-Z0-9-@_]{6,18}'
print(re.findall(reg, s))
