from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def initial_browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    # chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # 添加代理 proxy
    # chrome_options.add_argument('--proxy-server=http://' + proxy)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver


def no_login(browser, url):
    browser.get(url)
    html = browser.page_source
    # print(html)
    time.sleep(2)
    return html


if __name__ == '__main__':
    browser = initial_browser()
