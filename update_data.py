import requests
import spider_2
import json
import time


def update_data():
    base_url = 'http://www.xitou.online/api/get_link'

    response = requests.request('get', url=base_url)
    links = response.text
    j = json.loads(links)
    for i in j:
        link = i['link']
        spider_2.spider(link)
        time.sleep(1)


if __name__ == '__main__':
    update_data()
