# -*-coding:utf8-*-
import datetime
import os
from urllib import request
import re


def save():
    f = open("urls_drawings.txt")
    line = f.readline()
    print(line)
    for i in range(1, 1000):

        filename = os.path.basename(line)
        path = r"images/" + filename
        try:
            request.urlretrieve(line, path)
            line = f.readline()
            print('succeed:' + str(i))
        except:
            line = f.readline()
            print('fail:' + str(i))

    f.close()


if __name__ == "__main__":
    save()
