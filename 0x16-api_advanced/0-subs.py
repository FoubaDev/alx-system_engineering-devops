#!/usr/bin/python3
"""
Function that queries the Reddit API and returns the number
of subscribers (not active users, total subscribers)
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers
    for a given subreddit.
    If an invalid subreddit is given, the function returns 0.
    """
    url = f"https://api.reddit.com/r/{subreddit}/about"
    headers = {
        "User-Agent": "MyUserAgent/1.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data["data"]["subscribers"]
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        return 0
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to Reddit API")
        return 0
