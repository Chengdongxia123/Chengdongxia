import pandas as pd

# 示例数据准备
partial_names_list = ["F. Kennedy", "Lennon", "Maynard Keynes", "Wayne"]
names = ["John " + name for name in partial_names_list]
print(names)  # 输出: ['John F. Kennedy', 'John Lennon', 'John Maynard Keynes', 'John Wayne']

# 假设 mean_n_c 和 mean_p_c 是已经定义好的 pandas Series
mean_n_c = pd.Series([10, 20, 30, 40])
mean_p_c = pd.Series([5, 15, 25, 35])

# 注意：这里使用 .loc[[1, 10]] 可能会引发 KeyError，因为索引只有 0, 1, 2, 3
# 假设我们想要选择索引为 1 和 3 的元素作为示例
selected_mean_n_c = mean_n_c.loc[[1, 3]]
selected_mean_p_c = mean_p_c.loc[[1, 3]]

# 创建新的 DataFrame
compare_grps = pd.DataFrame(
    [selected_mean_n_c, selected_mean_p_c],
    index=["Without punishment", "With punishment"],
)

# 重命名列以包含 'round'
compare_grps.columns = ["Round " + str(i) for i in compare_grps.columns]

# 交换列和索引变量，准备绘图
compare_grps = compare_grps.T

# 绘制柱状图
compare_grps.plot.bar(rot=0);