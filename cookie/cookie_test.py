import split_cookies
import requests
from lxml import etree
import time


def login(page):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.0.16453 '
    }
    cookies = 'user_session=lvQFTkr6M5Oyge1ysF0Fp7rjVwUkuZBJcnmMPH-4A4v2lPSy; path=/; expires=Fri; __Host-user_session_same_site=lvQFTkr6M5Oyge1ysF0Fp7rjVwUkuZBJcnmMPH-4A4v2lPSy; path=/; expires=Fri; _gh_sess=dG5uRG95YmFsYkRPSjhDcUEvSW1BdFNWeXY2UFVlN0pJcVZFZHFkMlYzM0EySDUvVDg2azkvRXlGY1ExSEN4ZUJWN2duWFlwcWJHeVkrWFBKZmY1bHMwWFF5am8wRG9Hc0h4eVEvUUN3QTR3UHNVN3VIZHdTVllzaFFkbzdzQk9mNEJPVytzZ2hPZVkzQmVYRStoUmtBPT0tLVFWcjlDZEYxYnBDVWp0aFZJRXU0ZlE9PQ%3D%3D--08129c1a2445e2b45901d0197f06c5c7e74c08ca'
    cookie = split_cookies.split_cookies(cookies)
    """
    cookie = {
        # cookie修改自己的GitHubcookie值
        # user_session为记录用户登录状态的cookie
        'user_session': 'lvQFTkr6M5Oyge1ysF0Fp7rjVwUkuZBJcnmMPH-4A4v2lPSy',
    }
    """
    url = 'https://github.com/discover?utf8=%E2%9C%93&recommendations_after=' + str(page * 20)
    response = requests.get(url, headers=header, cookies=cookie)
    print(response.status_code)
    print('-' * 20)
    return response.text


def parse_page(html):
    data = etree.HTML(html)
    title = data.xpath('/html/body/div[4]/div[1]/div/h1/text()')
    items = data.xpath('//*[@id="recommended-repositories-container"]/div/div')
    print(title[0])
    print('|'*40)
    for item in items:
        owner = item.xpath('./div[2]/div[2]/div/div[1]/h3/a/span/text()')
        repository = item.xpath('./div[2]/div[2]/div/div[1]/h3/a/text()')
        contents = item.xpath('./div[2]/div[2]/div/p[@itemprop="description"]/text()')
        # topics = item.xpath('./div[2]/div[2]/div/div[2]/a/text()')
        stars = item.xpath('./div[2]/div[2]/div/div[@class="f6 text-gray mt-2"]/a/text()')
        programming_language = item.xpath('./div[2]/div[2]/div/div[@class="f6 text-gray mt-2"]/span[2]/text()')
        updated = item.xpath('./div[2]/div[2]/div/div[@class="f6 text-gray mt-2"]/relative-time/text()')
        # repository 字符串连接
        info = ''.join(owner).join(repository).strip()
        print(info)
        # description 字符串连接
        content = ''.join(contents).strip()
        print('description:', content)
        # stars
        print('stars:', end='')
        print(stars[1].strip())
        #for topic in topics:
            #print(topic, end=',')
        # programming_language
        programming_language = ''.join(programming_language).strip()
        print('programming_language:', programming_language)
        print('Updated:', updated[0])

        result = {
            'repository': info,
            'description': content,
            'stars': stars[1].replace('\n', ''),
            'programming_language': programming_language,
            'updated': updated[0]
        }
        print('-'*10)


MAX_PAGE = 20
if __name__ == '__main__':
    for page in range(0, MAX_PAGE):
        print('-- 正在爬取第{page}页 --'.format(page=page+1))
        html = login(page)
        parse_page(html)
        time.sleep(2)

