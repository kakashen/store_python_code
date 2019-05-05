# -*-coding:utf8-*-
import datetime
from urllib import request
import re


def save():
    line = 'http://miabyss.com/images/top02/visual04.jpg'
    path = r"images/visual04.jpg"
    try:
        request.urlretrieve(line, path)
        print('succeed:' + line)
    except:
        print('fail:' + line)


if __name__ == "__main__":
    save()
