# -*-coding:utf8-*-
import os
import time
from urllib import request


def save():
    f = open("urls_hentai.txt")

    for i in range(1, 10):
        line = f.readline()
        filename = os.path.basename(line).replace('\n', '')
        path = r"images/" + filename
        opener = request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        # 220.180.156.53:8060
        request.install_opener(opener)

        try:
            request.urlretrieve(line, path)
            print(path)
            print('succeed:' + line)

        except Exception as e:
            time.sleep(1)
            print(str(e))
            print('fail:' + line)

    f.close()


if __name__ == "__main__":
    save()
