from retrying import retry
import requests
import urllib


@retry(wait_fixed=2000)
def get_page(page):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/47.0.2526.108 Safari/537.36 2345Explorer/8.8.0.16453 '
    }
    # 构造参数
    # 可更改
    data = {
        'pageSize': '60',
        # 城市ID 可更改
        'cityId': '636',
        'workExperience': '-1',
        'education': '-1',
        'companyType': '-1',
        'employmentType': '-1',
        'jobWelfareTag': '-1',
        # 可更改参数
        'kw': '爬虫',
        'kt': '3',
        # 可更改参数
        'lastUrlQuery': '{"p":2,"jl":"489","sf":"2001","st":"4000","kw":"爬虫","kt":"3"}',
        '': '2001'
    }
    print('正在爬取第', page, '页')
    url = 'https://fe-api.zhaopin.com/c/i/sou?start=' + str(page*60-60) + '&' + urllib.parse.urlencode(data)
    response = requests.get(url, headers=header)
    return response.json()


if __name__ == '__main__':
    # ------------ 获取数据 ---------------
    # get01()
    # get_page()
    for i in range(1, 20):
        html = get_page(i)
        print(html)

