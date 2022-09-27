#!/usr/bin/python3
"""Module for the top_ten fonction"""
import requests


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts listed for a subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    req = requests.get(url, headers=headers)
    if req.status_code >= 400:
        print("None")
        return
    data = req.json()['data']['children']
    i = 0
    for post in data:
        print(post['data']['title'])
        i += 1
        if i == 10:
            break
