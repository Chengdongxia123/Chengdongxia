import pandas as pd
import matplotlib.pyplot as plt

# 假设data_n和data_p是已经加载好的DataFrame
# 这里为了示例，我们创建一些模拟数据
data_n = pd.DataFrame({
    'Period1': [10, 12, 11, 9, 10, 11, 10, 12, 13, 11],
    'Period2': [11, 13, 12, 10, 11, 12, 11, 13, 14, 12],
    # 添加更多列以模拟实际数据
    # ...
}, index=range(1, 11))

data_p = pd.DataFrame({
    'Period1': [15, 17, 16, 14, 15, 16, 15, 17, 18, 16],
    'Period2': [16, 18, 17, 15, 16, 17, 16, 18, 19, 17],
    # 添加更多列以模拟实际数据
    # ...
}, index=range(1, 11))

# 计算标准差、方差和均值
n_c = data_n.agg(["std", "var", "mean"], axis=1)
p_c = data_p.agg(["std", "var", "mean"], axis=1)

# 绘制没有惩罚的贡献图表
fig, ax = plt.subplots()
n_c["mean"].plot(ax=ax, label="mean")
# mean + 2 standard deviations
(n_c["mean"] + 2 * n_c["std"]).plot(ax=ax, ylim=(0, None), color="red", label="±2 s.d.")
# mean - 2 standard deviations
(n_c["mean"] - 2 * n_c["std"]).plot(ax=ax, ylim=(0, None), color="red", label="")
for i in range(len(data_n.columns)):
    ax.scatter(x=data_n.index, y=data_n.iloc[:, i], color="k", alpha=0.3)
ax.legend()
ax.set_ylabel("Average contribution")
ax.set_title("Contribution to public goods game without punishment")
plt.show()

# 绘制有惩罚的贡献图表
fig, ax = plt.subplots()
p_c["mean"].plot(ax=ax, label="mean")
# mean + 2 sd
(p_c["mean"] + 2 * p_c["std"]).plot(ax=ax, ylim=(0, None), color="red", label="±2 s.d.")
# mean - 2 sd
(p_c["mean"] - 2 * p_c["std"]).plot(ax=ax, ylim=(0, None), color="red", label="")
for i in range(len(data_p.columns)):
    ax.scatter(x=data_p.index, y=data_p.iloc[:, i], color="k", alpha=0.3)
ax.legend()
ax.set_ylabel("Average contribution")
ax.set_title("Contribution to public goods game with punishment")
plt.show()