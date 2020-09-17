#!/usr/bin/python3
""" Basic reddit query """

import requests


def number_of_subscribers(subreddit):
    """ Number of subscribers for a subreddit """

    Udata = {'User-Agent': 'JavaPhish 1.0'}

    """ The about page has the sub count """
    req_url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    api = requests.get(req_url, headers=Udata, allow_redirects=False)

    """ If we werent redirected (301) or 404 then we found the sub"""
    if api.status_code == 200:
        jso = api.json()
        return jso['data']['subscribers']

    return (0)
