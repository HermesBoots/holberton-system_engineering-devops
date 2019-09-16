#!/usr/bin/python3
"""Synthesize data from an HTTP API"""


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
    done = [task for task in tasks if task['completed']]
    print('Employee {} is done with tasks({}/{})'.format(
        user['name'],
        len(done),
        len(tasks)
    ))
    for task in done:
        print('\t ' + task['title'])
