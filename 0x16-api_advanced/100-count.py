#!/usr/bin/python3
import requests
"""
function that queries the Reddit API, parses the title of all hot articles
"""


def count_words(subreddit, word_list, hot_list=[], viewed_count=0, after=''):
    """
    Write a recursive function that queries the Reddit API, parses the title\
            of all hot articles, and prints a sorted count of given keywords\
            (case-insensitive, delimited by spaces. Javascript should count\
            as javascript, but java should not).
    """
    base = 'https://www.reddit.com/'
    endpoint = 'r/{}/hot.json'.format(subreddit)
    query_string = '?show="all"&limit=100&after={}&count={}'.format(
        after, viewed_count)
    url = base + endpoint + query_string
    headers = {'User-Agent': 'Python3(ALX)'}
    response = requests.get(url, headers=headers)
    if not response.ok:
        return

    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    after = data['after']
    dist = data['dist']
    if (after):
        count_words(subreddit, [], hot_list, viewed_count + dist, after)

    if viewed_count == 0:
        result = {}
        word_list = [word.lower() for word in word_list]
        hot_words = ' '.join(hot_list).lower().split(' ')
        for hot_word in hot_words:
            for search_word in word_list:
                if hot_word == search_word:
                    result.setdefault(search_word, 0)
                    result[search_word] += 1

        for word, count in sorted(
            sorted(result.items()), key=lambda x: x[1], reverse=True
        ):
            print("{}: {}".format(word, count))
