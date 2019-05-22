# -*-coding:utf8-*-
import os
from urllib import request


def save(line):
    filename = os.path.basename(line)

    path = r"images/" + filename

    opener = request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    request.install_opener(opener)
    try:
        request.urlretrieve(line, path)
        print('succeed:' + line)
        return 1
    except:
        return 0
