# Homework_10


matematika = ['Матвей', 'Евгения', 'Михаил', 'Максим', 'Наталья']
fizika = ['Максим', 'Матвей', 'Александр']
print("Все призеры:", list(set(matematika + fizika)))
print('Призеры обеих олимпиад:', set(matematika) & set(fizika))
print('Обновленный список призеров по математике:', set(matematika) & set(fizika))
del fizika

