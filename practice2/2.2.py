import pandas as pd
import matplotlib.pyplot as plt

# 读取Excel文件中的数据
data_np = pd.read_excel(
    "Chengdongxia/practice2/doing-economics-datafile-working-in-excel-project-2.xlsx",
    usecols="A:Q",
    header=1,
    index_col="Period"
)

# 提取A2:Q12的数据到data_n
data_n = data_np.iloc[:11, :].copy()  # 注意索引是从0开始的，且包含结束索引，所以使用[:11]

# 提取A16:Q26的数据到data_p
data_p = data_np.iloc[15:26, :].copy()  # 同样注意索引范围，使用[15:26]

# 绘制图形
plt.figure(figsize=(10, 6))

# 绘制data_n的折线图
plt.subplot(2, 1, 1)
data_n.plot(kind='line', title='A2:Q12 Data', grid=True)
plt.xlabel('Period')
plt.ylabel('Values')

# 绘制data_p的折线图
plt.subplot(2, 1, 2)
data_p.plot(kind='line', title='A16:Q26 Data', grid=True)
plt.xlabel('Period')
plt.ylabel('Values')

# 调整子图布局并显示图形
plt.tight_layout()
plt.show()