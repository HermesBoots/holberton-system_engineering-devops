#!/usr/bin/python3
"""Get the number of subscribers to a Subreddit"""


import http.client
import io
import json
import urllib.parse


def number_of_subscribers(subreddit):
    """Get the number of subscribers to a Subreddit"""

    path = '/r/' + urllib.parse.quote(subreddit, safe='') + '/about.json'
    path += '?raw_json=1'
    client = http.client.HTTPSConnection('www.reddit.com')
    client.connect()
    client.putrequest('GET', path)
    client.putheader('Connection', 'close')
    client.putheader('User-Agent', 'python:hbtn701t0:1 (by /u/SamHermesBoots)')
    client.endheaders()
    response = client.getresponse()
    if response.status != 200:
        client.close()
        return 0
    info = json.load(io.TextIOWrapper(response, encoding='UTF-8'))
    client.close()
    return info['data']['subscribers']
