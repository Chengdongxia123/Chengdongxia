import pandas as pd
import matplotlib.pyplot as plt

# 假设的平均值数据（请用实际数据替换）
# 这里我们假设有10个周期的平均值，无惩罚和有惩罚条件下
mean_n_c = [12, 15, 18, 21, 24, 27, 30, 33, 36, 39]  # 无惩罚条件下的平均值
mean_p_c = [11, 14, 17, 20, 23, 26, 29, 32, 35, 40]  # 有惩罚条件下的平均值

# 将数据转换为Pandas Series，以便更容易地处理
mean_n_c_series = pd.Series(mean_n_c, index=range(1, 11))
mean_p_c_series = pd.Series(mean_p_c, index=range(1, 11))

# 提取第1期和第10期的数据
data_to_compare = pd.DataFrame({
    'Without Punishment': mean_n_c_series[[1, 10]],
    'With Punishment': mean_p_c_series[[1, 10]]
})

# 绘制列图
data_to_compare.plot(kind='bar', rot=0)
plt.title('Contributions in the Public Goods Game')
plt.xlabel('Period')
plt.ylabel('Average Contribution (€)')
plt.legend(title='Condition')
plt.show()