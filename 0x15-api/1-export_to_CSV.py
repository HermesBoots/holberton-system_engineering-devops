#!/usr/bin/python3
"""Synthesize data from an HTTP API"""


import csv
import json
import sys
import urllib.request


if __name__ == '__main__':
    userId = int(sys.argv[1])
    request = urllib.request.Request(
        'https://jsonplaceholder.typicode.com/users'
    )
    with urllib.request.urlopen(request) as response:
        users = json.loads(response.read().decode())
    users = {user['id']: user for user in users}
    user = users[userId]
    request = urllib.request.Request(
        'https://jsonplaceholder.typicode.com/todos'
    )
    with urllib.request.urlopen(request) as response:
        tasks = json.loads(response.read().decode())
    tasks = [task for task in tasks if task['userId'] == userId]
    with open(sys.argv[1] + '.csv', 'wt', newline='') as file:
        file = csv.writer(file, quoting=csv.QUOTE_ALL)
        row = [userId, user['name'], '', '']
        for task in tasks:
            row[2] = str(task['completed'])
            row[3] = task['title']
            file.writerow(row)
