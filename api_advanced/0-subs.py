#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'MyBot'}
    
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        res.raise_for_status()
    except requests.exceptions.HTTPError:
        return 0
        
    data = res.json().get('data')
    if data:
        return data.get('subscribers', 0)
    else:
        return 0
