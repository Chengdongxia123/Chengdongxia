import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 假设data_p已经给出（您之前提供的输出可以作为参考）
# 这里我们创建一个类似的DataFrame来模拟data_p
np.random.seed(0)  # 设置随机种子以便复现
data_p = pd.DataFrame(np.random.rand(10, 5) * 10, columns=['A', 'B', 'C', 'D', 'E'])
data_p['Period'] = range(1, 11)
data_p.set_index('Period', inplace=True)

# 假设data_n与data_p结构相同，但数据不同
# 这里我们创建另一个DataFrame来模拟data_n
data_n = pd.DataFrame(np.random.rand(10, 5) * 10, columns=['A', 'B', 'C', 'D', 'E'])
data_n['Period'] = range(1, 11)
data_n.set_index('Period', inplace=True)

# 定义一个lambda函数来计算范围
range_function = lambda x: x.max() - x.min()

# 应用这个函数到data_p和data_n的每一行
range_p = data_p.apply(range_function, axis=1)
range_n = data_n.apply(range_function, axis=1)

# 绘图
fig, ax = plt.subplots()
range_p.plot(ax=ax, label="With punishment", marker='o')
range_n.plot(ax=ax, label="Without punishment", marker='x')
ax.set_ylim(0, None)
ax.legend()
ax.set_title("Range of contributions to the public goods game")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()