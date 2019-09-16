#!/usr/bin/python3
"""Synthesize data from an HTTP API"""


import json
import sys
import urllib.request


if __name__ == '__main__':
    request = urllib.request.Request(
        'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    )
    with urllib.request.urlopen(request) as response:
        user = json.loads(response.read().decode())
    request = urllib.request.Request(
        'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    )
    with urllib.request.urlopen(request) as response:
        tasks = json.loads(response.read().decode())
    done = [task for task in tasks if task['completed']]
    print('Employee {} is done with tasks({}/{})'.format(
        user['name'],
        len(done),
        len(tasks)
    ))
    for task in done:
        print('\t ' + task['title'])
