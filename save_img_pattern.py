import requests

url = 'http://'
r = requests.get(url)
with open('img.jpg', 'wb') as fo:
    fo.write(r.content)