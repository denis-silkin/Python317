# Homework_31

import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = json.loads(response.text)

todos_by_user = {}

for todo in todos:
    if todo['completed']:
        try:
            todos_by_user[todo['userId']] += 1
        except KeyError:
            todos_by_user[todo['userId']] = 1

print(todos_by_user)

top_user = sorted(todos_by_user.items(), key=lambda x: x[1], reverse=True)
print(top_user)

max_complete = top_user[0][1]

users = []
for user, num_complete in top_user:
    if num_complete < max_complete:
        break
    users.append(str(user))

max_users = ' and '.join(users)
print(f'users {max_users} completed {max_complete} Todos')

# Домашнее задание


def keep(tod):
    complete = tod["completed"]
    max_count = str(tod["userId"]) in users
    return complete and max_count


with open("data_file.json", "w") as f:
    filtered_todos = list(filter(keep, todos))
    json.dump(filtered_todos, f, indent=2)
