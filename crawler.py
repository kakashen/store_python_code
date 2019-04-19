import requests


def crawl():
    url = 'https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MzA5OTA0NDIyMQ==&scene=126&bizpsid=1555554013&sessionid=1555554013&subscene=0&devicetype=iOS12.0&version=1700032a&lang=zh_CN&nettype=WIFI&a8scene=0&fontScale=100&pass_ticket=IXl5s1mgojVBWmx8jk8H8lLEjyy2kzl5mrquxFDC6ky%2BY1LUUtXzJP4Mwu4xwPkX&wx_header=1'
    headers = """Host: mp.weixin.qq.com
Cookie: wxtokenkey=777; devicetype=iOS12.0; lang=zh_CN; pass_ticket=IXl5s1mgojVBWmx8jk8H8lLEjyy2kzl5mrquxFDC6ky+Y1LUUtXzJP4Mwu4xwPkX; rewardsn=; version=1700032a; wap_sid2=CNWNrsAFElxFTzQyMDRnNmROQmpaUHlQMmdXS01SaDA5LTh2czhzbEtFbERxaWU5a2R1MkxQeTBuSVE3ZDhZZzFIU2JtWmIxMGt2VTgyWXo1eVZ3eXNFdUx0Vy1kdTBEQUFBfjCP09/lBTgNQAE=; wxuin=1477150421; pgv_pvid=6829881288; ua_id=YMUqQzCvyTdg7RheAAAAAHHsVKSD95pt0DF9He8rDyQ=; _scan_has_moon=1; eas_sid=K1z5X4E3G2z0d7K3P6b5Z4j1I7; sd_cookie_crttime=1542384392587; sd_userid=82761542384392587
X-WECHAT-KEY: bf6390d363657f3f40f35efee66366fc711bf97668a907837f610d295cd8bbb5c8cdf3bc2703e11a2997dd2be3255b8d424e96a0bd0ffff3ff35593413cb1d836ea1f998b884c8882c2f9105bb664e8b
X-WECHAT-UIN: MTQ3NzE1MDQyMQ%3D%3D
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 12_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16A366 MicroMessenger/7.0.3(0x17000321) NetType/WIFI Language/zh_CN
Accept-Language: zh-cn
Accept-Encoding: br, gzip, deflate
Connection: keep-alive"""

    headers = headers_to_dict(headers)

    response = requests.get(url, headers=headers, verify=False)
    print(response.text)
    with open("weixin_history.html", "w", encoding="utf-8") as f:
        f.write(response.text)

    extract_data(response.text)


def headers_to_dict(headers):
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers


def extract_data(html_content):
    """
    从html页面中提取历史文章数据
    :param html_content 页面源代码
    :return: 历史文章列表
    """
    import re
    import html
    import json

    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(html_content)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles


if __name__ == '__main__':
    crawl()
