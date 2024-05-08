# 0x16. API advanced

#### 0x16. API advanced

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

###### General

* How to read API documentation to find the endpoints you’re looking for
* How to use an API with pagination
* How to parse JSON results from an API
* How to make a recursive API call
* How to sort a dictionary by value

##  Tasks
## 0. How many subs?
* [ 0-subs.py](./ 0-subs.py)
Write a function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API. If you’re getting errors related to Too Many Requests, ensure you’re setting a custom User-Agent.
* [ 0-subs.py](./ 0-subs.py)

## 1. Top Ten

Prototypes for functions written in this project:

Write a function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.


## 2. Recurse it!:
* [ 2-recurse.py](./ 2-recurse.py)
Write a recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.


| File                    | Prototype                             |
| ----------------------- | ------------------------------------- |
| `0-subs.py`             | `def number_of_subscribers(subreddit)`|
| `1-top_ten.py`          | `def top_ten(subreddit)`              |
| `2-recurse.py`          | `def recurse(subreddit, hot_list=[])` |

