import pandas as pd
import matplotlib.pyplot as plt

df_imdb = pd.read_csv('Chengdongxia/practice4/imdb_top250.csv')
df_douban = pd.read_csv('Chengdongxia/practice4/douban_top250.csv')

# 假设IMDb的genre已通过"|"连接多个类型
df_imdb['genre'] = df_imdb['genre'].fillna('')
imdb_genres = df_imdb['genre'].str.split('|').explode().str.strip()
imdb_genre_counts = imdb_genres.value_counts()

# 假设后续您在data_retrieval.py中为豆瓣也提取了相同格式的genre字段
df_douban['genre'] = df_douban['genre'].fillna('')
douban_genres = df_douban['genre'].str.split('|').explode().str.strip()
douban_genre_counts = douban_genres.value_counts()

# 简单比较前10常见类型
top_imdb_genres = imdb_genre_counts.head(10)
top_douban_genres = douban_genre_counts.head(10)

plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
top_imdb_genres.plot(kind='bar', color='skyblue')
plt.title('Top 10 Genres in IMDb')
plt.ylabel('Count')

plt.subplot(1,2,2)
top_douban_genres.plot(kind='bar', color='salmon')
plt.title('Top 10 Genres in Douban')
plt.ylabel('Count')

plt.tight_layout()
plt.show()
