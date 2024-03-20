#  Homework_20
import os


print("Текущая директория:", os.getcwd())
os.chdir('..')
print("Текущая директория изменилась на python:", os.getcwd())

dirs = r'folder\Work'
o = os.listdir(dirs)
print(o)
o = list(map(lambda i: os.path.join(dirs, i), o))

print(sorted(o, key=os.path.isfile, reverse=True))


