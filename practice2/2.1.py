import matplotlib.pyplot as plt

# 数据准备
periods = list(range(1, 11))  # 周期从1到10
average_contributions = [50.0, 14.7, 28.8, 27.2, 35.2, 40.2, 46.2, 42.3, 35.9, 42.7]  # 平均贡献值

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制折线图
plt.plot(periods, average_contributions, marker='o', linestyle='-', color='b')

# 添加图表标题和坐标轴标签
plt.title('游戏过程中平均贡献的变化')
plt.xlabel('周期 (1-10)')  # 横坐标名称
plt.ylabel('平均贡献 (€)')  # 竖坐标名称

# 显示网格
plt.grid(True)

# 展示图形
plt.show()