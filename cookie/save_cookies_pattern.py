import requests

# cookie
url = 'https://zhihu.com/'
r = requests.get(url)

cookies = r.cookies
# 遍历cookies字典
for k, v in cookies.get_dict().items():
    print(k, ':', v)

# 提交cookie
cookies = {
    'c1': 'v1',
    'c2': 'v2'
}
r = requests.get('http://', cookies=cookies)
print(r.text)
