#!/usr/bin/python3
"""
    Uses REST API to return information about an employee
"""

import requests
from sys import argv


if __name__ == "__main__":
    rest = 'https://jsonplaceholder.typicode.com/'
    user_id = int(argv[1])
    name = requests.get(rest + 'users/{}'.format(user_id)).json()
    user_to_do = requests.get(rest + 'todos?userId={}'.format(user_id)).json()

    done_tasks = []

    for task in user_to_do:
        if task.get('completed') is True:
            done_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(name.get('name'), len(done_tasks), len(user_to_do)))
    for task in done_tasks:
            print("\t {}".format(task))
