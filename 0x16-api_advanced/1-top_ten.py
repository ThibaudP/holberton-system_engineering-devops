#!/usr/bin/python3
"""
1-top_ten
"""
import requests


def top_ten(subreddit):
    """fetches the number of subscribers to a subreddit"""

    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {"User-Agent": "ubuntu:hbtn:v1.0 (by /u/eskaps)"}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 404:
        print(None)
    else:
        for child in request.json().get("data").get("children"):
            print(child.get("data").get("title"))
