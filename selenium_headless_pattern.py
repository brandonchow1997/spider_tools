from selenium import webdriver


def selenium_headless():
    # 创建chrome参数对象
    opt = webdriver.ChromeOptions()
    # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
    opt.set_headless()
    # 创建chrome无界面对象
    browser = webdriver.Chrome(options=opt)
    url = 'https://brandonchow1997.github.io/about/'
    browser.get(url)
    html = browser.page_source
    print('ZwZ' in html)


def better_selenium_headless():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options

    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
    chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
    chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
    chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
    chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # 添加代理 proxy
    # chrome_options.add_argument('--proxy-server=http://' + proxy)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://www.baidu.com')

    print('hao123' in driver.page_source)

    driver.close()  # 切记关闭浏览器，回收资源


if __name__ == '__main__':

    # ----第一种headless方法
    selenium_headless()
    print('=' * 20)
    # ----第二种headless方法
    better_selenium_headless()
