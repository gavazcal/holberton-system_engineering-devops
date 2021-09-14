#!/usr/bin/python3
"""
    exports data in JSON format
"""

import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    rest = 'https://jsonplaceholder.typicode.com/'
    user_id = int(argv[1])
    name = requests.get(rest + 'users/{}'.format(user_id)).json()
    user_to_do = requests.get(rest + 'todos?userId={}'.format(user_id)).json()

    done_tasks = []

    for todo in user_to_do:
        if todo.get('completed') is True:
            done_tasks.append(todo.get('title'))
    print("Employee {} is done with todos({}/{}):".
          format(name.get('name'), len(done_tasks), len(user_to_do)))
    for todo in done_tasks:
        print("\t {}".format(todo))

    with open('{}.csv'.format(user_id), "w") as csv_file:
        info = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in user_to_do:
            info.writerow(
                [user_id,
                 name.get('username'),
                 todo.get('completed'),
                 todo.get('title')])

    todo_list = []
    for todo in user_to_do:
        tasks_dict = {}
        tasks_dict["task"] = todo.get('completed')
        tasks_dict["completed"] = todo.get('completed')
        tasks_dict["username"] = name.get('username')
        todo_list.append(tasks_dict)
    json_format = {}
    json_format[user_id] = todo_list
    with open("{}.json".format(user_id), 'w') as JSON_file:
        json.dump(json_format, JSON_file)
