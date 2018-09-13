# *-* encoding = utf-8

import requests
import re
from multiprocessing.dummy import Pool as ThreadPool

import redis

r = redis.Redis(host='192.168.2.119', port=6379, db=0, charset='utf-8')


def main(num=10):
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Host': 'www.xicidaili.com '
    }
    proxies = []
    for i in range(1, num):
        url = 'http://www.xicidaili.com/nt/' + str(i)

        response = requests.get(url, headers=header)

        proxies.extend(getip(response.text))

    write(proxies)


def main_2(num=10000):
    url = 'http://www.66ip.cn/mo.php?tqsl=' + str(num)
    try:
        html = requests.get(url).text
        proxies = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d+)', html)
    except:
        pass

    write(proxies)


def getip(page):
    ip_pattern = re.compile('>(\d+.\d+.\d+.\d+)<')
    host_pattern = re.compile('>(\d+)<')

    proxies = []

    ips = re.findall(ip_pattern, page)
    hosts = re.findall(host_pattern, page)

    for i in range(0, len(ips)):
        proxy = ips[i] + ':' + hosts[i]
        proxies.append(proxy)

    return proxies


def check(proxy):
    proxy = proxy.strip()
    url = 'http://ip.chinaz.com/getip.aspx'  # 'http://2018.ip138.com/ic.asp'
    timeout = 5
    try:
        response = requests.get(url, proxies={'http': proxy}, timeout=timeout)
        print('检测：' + proxy)
        if re.sub(":\d+", '', proxy) in response.text:
            print('\t合格:\t' + response.text)
            r.sadd('ip', proxy)
            return proxy
    except:
        pass

    return None


def checkall(proxies):
    proxies_right = []
    proc = []
    pool = ThreadPool(processes=10)
    for proxy in proxies:
        proc.append(pool.apply_async(check, (proxy,)))

    pool.close()
    pool.join()

    print('num: ' + str(len(proc)))
    for p in proc:
        if p.get():
            proxies_right.append(p.get())
    return proxies_right


def write(proxies):
    proxies = checkall(proxies)

    with open('ip.txt', 'r') as f:
        pproxies = f.readlines()
        proxies.extend(checkall(pproxies))

    # xie ru shu ju ku
    r.delete('ip')
    with open('ip.txt', 'w', encoding='utf-8') as f:
        for p in proxies:
            f.write(p)
            f.write('\n')


if __name__ == '__main__':
    # main()
    main_2(10000)