'''fetch('https://jsonplaceholder.typicode.com/posts')
  .then((response) => response.json())
  .then((json) => console.log(json));'''
import json

import requests

response = requests.request(method="GET", url='https://jsonplaceholder.typicode.com/posts')
body = json.loads(response.text)
result = []

for i in body:
    if i['userId'] == 1 and i['id'] == 5:
        new_d = {}
        new_d['title'], new_d['body'] = i['title'], i['body']
        result.append(new_d)

print(result)
