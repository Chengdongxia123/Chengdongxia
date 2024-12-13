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