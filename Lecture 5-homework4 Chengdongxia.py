import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取 CSV 文件
df = pd.read_csv('plastic-waste.csv')

# 清理数据：去除缺失值
df_cleaned = df.dropna(subset=['total_pop', 'coastal_pop', 'plastic_waste_per_cap'])

# 创建两个子图
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# 人均塑料垃圾与总人口的关系
sns.scatterplot(x='total_pop', y='plastic_waste_per_cap', data=df_cleaned, ax=axes[0])
axes[0].set_title("Plastic Waste Per Capita vs. Total Population")
axes[0].set_xlabel("Total Population")
axes[0].set_ylabel("Plastic Waste Per Capita (kg)")

# 人均塑料垃圾与沿海人口的关系
sns.scatterplot(x='coastal_pop', y='plastic_waste_per_cap', data=df_cleaned, ax=axes[1])
axes[1].set_title("Plastic Waste Per Capita vs. Coastal Population")
axes[1].set_xlabel("Coastal Population")
axes[1].set_ylabel("Plastic Waste Per Capita (kg)")

# 显示图形
plt.tight_layout()
plt.show()