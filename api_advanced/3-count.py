#!/usr/bin/python3
<<<<<<< HEAD
=======
"""
Script that queries the reddit API
returns a list containing the titles of all hot articles for a given subreddit
>>>>>>> 68b8ce230a4d3e06aa135669e86952be8f53256b
"""
function that queries the Reddit API
parses the title of all hot articles
prints a sorted count of given keywords
"""
import requests
import sys


<<<<<<< HEAD
def count_words(subreddit, word_list):
    """
    Module
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'myRedditScript/1.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:

        return None
    posts = response.json().get('data').get('children')
    word_count = {}
    for post in posts:
        title = post['data']['title']
        for word in word_list:
            if word.lower() in title.lower():
                word_count[word.lower()] = word_count.get(word.lower(), 0) + 1

    if not word_count:
        return
    for key, value in sorted(word_count.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(key.lower(), value))
    return count_words(subreddit, word_list)
=======
def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    url = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    headers = {"User-agent": "myRedditScript/1.0"}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            new_posts = data['data']['children']
            hot_list.extend([post['data']['title'] for post in new_posts])

            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None

    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
>>>>>>> 68b8ce230a4d3e06aa135669e86952be8f53256b
