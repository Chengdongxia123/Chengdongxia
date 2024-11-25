import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 数据字典
data = {
    "Copenhagen": [14.1, 14.1, 13.7, 12.9, 12.3, 11.7, 10.8, 10.6, 9.8, 5.3],
    "Dnipro": [11.0, 12.6, 12.1, 11.2, 11.3, 10.5, 9.5, 10.3, 9.0, 8.7],
    "Minsk": [12.8, 12.3, 12.6, 12.3, 11.8, 9.9, 9.9, 8.4, 8.3, 6.9],
}

# 创建 DataFrame
df = pd.DataFrame.from_dict(data)

# 计算每个城市的平均值和标准差
means = df.mean()
std_devs = df.std()

# 打印平均值和标准差
print("平均值:")
print(means)
print("\n标准差:")
print(std_devs)

# 绘制折线图
plt.figure(figsize=(10, 6))
for city in df.columns:
    plt.plot(df.index, df[city], label=city)

# 添加平均值和标准差到图中
for i, city in enumerate(df.columns):
    plt.text(len(df) - 1, df[city].iloc[-1], f"Avg: {means[i]:.2f}\nStd: {std_devs[i]:.2f}", 
             fontsize=10, verticalalignment='center')

# 图形设置
plt.title("多变量折线图及统计量")
plt.xlabel("时间点")
plt.ylabel("值")
plt.legend()
plt.grid(True)
plt.tight_layout()

# 显示图形
plt.show()