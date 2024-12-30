import pandas as pd

df_imdb = pd.read_csv('Chengdongxia/practice4/imdb_top250.csv')
df_douban = pd.read_csv('Chengdongxia/practice4/douban_top250.csv')

df_imdb_titles = set(df_imdb['title'].dropna().str.strip())
df_douban_titles = set(df_douban['en_title'].dropna().str.strip())

common_titles = df_imdb_titles.intersection(df_douban_titles)

print("同时出现在IMDb和豆瓣Top 250中的电影（英文标题匹配）：")
if common_titles:
    for title in sorted(common_titles):
        print(title)
else:
    print("没有同时出现的电影。")
