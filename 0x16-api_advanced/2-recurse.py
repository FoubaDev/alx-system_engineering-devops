#!/usr/bin/python3
import requests
"""
Querries the Reddit API with recursive function
"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
    Write a recursive function that queries the Reddit API and returns \
            a list containing the titles of all hot articles for a given \
            subreddit. If no results are found for the given subreddit, \
            the function should return None.
    """
    import requests

    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json"
                            .format(subreddit),
                            params={"count": count, "after": after},
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 400:
        return None

    hot_l = hot_list + [child.get("data").get("title")
                        for child in sub_info.json()
                        .get("data")
                        .get("children")]

    info = sub_info.json()
    if not info.get("data").get("after"):
        return hot_l

    return recurse(subreddit, hot_l, info.get("data").get("count"),
                   info.get("data").get("after"))
