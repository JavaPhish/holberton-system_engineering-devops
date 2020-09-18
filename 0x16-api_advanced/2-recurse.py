#!/usr/bin/python3
""" Basic reddit query """

import requests


def recurse(subreddit, hot_list=[], counter=0, data={}):
    """ top ten posts on a given sub reddit """

    if (counter == 0 and subreddit is not None):
        Udata = {'User-Agent': 'JavaPhish 2.0'}
        req_url = 'https://www.reddit.com/r/{}/top.json'.format(subreddit)
        api = requests.get(req_url, headers=Udata, allow_redirects=False)

        if (api.status_code == 200):
            data = api.json()['data']['children']
            hot_list.append(data[0]['data']['title'])
            counter += 1
            return (recurse(subreddit, hot_list, counter, data))
    elif (counter > 0):
        if (len(data) > counter + 1):
            hot_list.append(data[counter]['data']['title'])
            counter += 1
            return (recurse(subreddit, hot_list, counter, data))
        return (hot_list)
    else:
        return (None)
