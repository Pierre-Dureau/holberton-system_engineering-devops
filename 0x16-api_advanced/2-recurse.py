#!/usr/bin/python3
"""Module for the recurse fonction"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """returns a list containing the titles of all hot articles for
    a given subreddit using recursion"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    param = {'after': after}
    req = requests.get(url, headers=headers, params=param)
    if req.status_code >= 400:
        return
    data = req.json()['data']['children']
    after = req.json()['data']['after']
    for post in data:
        hot_list.append(post['data']['title'])
    if after:
        recurse(subreddit, hot_list, after)
    return hot_list
