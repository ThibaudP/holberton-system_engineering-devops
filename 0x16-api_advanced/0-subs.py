#!/usr/bin/python3
"""
0-subs
"""
import requests


def number_of_subscribers(subreddit):
    """fetches the number of subscribers to a subreddit"""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "ubuntu:hbtn:v1.0 (by /u/eskaps)"}

    request = requests.get(url, headers=headers, allow_redirects=False)

    if request.status_code == 404:
        return 0

    return request.json().get("data").get("subscribers")
