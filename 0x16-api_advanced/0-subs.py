#!/usr/bin/python3
''' Queries given API '''

import requests


def number_of_subscribers(subreddit):
    '''' Returns number of subscribers for a given subreddit '''
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'ubuntu/20.04'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return (0)
    return (response.json().get('data').get('subscribers'))
