#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers 
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers 
    """
    url = ("https://api.reddit.com/r/{}/about".format(subreddit))
    header = {'User-Agent': 'alx_api_advanced'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        return (response.json().get("data").get("subscribers"))
    return (0)
