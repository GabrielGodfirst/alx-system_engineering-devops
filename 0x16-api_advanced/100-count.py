#!/usr/bin/python3

import requests


def count_words(subreddit, word_list, counts={}):
    """
    Recursively queries the Reddit API, parses the title of all hot articles
    """
    if not word_list:
        return

    if not counts:
        counts = {word.lower(): 0 for word in word_list}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            title_words = title.lower().split()
            for word in word_list:
                word_lower = word.lower()
                counts[word_lower] += title_words.count(word_lower)

        if 'after' in data['data'] and data['data']['after'] is not None:
            return count_words(subreddit, word_list, counts=counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    else:
        print(None)
