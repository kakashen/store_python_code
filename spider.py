# -*-coding:utf8-*-

from urllib import request
import re


def save():
    f = open("urls_drawings.txt")
    line = f.readline()
    for i in range(1, 1000):

        path = r"image/drawings" + str(i) + ".jpg"
        try:
            data = request.urlretrieve(line, path)
            line = f.readline()
            print('succeed:' + str(i))
        except:
            line = f.readline()
            print('fail:' + str(i))
            continue

    f.close()


if __name__ == "__main__":
    save()
