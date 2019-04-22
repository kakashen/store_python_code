import matplotlib.pyplot as plt
import pandas as pd
from pymongo import MongoClient
from wordcloud import WordCloud
import jieba

display_columns = ["name"]
# 连接 mongodb
c = MongoClient()
cursor = c.logs['org'].find()
df = pd.DataFrame(list(cursor))

# 删除 "_id"列
df = df.drop("_id", axis=1)
# 重新设置列的顺序
df = df.reindex(columns=display_columns)
# 将p_date的数据类型从timestamp 转换成 datetime
df.head()

words = []
for i in df.name:
    seg_list = jieba.cut(i, cut_all=False)
    words.append(" ".join(seg_list))
wordcloud = WordCloud(font_path='/Library/Fonts/simsun.ttc',
                      background_color="white",
                      max_words=80, ).generate(" ".join(words))
plt.figure(figsize=(9, 6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
