#!/usr/bin/python3
"""Get the number of subscribers to a Subreddit"""


import io
import json
import requests
import urllib.parse


def number_of_subscribers(subreddit):
    """Get the number of subscribers to a Subreddit"""

    path = 'https://www.reddit.com'
    path += '/r/' + urllib.parse.quote(subreddit, safe='') + '/about.json'
    path += '?raw_json=1'
    headers = {
        'Connection': 'close',
        'User-Agent': 'python:hbtn701t0:2 (by /u/SamHermesBoots)'
    }
    response = requests.get(path, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    info = response.json()
    return info['data']['subscribers']
