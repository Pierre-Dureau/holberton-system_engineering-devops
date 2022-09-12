#!/usr/bin/python3
"""export data in the CSV format"""

if __name__ == '__main__':

    import csv
    import requests
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    url2 = 'https://jsonplaceholder.typicode.com/todos'
    user = requests.get(url)
    username = user.json().get('username')
    todos = requests.get(url2)

    with open('{}.csv'.format(id), mode='w') as file:
        taskswriter = csv.writer(file, delimiter=',', quotechar='"',
                                 quoting=csv.QUOTE_ALL)

        for todo in todos.json():
            if todo.get('userId') == int(id):
                taskswriter.writerow([id, username, todo.get('completed'),
                                      todo.get('title')])
