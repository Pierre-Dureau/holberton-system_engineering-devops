#!/usr/bin/python3
"""export data in the JSON format"""

if __name__ == '__main__':

    import json
    import requests

    url = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url).json()
    dict = {}

    for user in users:
        id = user.get('id')
        url2 = url + str(id) + '/todos'
        todos = requests.get(url2).json()

        tasks = []
        for todo in todos:
            task = {}
            task['username'] = user.get('username')
            task['task'] = todo.get('title')
            task['completed'] = todo.get('completed')
            tasks.append(task)
        dict[id] = tasks

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(dict, file)
