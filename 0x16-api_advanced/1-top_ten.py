#!/usr/bin/python3
"""Get the 10 top posts on a Subreddit"""


import http.client
import io
import json
import urllib.parse


def top_ten(subreddit):
    """Get the 10 top posts on a Subreddit"""

    path = '/r/' + urllib.parse.quote(subreddit, safe='') + '/hot.json'
    path += '?raw_json=1&limit=10'
    client = http.client.HTTPSConnection('www.reddit.com')
    client.connect()
    client.putrequest('GET', path)
    client.putheader('Connection', 'close')
    client.putheader('User-Agent', 'python:hbtn701t1:1 (by /u/SamHermesBoots)')
    client.endheaders()
    response = client.getresponse()
    if response.status != 200:
        client.close()
        print(None)
        return
    posts = json.load(io.TextIOWrapper(response, encoding='UTF-8'))
    client.close()
    for post in posts['data']['children']:
        print(post['data']['title'])
