#!/usr/bin/python3
"""Synthesize data from an HTTP API"""


import csv
import json
import sys
import urllib.request


if __name__ == '__main__':
    request = urllib.request.Request(
        'https://jsonplaceholder.typicode.com/users'
    )
    with urllib.request.urlopen(request) as response:
        users = json.loads(response.read().decode())
    users = {user['id']: user for user in users}
    request = urllib.request.Request(
        'https://jsonplaceholder.typicode.com/todos'
    )
    with urllib.request.urlopen(request) as response:
        tasks = json.loads(response.read().decode())
    tasks = {user['id']: [
        {
            'username': user['username'],
            'task': task['title'],
            'completed': task['completed']
        } for task in tasks if task['userId'] == user['id']
    ] for user in users.values()}
    with open('todo_all_employees.json', 'wt') as file:
        json.dump(tasks, file)
