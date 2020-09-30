#!/usr/bin/python3
""" Basic reddit query """

import requests


def top_ten(subreddit):
    """ top ten posts on a given sub reddit """

    Udata = {'User-Agent': 'JavaPhish 2.0'}

    req_url = 'https://www.reddit.com/r/{}/top.json?limit=10'.format(subreddit)
    api = requests.get(req_url, headers=Udata, allow_redirects=False)

    if (api.status_code == 200):
        data = api.json()['data']
        for post in data['children']:
            print(post['data']['title'])
    else:
        print('None')
