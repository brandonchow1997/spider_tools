import requests

data = {
    'data1': 'XXXXX',
    'data2': 'XXXXX'
}
url = 'xxx'
# Requests：data为dict，json
response = requests.get(url=url, params=data)