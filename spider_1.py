from urllib.request import urlopen

from bs4 import BeautifulSoup


def spider():
    html = urlopen("https://rizhao.58.com/ershoufang/37886495714975x.shtml")

    
    soup = BeautifulSoup(html, "html.parser")
    print(soup.meta)


if __name__ == '__main__':
    spider()
