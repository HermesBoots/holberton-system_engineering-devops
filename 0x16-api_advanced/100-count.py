#!/usr/bin/python3
"""Get frequency of keywords in posts in a Subreddit"""


import collections
import http.client
import io
import json
import urllib.parse


def count_words(subreddit, word_list, hot_list=[], after=None, client=None):
    """Get frequency of keywords in posts in a Subreddit"""

    path = '/r/' + urllib.parse.quote(subreddit, safe='') + '/hot.json'
    path += '?raw_json=1'
    if after is not None:
        path += '&after=' + urllib.parse.quote_plus(after)
        path += '&count=' + str(len(hot_list))
    if client is None:
        client = http.client.HTTPSConnection('www.reddit.com')
        client.connect()
    client.putrequest('GET', path)
    client.putheader('Connection', 'keep-alive')
    client.putheader('User-Agent', 'python:hbtn701t3:0 (by /u/SamHermesBoots)')
    client.endheaders()
    response = client.getresponse()
    if response.status != 200:
        client.close()
        return None
    posts = json.load(io.TextIOWrapper(response, encoding='UTF-8'))
    if response.getheader('Connection', 'close') == 'close':
        client.close()
        client = None
    hot_list.extend(p['data']['title'] for p in posts['data']['children'])
    after = posts['data']['after']
    if after is None:
        client.close()
        words = collections.Counter(' '.join(hot_list).lower().split())
        words = sorted(
            ((word, words[word.lower()]) for word in word_list),
            key=lambda pair: pair[1],
            reverse=True
        )
        for word, count in words:
            print(word, ': ', count, sep='')
        return
    return count_words(subreddit, word_list, hot_list, after, client)
