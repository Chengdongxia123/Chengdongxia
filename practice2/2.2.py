import matplotlib.pyplot as plt
import pandas as pd

# 假设数据
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [23, 45, 56, 78]
}
df = pd.DataFrame(data)

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Values'], color='skyblue')
plt.title('Category vs. Values')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()


import matplotlib.pyplot as plt
import pandas as pd

# 假设数据
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': [100, 150, 200, 250, 300]
}
df = pd.DataFrame(data)

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(df['Month'], df['Sales'], marker='o', linestyle='-', color='b')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt

# 假设数据
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # 突出显示第一个切片

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart Example')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

import matplotlib.pyplot as plt
import pandas as pd

# 假设数据
data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 3, 5, 7, 11]
}
df = pd.DataFrame(data)

# 绘制散点图
plt.figure(figsize=(10, 6))
plt.scatter(df['X'], df['Y'], color='red', marker='x')
plt.title('Scatter Plot of X vs. Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# 假设数据
np.random.seed(0)
data = np.random.rand(10, 12)
dataframe = pd.DataFrame(data, columns=[f'Feature {i}' for i in range(1, 13)])

# 绘制热力图
plt.figure(figsize=(12, 8))
sns.heatmap(dataframe, annot=True, cmap='coolwarm')
plt.title('Heatmap Example')
plt.show()


