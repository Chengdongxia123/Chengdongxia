import pandas as pd
import matplotlib.pyplot as plt

# 数据字典
data = {
    "Copenhagen": [14.1, 14.1, 13.7, 12.9, 12.3, 11.7, 10.8, 10.6, 9.8, 5.3],
    "Dniprop": [11.0, 12.6, 12.1, 11.2, 11.3, 10.5, 9.5, 10.3, 9.0, 8.7],
    "Minsk": [12.8, 12.3, 12.6, 12.3, 11.8, 9.9, 9.9, 8.4, 8.3, 6.9],
}

# 创建DataFrame
df = pd.DataFrame.from_dict(data)

# 绘制数据
fig, ax = plt.subplots()
df.plot(ax=ax, legend=True)  # 添加legend=True来显示图例

# 设置图表标题和轴标签
ax.set_title("Average contributions to the public goods game: Without punishment")
ax.set_ylabel("Average contribution")
ax.set_xlabel("Round")

# 显示图表
plt.show()