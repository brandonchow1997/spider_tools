from io import BytesIO
import requests
from PIL import Image


# 二进制数据
url = ''
r = requests.get(url)
image = Image.open(BytesIO(r.content))
image.save('xxx.jpg')


# 原数据处理
r = requests.get(url)
with open('xxx.jpg', 'wb+') as f:
    for chunk in r.iter_content(1024):
        f.write(chunk)