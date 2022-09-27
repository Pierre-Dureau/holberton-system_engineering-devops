#!/usr/bin/python3
"""Module for the number_of_subscribers fonction"""
import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    req = requests.get(url, headers=headers)
    if req.status_code >= 400:
        return 0
    return req.json()['data']['subscribers']
