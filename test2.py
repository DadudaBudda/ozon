import requests

response = requests.request(method="GET", url='https://jsonplaceholder.typicode.com/posts')
body = response.json()
result = [i for i in body if i['userId'] == 1 and i['id'] == 5]
for _ in result:
    del _['userId'], _['id']
print(result)
