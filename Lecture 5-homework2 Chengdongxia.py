import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 读取 CSV 文件
df = pd.read_csv('plastic-waste.csv')

# 清理数据：去除缺失值
df_cleaned = df.dropna(subset=['continent', 'plastic_waste_per_cap'])

# 设置图形风格
sns.set(style="whitegrid")

# 创建 FacetGrid，按 'continent' 分面
g = sns.FacetGrid(df_cleaned, col='continent', col_wrap=3, height=4, sharey=False)
g.map(sns.violinplot, 'plastic_waste_per_cap', color='blue')

# 设置图表标题和坐标轴标签
g.set_titles("{col_name} Plastic Waste Per Capita Violin Plot")
g.set_axis_labels("Plastic Waste Per Capita (kg)", "Density")
g.fig.suptitle("Violin Plot of Plastic Waste Per Capita by Continent", fontsize=16)
g.tight_layout(pad=2)

# 显示图形
plt.show()