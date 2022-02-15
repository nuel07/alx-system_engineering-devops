#!/usr/bin/python3
''' recursive function that queries given API '''

import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    ''' returns a list containing the titles of all hot articles
    for a given subreddit
    Arguments:
         hot_list: list of hottest articles for subreddit
         after: last hot_item appended to hot_list
    Returns
        a list of all hot articles for subreddit
        otherwise, None, if queried subreddit is invalid
    '''
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {"User-Agent": "ubuntu/20.04"}
    params = {"after":after, "count":count, "limit":10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 404:
        return None
    results = response.json().get('data')
    after = results.get("after")
    count += results.get('dist')

    for child in results.get('children'):
        hot_list.append(child.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    else:
        return hot_list
