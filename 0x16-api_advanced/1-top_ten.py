#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': 'alx_api_advanced'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return response.json().get("data", {}).get("subscribers", 0)

    return 0
