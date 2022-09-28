#!/usr/bin/python3
"""Module for the count_words fonction"""
import requests


def count_words(subreddit, word_list, after=None, dictCount={}):
    """prints a sorted count of given keywords"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent 1.0'}
    param = {'after': after}
    req = requests.get(url, headers=headers, params=param)
    if req.status_code >= 400:
        return
    data = req.json()['data']['children']
    after = req.json()['data']['after']

    for post in data:
        title = post['data']['title']
        line = title.lower().split()
        for keyword in word_list:
            if keyword.lower() in line:
                for word in line:
                    if word == keyword.lower():
                        if keyword.lower() not in dictCount.keys():
                            dictCount[word.lower()] = 1
                        else:
                            dictCount[word.lower()] += 1

    if after is None:
        dictCount = sorted(dictCount.items(), key=lambda a: (-a[1], a[0]))
        for k, v in dictCount:
            print(k + ': ' + str(v))
        return

    return count_words(subreddit, word_list, after, dictCount)
