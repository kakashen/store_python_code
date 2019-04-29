import time
import requests
from bs4 import BeautifulSoup


def get_urls():
    base_url = 'https://rizhao.58.com/ershoufang/0/'

    response = requests.get(base_url)
    with open("base.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    # f = open('base.html', 'r', encoding='utf8')
    # string = f.read()
    soup = BeautifulSoup(response.text, 'html.parser')
    # print(soup.select('.house-list-wrap')[0].li['logr'])

    li = soup.select('.house-list-wrap')[0].find_all('li')

    hrefs = []
    for i in li:
        total = connect(i.select('.sum')[0].strings)  # 总价
        href = i.find('a')['href']  # url 地址
        # print(href)
        with open("href.csv", "a+", encoding="utf-8") as f:
            f.write(href + '\n')

        num = i['logr'].find('@postdate:') + 10  # 时间 ms
        post_date = i['logr'][num:num + 13]
        # print(i['logr'][num:num+13])

        data = {'link': href, 'sum': total, 'post_date': int(post_date) // 1000}
        ret = requests.post('http://www.xitou.online/api/python', data)

        if ret:
            hrefs.append(href)
            # spider(href)
            # print(href)
        time.sleep(1)

    for href in hrefs:
        spider(href)


def spider(url):
    # url = 'https://rizhao.58.com/ershoufang/37886495714975x.shtml'
    try:
        response = requests.get(url)
    except:
        return
    # print(response.text)
    with open("1.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    # f = open('1.html', 'r', encoding='utf8')
    # string = f.read()

    soup = BeautifulSoup(response.text, 'html.parser')

    tel_tag = soup.select('.phone-num')

    tel = tel_tag[0].string  # 手机号

    house_basic_item3 = soup.select('.house-basic-item3>li')

    community = trim(connect(house_basic_item3[0].strings))  # 小区名称

    main = soup.select('.area>.main')
    area = trim(main[0].string)  # 面积

    region = trim(connect(house_basic_item3[1].strings))  # 地区

    # db(tel, community, area, region)

    data = {'link': url, 'phone': tel, 'community': community, 'area': area, 'region': region}
    ret = requests.post('http://www.xitou.online/api/python', data)
    if ret:
        print(data)


def connect(string):
    """
    连接字符串
    :param string:
    :return:
    """
    strings = []
    for i in string:
        strings.append(i)
    return ''.join(strings)


def trim(string):
    """
    字符串去空格空行
    :param string:
    :return:
    """
    return string.replace(' ', '').replace('\n', '')


if __name__ == '__main__':
    get_urls()
