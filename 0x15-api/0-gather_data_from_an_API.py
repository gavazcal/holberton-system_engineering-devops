#!/usr/bin/python3
"""
    Uses REST API to return information about an employee
"""

import requests
from sys import argv


if __name__ == "__main__":
    user_id = int(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.
                        format(user_id)).json()
    user_to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'.
                        format(user_id)).json()

    done_tasks = []

    for task in user_to_do:
        if task.get('completed') is True:
            done_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(done_tasks), len(user_to_do)))
    for task in done_tasks:
            print("\t {}".format(task))
