# -*-coding:utf8-*-
import os
from urllib import request


def save():
    f = open("area.txt")

    for i in range(1, 4000):
        line = f.readline()
        filename = os.path.basename(line).replace('\n', '')
        path = r"images/" + filename
        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        request.install_opener(opener)
        try:
            request.urlretrieve(line, path)
            print(path)
            print('succeed:' + line)
        except Exception as e:
            print(str(e))
            print('fail:' + line)

    f.close()


if __name__ == "__main__":
    save()
