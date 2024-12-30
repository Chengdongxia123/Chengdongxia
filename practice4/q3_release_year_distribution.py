import pandas as pd
import matplotlib.pyplot as plt

df_imdb = pd.read_csv('Chengdongxia/practice4/imdb_top250.csv')
df_douban = pd.read_csv('Chengdongxia/practice4/douban_top250.csv')

# 将年份转成数值类型，有些年份可能包含空字符串，需要清洗
df_imdb['year'] = pd.to_numeric(df_imdb['year'], errors='coerce')
df_douban['year'] = pd.to_numeric(df_douban['year'], errors='coerce')

# 绘制年份分布直方图对比
plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
df_imdb['year'].dropna().hist(bins=20, color='skyblue')
plt.title('IMDb Year Distribution')
plt.xlabel('Year')
plt.ylabel('Count')

plt.subplot(1,2,2)
df_douban['year'].dropna().hist(bins=20, color='salmon')
plt.title('Douban Year Distribution')
plt.xlabel('Year')
plt.ylabel('Count')

plt.tight_layout()
plt.show()
