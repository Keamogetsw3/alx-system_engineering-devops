#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number of subscribers.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    """
    if not isinstance(subreddit, str) or not subreddit:
        return 0

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:V1.0.0 (by /u/Chemistry_Amu)"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            return response.json().get("data", {}).get("subscribers", 0)
    except requests.RequestException:
        return 0

    return 0


if __name__ == "__main__":
    import sys
    print(number_of_subscribers(sys.argv[1]))
