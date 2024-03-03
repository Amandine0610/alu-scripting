#!/usr/bin/python3
"""Prints the title of the first 10 hot posts listed for a given subreddit"""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyBot'}
    
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        res.raise_for_status()
    except requests.HTTPError:
        print(None)
        return
        
    data = res.json().get('data')
    if not data:
        print(None)
        return
        
    for i, post in enumerate(data['children']):
        if i == 10:
            break
        print(post['data']['title'])
