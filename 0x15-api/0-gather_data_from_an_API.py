#!/usr/bin/python3
"""for a given employee ID,
returns information about his/her todo list progress"""

if __name__ == '__main__':
    import requests
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url2 = 'https://jsonplaceholder.typicode.com/todos'

    user = requests.get(url)
    name = user.json().get('name')

    todos = requests.get(url2)
    done = 0
    all = 0
    for todo in todos.json():
        if todo.get('userId') == int(id):
            all += 1
            if todo.get('completed') is True:
                done += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, done, all))

    for todo in todos.json():
        if todo.get('userId') == int(id) and todo.get('completed') is True:
            print("\t {}".format(todo.get('title')))
