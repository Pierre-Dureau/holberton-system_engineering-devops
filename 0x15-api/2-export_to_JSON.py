#!/usr/bin/python3
"""export data in the JSON format"""

if __name__ == '__main__':

    import json
    import requests
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(url)
    username = user.json().get('username')
    todos = requests.get(url2)

    with open('{}.json'.format(id), mode='w') as file:
        tasks = []
        for todo in todos.json():
            if todo.get('userId') == int(id):
                task = {}
                task['task'] = todo.get('title')
                task['completed'] = todo.get('completed')
                task['username'] = username
                tasks.append(task)
        dict = {}
        dict[id] = tasks
        json.dump(dict, file)
