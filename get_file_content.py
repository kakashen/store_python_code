import re
import html
import json


def one():
    f = open('weixin_history.html', 'r', encoding='utf8')
    string = f.read()
    rex = "msgList = '({.*?})'"
    pattern = re.compile(pattern=rex, flags=re.S)
    match = pattern.search(string)
    if match:
        data = match.group(1)
        data = html.unescape(data)
        data = json.loads(data)
        articles = data.get("list")
        for item in articles:
            print(item)
        return articles

    f.close()

if __name__ == '__main__':
    one()
