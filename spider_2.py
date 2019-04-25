import requests
from bs4 import BeautifulSoup


def spider():
    # url = 'https://rizhao.58.com/ershoufang/37886495714975x.shtml'
    # response = requests.get(url)
    # # print(response.text)
    # with open("1.html", "w", encoding="utf-8") as f:
    #     f.write(response.text)

    f = open('1.html', 'r', encoding='utf8')
    string = f.read()

    soup = BeautifulSoup(string, 'html.parser')

    tel_tag = soup.select('.phone-num')

    tel = tel_tag[0].string  # 手机号

    house_basic_item3 = soup.select('.house-basic-item3>li')

    str1 = []
    for str in house_basic_item3[0].strings:
        print(str)


if __name__ == '__main__':
    spider()
