import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 数据创建
np.random.seed(0)  # 设置随机种子以确保结果可重复
data_n = pd.DataFrame(np.random.randint(1, 15, size=(10, 5)), columns=['Period1', 'Period2', 'Period3', 'Period4', 'Period5'])
data_p = pd.DataFrame(np.random.randint(5, 20, size=(10, 5)), columns=['Period1', 'Period2', 'Period3', 'Period4', 'Period5'])

# 使用两种不同的方法计算平均值
# 第一种方法：使用内置的.mean()函数计算data_n除第一列外每列的平均值
mean_n_c = data_n.iloc[:, 1:].mean(axis=1)

# 第二种方法：使用.agg()函数和np.mean计算data_p除第一列外每列的平均值
mean_p_c = data_p.iloc[:, 1:].agg(np.mean, axis=1)

# 绘制平均贡献的直线图
fig, ax = plt.subplots()
mean_n_c.plot(ax=ax, label="Without punishment", marker='o')
mean_p_c.plot(ax=ax, label="With punishment", marker='x')
ax.set_title("Average Contributions to the Public Goods Game")
ax.set_ylabel("Average Contribution")
ax.set_xlabel("Periods (excluding the first)")
ax.legend()
plt.grid(True)
plt.show()

# 绘制第一和最后阶段平均贡献的列图
first_last_mean_n = mean_n_c.iloc[[0, -1]]
first_last_mean_p = mean_p_c.iloc[[0, -1]]

fig, ax = plt.subplots()
first_last_mean_n.plot(kind='bar', ax=ax, label="Without punishment", color='blue', alpha=0.7, width=0.4, position=0)
first_last_mean_p.plot(kind='bar', ax=ax, label="With punishment", color='orange', alpha=0.7, width=0.4, position=1)
ax.set_title("Average Contributions at the First and Last Periods")
ax.set_ylabel("Average Contribution")
ax.set_xticklabels(['First Period', 'Last Period'])
ax.legend()
plt.grid(True, axis='y')
plt.show()