import json
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 获取IMDb Top 250数据
url_imdb = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
headers_imdb = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/91.0.4472.124 Safari/537.36")
}
response_imdb = requests.get(url_imdb, headers=headers_imdb)
soup_imdb = BeautifulSoup(response_imdb.text, "html.parser")
script_imdb = soup_imdb.select_one("script[type='application/ld+json']")
data_imdb = json.loads(script_imdb.text)

imdb_movies = []
for movie in data_imdb["itemListElement"]:
    item = movie["item"]
    rating = None
    if "aggregateRating" in item and "ratingValue" in item["aggregateRating"]:
        rating = item["aggregateRating"]["ratingValue"]
    # IMDb的结构化数据中也可以获取到上映年份、导演和类型
    # 这里简单示范，只获取必须数据，后续需要可拓展。
    # item中包含datePublished、genre、director等字段
    imdb_movies.append({
        "title": item.get("name"),    # 英文片名
        "rating": rating,
        "year": item.get("datePublished", ""),
        "genre": "|".join(item.get("genre", [])) if "genre" in item else "",
        "director": "|".join([d["name"] for d in item.get("director", [])]) if "director" in item else ""
    })
df_imdb = pd.DataFrame(imdb_movies)

df_imdb.to_csv('imdb_top250.csv', index=False)

# 获取豆瓣Top 250数据
movies_douban = []
headers_douban = {
    "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/91.0.4472.124 Safari/537.36")
}

for start in range(0, 250, 25):
    url_douban = f"https://movie.douban.com/top250?start={start}"
    response_douban = requests.get(url_douban, headers=headers_douban)
    soup_douban = BeautifulSoup(response_douban.text, 'html.parser')
    for item in soup_douban.select('.item'):
        title_tags = item.select('.title')
        if len(title_tags) > 1:
            cn_title = title_tags[0].text.strip()
            en_title = title_tags[1].text.strip().replace('\xa0/\xa0', '')
        else:
            cn_title = title_tags[0].text.strip()
            en_title = ''
        rating = item.select('.rating_num')[0].text
        info = item.select('.bd p')[0].text.strip().split('\n')
        info = [line.strip() for line in info if line.strip() != '']
        year_line = info[1] if len(info) > 1 else ''
        year = year_line.split('/')[0].strip() if '/' in year_line else year_line

        # 如果需要导演、类型，需要进一步解析info等文本或单独页面请求。
        # 此处省略，可在后续根据需求添加代码提取相关信息。
        # 导演、类型的提取方式参考之前的说明，需要正则或文本切分。

        movies_douban.append({
            'cn_title': cn_title,
            'en_title': en_title,
            'rating': rating,
            'year': year,
            # 'genre': ...   #后续可加入
            # 'director': ... #后续可加入
        })

df_douban = pd.DataFrame(movies_douban)
df_douban.to_csv('douban_top250.csv', index=False)

print("数据获取完成！请运行各分析文件。")
