# coding=utf-8
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import time
import socket


def stock():
    socket.setdefaulttimeout(20)  # 设置socket层的超时时间为20秒
    header = {'User-Agent': 'Mozilla/5.0'}
    url = []
    print('输入需要查询的基金号，按Q结束\n')
    while True:
        n = input()
        if n == 'Q':
            break
        elif n:
            t = 'http://fund.eastmoney.com/{0}.html?spm-search'.format(n)
            url.append(t)
        else:
            print('输入错误')
    for i in url:
        request = urllib.request.Request(i, headers=header)
        try:
            response = urllib.request.urlopen(request)
            soup = BeautifulSoup(response, 'html.parser')
            title = soup.find('div', attrs={'class': 'fundDetail-tit'})
            rate = soup.find('span', attrs={'id': 'gz_gszzl'})
            print(title.text, rate.text)
            response.close()  # 注意关闭response
        except urllib.error.URLError as e:
            print(e.reason)
        time.sleep(5)  # 自定义


if __name__ == '__main__':
    stock()
