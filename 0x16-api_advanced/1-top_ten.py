#!/usr/bin/python3
''' Queries given API for hottest subreddits '''

import requests


def top_ten(subreddit):
    ''' Prints titles of 10 hottest posts on given subreddit '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "ubuntu/20.04"}
    parameters = {"limit": 10}
    response = requests.get(url, headers=headers,
                            params=parameters, allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return
    else:
        titles = response.json().get('data').get('children')
        for t in titles:
            print(t.get('data').get('title'))
