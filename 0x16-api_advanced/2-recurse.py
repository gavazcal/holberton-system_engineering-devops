#!/usr/bin/python3
"""
recursive function that returns all hot articles from a sub
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """recursion"""
    uagent = {'User-agent': 'requested'}
    url = 'https://www.reddit.com/'
    q = 'r/{}/hot.json?after={}'.format(subreddit, after)
    args = {'after': after, 'limit': '100'}
    response = requests.get(url + q, headers=uagent)
    results = response.json().get('data', {}).get('children', [])
    after = response.json().get('data', {}).get('after', None)
    if not results:
        return None
    for entry in results:
        hot_list.append(entry.get('data').get('title'))
    if not after:
        return hot_list
    return recurse(subreddit, hot_list, after)
