#!/usr/bin/python3
""" Recursive function that queries the Reddit API """

import requests
after = None
count_dict = []


def count_words(subreddit, word_list):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces) """
    global after
    global count_dict
    headers = {'User-Agent': 'ubuntu/20.04'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    response = requests.get(url, headers=headers, allow_redirects=False,
                            params=parameters)
