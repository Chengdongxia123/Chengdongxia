import pandas as pd
df = pd.read_csv('Chengdongxia/all-ages.csv')
df

# 按照专业分组，并把失业率从低到高升序排列
result = df.groupby(["Major"]).sum().sort_values(["Unemployment_rate"])
print(result)

import pandas as pd
df = pd.read_csv('Chengdongxia/recent-grads.csv')
df

# 按照专业分组，将女生占比从高到低降序排列
result = df.groupby(["Major"]).sum().sort_values(["ShareWomen"],ascending=False)
print(result)

import matplotlib.pyplot as plt
a=df['Median'].groupby(df['Major_category']).sum()
a.plot.bar()
plt.show()