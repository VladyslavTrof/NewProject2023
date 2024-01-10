import requests
 url comments = 'https://dummyjson.com/comments?limit=340'

url comments = 'https://dummyjson.com/comments?limit=340'
response = requests. get (url=url_comments)
data from net = response. json ()
comments = data_from_netI'comments'1# list of dicts


for comment in comments:
    if comment'user'l'id'] == 31:
print(comment)