from bs4 import BeautifulSoup
import requests

def post_date():
    f = open('base.html', 'r', encoding='utf8')
    string = f.read()

    soup = BeautifulSoup(string, 'html.parser')
    li = soup.select('.house-list-wrap')[0].find_all('li')
    for i in li:
        href = i.find('a')['href']  # url 地址

        with open('logr.csv', 'a+', encoding="utf-8") as l:
            l.write(i['logr'] + '\n')
        num = i['logr'].find('@postdate:') + 10  # 时间 ms

        post_date = i['logr'][num:num+13]
        # print(post_date)

        data = {'link': href, 'post_date': int(post_date) // 1000}
        ret = requests.post('http://www.xitou.online/api/python', data)
        print(ret)
if __name__ == '__main__':
    post_date()
