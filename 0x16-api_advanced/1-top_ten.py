#!/usr/bin/python3
"""
prints the first 10 posts for any subreddit
"""

import json
import requests


def top_ten(subreddit):
    """retrieves top 10"""
    url = "https://reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    agent = {'User-agent': 'requested'}
    request = requests.get(url, headers=agent)
    r = request.json()
    if request.status_code == 404:
        print(None)
    else:
        sub_dict = r["data"]["children"]
        for idx in range(len(sub_dict)):
            print(sub_dict[idx]["data"]["title"])
