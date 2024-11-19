import pandas as pd
import matplotlib.pyplot as plt

# 下载NASA的北半球温度数据
url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/NH.Ts+dSST.csv"

# 尝试下载数据并处理可能出现的错误
try:
    df = pd.read_csv(url, skiprows=1, na_values="***")
except Exception as e:
    print(f"Error downloading or reading the data: {e}")
    df = None

# 检查数据是否成功加载
if df is not None:
    # 设置年份为索引
    df = df.set_index("Year")

    # 绘制1月份的温度异常线图
    def plot_monthly_temperature(month):
        try:
            fig, ax = plt.subplots()
            ax.axhline(0, color="orange")
            ax.annotate("1951—1980 average", xy=(0.66, -0.2), xycoords=("figure fraction", "data"))
            df[month].plot(ax=ax)
            ax.set_title(f"Average temperature anomaly in {month} \n in the northern hemisphere (1880—{df.index.max()})")
            ax.set_ylabel("Annual temperature anomalies")
            plt.show()
        except KeyError:
            print(f"No data for month {month}")

    # 绘制季节平均温度异常线图
    def plot_seasonal_temperature(season):
        try:
            fig, ax = plt.subplots()
            ax.axhline(0, color="orange")
            ax.annotate("1951—1980 average", xy=(0.66, -0.2), xycoords=("figure fraction", "data"))
            df[season].plot(ax=ax)
            ax.set_title(f"Average temperature anomaly in {season} \n in the northern hemisphere (1880—{df.index.max()})")
            ax.set_ylabel("Annual temperature anomalies")
            plt.show()
        except KeyError:
            print(f"No data for season {season}")

    # 绘制年度平均温度异常线图
    def plot_annual_temperature():
        try:
            fig, ax = plt.subplots()
            ax.axhline(0, color="orange")
            ax.annotate("1951—1980 average", xy=(0.66, -0.2), xycoords=("figure fraction", "data"))
            df["J-D"].plot(ax=ax)
            ax.set_title(f"Average annual temperature anomaly \n in the northern hemisphere (1880—{df.index.max()})")
            ax.set_ylabel("Annual temperature anomalies")
            plt.show()
        except KeyError:
            print("No annual data available")

    # 绘制图表
    plot_monthly_temperature("Jan")
    plot_seasonal_temperature("DJF")  # 冬季
    plot_seasonal_temperature("MAM")  # 春季
    plot_seasonal_temperature("JJA")  # 夏季
    plot_seasonal_temperature("SON")  # 秋季
    plot_annual_temperature()
else:
    print("Failed to load data. Please check your internet connection and try again.")