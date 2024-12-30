import pandas as pd
import matplotlib.pyplot as plt

df_imdb = pd.read_csv('Chengdongxia/practice4/imdb_top250.csv')
df_douban = pd.read_csv('Chengdongxia/practice4/douban_top250.csv')

df_imdb['rating'] = pd.to_numeric(df_imdb['rating'], errors='coerce')
df_douban['rating'] = pd.to_numeric(df_douban['rating'], errors='coerce')

avg_imdb = df_imdb['rating'].mean()
avg_douban = df_douban['rating'].mean()

print("IMDb平均评分：", avg_imdb)
print("豆瓣平均评分：", avg_douban)

platforms = ['IMDb', 'Douban']
avg_ratings = [avg_imdb, avg_douban]

plt.figure(figsize=(6,4))
plt.bar(platforms, avg_ratings, color=['skyblue', 'salmon'])
plt.title('Average Ratings Comparison')
plt.ylabel('Average Rating')
plt.ylim(0,10)
for i, v in enumerate(avg_ratings):
    plt.text(i, v + 0.1, f'{v:.2f}', ha='center', fontsize=12)
plt.show()
