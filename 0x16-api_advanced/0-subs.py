#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    """
    url = f"https://www.reddit.com/r/{}/about.json"
    headers = {"User-Agent": "python:subreddit.subscriber.counter:v1.0 (by /u/Chemistry_Amu)"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0
