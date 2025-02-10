#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/Chemistry_Amu)"
    }
    params = {
        "limit": 10
    }

    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    # Check if the response is valid JSON
    if response.status_code != 200:
        print("None")
        return

    try:
        response_json = response.json()
    except ValueError:
        print("Error: Invalid JSON response.")
        return

    # Handle empty responses or invalid subreddits
    results = response_json.get("data", {}).get("children", [])
    if not results:
        print("None")
    else:
        for c in results:
            print(c.get("data", {}).get("title", "No title available"))
