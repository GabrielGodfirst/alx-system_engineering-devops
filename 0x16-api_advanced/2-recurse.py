#!/usr/bin/python3

import requests


def recurse(subreddit, hot_list=[]):
    """
    Recursively queries the Reddit API and returns a list containing the titles
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            hot_list.append(post['data']['title'])

        # Check if there are more pages to fetch
        if 'after' in data['data'] and data['data']['after'] is not None:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return (None)
