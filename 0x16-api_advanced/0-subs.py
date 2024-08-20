"""
 function that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers (not active users, total subscribers) for a given subreddit
    """
    if subreddit is None or type(subreddit) is not str:
        return 0
    response = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': '0x16-api_advanced:project:\
v1.0.0 (by /u/Chemistry_Amu'}).json()
    subs = response.get("data", {}).get("subscribers", 0)
    return subs
