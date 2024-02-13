# Homework_12



def print_scores(name, surname, *scores):
    print('Name:', name)
    print('Surname:', surname)
    for score in scores:
        print(score, end=' ')
    print()


print_scores('Roman', 'Silkin', 5, 5)
print_scores('Nikita', 'Silkin', 5)

