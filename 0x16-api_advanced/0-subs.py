#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    headers = {'User-Agent': '0x16-api_advanced/0.1 (by /u/Chemistry_Amu)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (0)
    
    results = response.json().get("data")
    return (results.get("subscribers"))
