import requests
import time


def begin():
    while True:
        # # Request URL: http://mdfm.eastmoney.com/EM_UBG_MinuteApi/Js/Get?dtype=25&style=tail&check=st&dtformat=HH:mm:ss&cb=jQuery18309738854033117121_1557975154503&id=0024562&num=10&_=1557975323439
        t = time.time() * 1000

        url = 'http://mdfm.eastmoney.com/EM_UBG_MinuteApi/Js/Get?dtype=25&style=tail&check=st&dtformat=HH:mm:ss&cb=jQuery18309738854033117121_1557975154503&id=0024562&num=1&_={0}'.format(
            t)

        data = requests.get(url)
        text = data.text
        # print(text)
        n = text.find('"data":')
        # print(n)
        # print(type(n))
        print(text[n + 9: n + 34])
        time.sleep(20)


if __name__ == '__main__':
    begin()
