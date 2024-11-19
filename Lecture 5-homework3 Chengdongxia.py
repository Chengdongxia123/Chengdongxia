import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取 CSV 文件
df = pd.read_csv('plastic-waste.csv')

# 清理数据：去除缺失值
df_cleaned = df.dropna(subset=['continent', 'plastic_waste_per_cap', 'mismanaged_plastic_waste_per_cap'])

# 绘制散点图
plt.figure(figsize=(10, 6))
sns.scatterplot(x='plastic_waste_per_cap', y='mismanaged_plastic_waste_per_cap', hue='continent', data=df_cleaned, palette='deep')

# 设置图表标题和坐标轴标签
plt.title("Relationship between Plastic Waste Per Capita and Mismanaged Plastic Waste Per Capita")
plt.xlabel("Plastic Waste Per Capita (kg)")
plt.ylabel("Mismanaged Plastic Waste Per Capita (kg)")

# 显示图例
plt.legend(title='Continent')

# 显示图形
plt.show()