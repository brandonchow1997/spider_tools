import requests
import random


# 从代理池中随机选取代理
def proxy_pool():
    # 代理池list
    proxy_list = ['110.188.0.75:35236', '122.96.93.158:49435', '221.202.72.250:53281', '61.50.131.234:8080']
    # 获取代理数
    len_list = len(proxy_list)
    # 随机选取代理
    a = random.randint(0, len_list - 1)
    return proxy_list[a]


# 使用返回的代理检验是否可用
def get_proxy(proxy):
    # proxy = '110.188.0.75:35236'
    proxies = {
        'http': 'http://' + proxy,
        'https': 'https://' + proxy,
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        print(response.text)
    except requests.exceptions.ConnectionError as e:
        print('Error', e.args)


# 使用返回的代理 通过selenium检测是否可用
def get_proxy_selenium(proxy):
    # -----------------------------------Selenium
    from selenium import webdriver

    # proxy = '110.188.0.75:35236'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--proxy-server=http://' + proxy)
    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.get('http://httpbin.org/get')
    print(browser.page_source)


if __name__ == '__main__':
    proxy = proxy_pool()
    get_proxy(proxy)
    print('-'*20)
    get_proxy_selenium(proxy)