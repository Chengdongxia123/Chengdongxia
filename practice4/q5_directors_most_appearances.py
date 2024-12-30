import pandas as pd
import matplotlib.pyplot as plt

df_imdb = pd.read_csv('Chengdongxia/practice4/imdb_top250.csv')
df_douban = pd.read_csv('Chengdongxia/practice4/douban_top250.csv')

# 假设两个DataFrame的director字段类似IMDb，使用"|"分隔多个导演
df_imdb['director'] = df_imdb['director'].fillna('')
imdb_directors = df_imdb['director'].str.split('|').explode().str.strip()
imdb_director_counts = imdb_directors.value_counts()

# 对豆瓣数据执行同样操作 (请先在data_retrieval.py中实现导演提取)
df_douban['director'] = df_douban['director'].fillna('')
douban_directors = df_douban['director'].str.split('|').explode().str.strip()
douban_director_counts = douban_directors.value_counts()

# 绘制各平台导演出现次数Top10
top_imdb_directors = imdb_director_counts.head(10)
top_douban_directors = douban_director_counts.head(10)

plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
top_imdb_directors.plot(kind='bar', color='skyblue')
plt.title('Top 10 Directors in IMDb Top 250')
plt.ylabel('Count')

plt.subplot(1,2,2)
top_douban_directors.plot(kind='bar', color='salmon')
plt.title('Top 10 Directors in Douban Top 250')
plt.ylabel('Count')

plt.tight_layout()
plt.show()
