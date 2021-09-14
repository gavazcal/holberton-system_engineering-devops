#!/usr/bin/python3
"""
    task 3
"""

import json
import requests
from sys import argv


if __name__ == "__main__":
    rest = 'https://jsonplaceholder.typicode.com/'
    user_to_do = requests.get(rest + 'users').json()
    user_json = {}

    for users in user_to_do:
        user_id = users.get('id')
        user_todo = requests.get(rest + 'todos?userId={}'
                                 .format(user_id)).json()
        user_tasks = []

        for todo in user_todo:
            newdic = {}
            newdic["task"] = todo.get('title')
            newdic["completed"] = todo.get('completed')
            newdic["username"] = users.get('username')

            user_tasks.append(newdic)

        user_json[user_id] = user_tasks
    with open("todo_all_employees.json".format(user_id), 'w') as json_file:
        json.dump(user_json, json_file)
    json_file.close()
