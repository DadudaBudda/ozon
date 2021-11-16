'''fetch('https://jsonplaceholder.typicode.com/posts')
  .then((response) => response.json())
  .then((json) => console.log(json));'''
import json

import requests

response = requests.request(method="GET", url='https://jsonplaceholder.typicode.com/posts')
body = json.loads(response.text)
result = [i for i in body if i['userId'] == 1 and i['id'] == 5]
del result[0]['userId'], result[0]['id']
print(result)
