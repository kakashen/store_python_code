import requests


def crawl():
    url = 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA5OTA0NDIyMQ==&scene=126&bizpsid=1555554013&sessionid=1555554013&subscene=0&devicetype=iOS12.0&version=1700032a&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=IXl5s1mgojVBWmx8jk8H8lLEjyy2kzl5mrquxFDC6ky%2BY1LUUtXzJP4Mwu4xwPkX&wx_header=1'
    headers = """
    Host: mp.weixin.qq.com
Cookie: devicetype=iOS12.0; lang=zh_CN; pass_ticket=IXl5s1mgojVBWmx8jk8H8lLEjyy2kzl5mrquxFDC6ky+Y1LUUtXzJP4Mwu4xwPkX; version=1700032a; wap_sid2=CNWNrsAFElwxMnFtbXU5ZU5NcEpMQ0E2RTFrcHEzVXZmdmJnS3dfZldZai1TVHNiems2NVk0S3FjWktlOHpFNWdadmJOSmxKX1o0M05WU0NkcFpEZHo4ZmtlRkhKTzBEQUFBfjCszN/lBTgNQJVO; wxuin=1477150421; pgv_pvid=6829881288; ua_id=YMUqQzCvyTdg7RheAAAAAHHsVKSD95pt0DF9He8rDyQ=; _scan_has_moon=1; eas_sid=K1z5X4E3G2z0d7K3P6b5Z4j1I7; sd_cookie_crttime=1542384392587; sd_userid=82761542384392587
X-WECHAT-KEY: 446974b7a1ec3beb835f024299fdde54e66a4d6571e7fa428c6e3c99f902403ef12fe89fa7a7c8cc583822fd385789be811e1b14048988bc649da34ac34ec6962896be31cae967069b0ba4bb50995ce4
X-WECHAT-UIN: MTQ3NzE1MDQyMQ%3D%3D
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN
Accept-Language: zh-cn
Accept-Encoding: br, gzip, deflate
Connection: keep-alive
        """

    headers_to_dict(headers)

    # response = requests.get(url, headers=headers, verify=False)
    # print(response.text)
    # with open("weixin_history.html", "w", encoding="utf-8") as f:
    #    f.write(response.text)


def headers_to_dict(headers):
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            print(h)
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers



if __name__ == '__main__':
    crawl()
