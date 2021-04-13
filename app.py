import requests
import json

parameter = {
    "page": 1
}

response = requests.get('https://jsonmock.hackerrank.com/api/article_users/search', params=parameter)
datas = response.json()['data']

def active_authors(treshold):
    submission_count = []
    for data in datas:
        if data['submission_count'] > treshold:
            count = data['username']
            submission_count.append(count)
    print(submission_count)

active_authors(100)

