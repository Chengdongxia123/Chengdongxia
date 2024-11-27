import pandas as pd
import matplotlib.pyplot as plt

try:
    data_np = pd.read_excel(
        "Chengdongxia/practice2/doing-economics-datafile-working-in-excel-project-2.xlsx",
        usecols="A:Q",
        header=1,
        index_col="Period"
    )
except FileNotFoundError:
    print()
    exit()
except Exception as e:
    print( )
    exit()

data_n = data_np.iloc[:10, :].copy()
data_p = data_np.iloc[14:24, :].copy()

try:
    data_n = data_n.astype(float)
    data_p = data_p.astype(float)
except ValueError:
    print()
    exit()

avg_contributions_n = data_n.mean(axis=1)
avg_contributions_p = data_p.mean(axis=1)

plt.figure(figsize=(10, 6))
plt.plot(avg_contributions_n, label='No Punishment', marker='o')
plt.plot(avg_contributions_p, label='With Punishment', marker='x')
plt.xlabel('Period')
plt.ylabel('Average Contributions')
plt.title('Effect of Punishment on Average Contributions')
plt.legend()
plt.grid(True)
plt.show()