#!/usr/bin/python3
"""Synthesize data from an HTTP API"""


import json
import sys
import urllib.request


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    response = urllib.request.urlopen(url)
    user = json.loads(response.read().decode())
    response.close()
    url = 'https://jsonplaceholder.typicode.com/todos?userId=' + sys.argv[1]
    response = urllib.request.urlopen(url)
    tasks = json.loads(response.read().decode())
    response.close()
    done = [task for task in tasks if task.get('completed')]
    print('Employee {} is done with tasks({}/{})'.format(
        user.get('name'),
        len(done),
        len(tasks)
    ))
    for task in done:
        print('\t ' + task.get('title'))
