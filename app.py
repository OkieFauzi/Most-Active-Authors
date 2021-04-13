import requests
import json

resp = requests.get('https://jsonmock.hackerrank.com/api/article_users/search')
total_pages = resp.json()['total_pages']

def active_authors(treshold):
    submission_count = []
    i = 1
    while i <= total_pages:
        response = requests.get('https://jsonmock.hackerrank.com/api/article_users/search?page=' + str(i))
        datas = response.json()['data']
        for data in datas:
            if data['submission_count'] > treshold:
                count = data['username']
                submission_count.append(count)
        i = i + 1
    return submission_count

print(active_authors(10))