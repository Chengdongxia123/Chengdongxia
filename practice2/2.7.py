funcs_to_apply = [range_function, "max", "min", "std", "mean"]
summ_p = data_p.apply(funcs_to_apply, axis=1).rename(columns={"<lambda>": "range"})
summ_n = data_n.apply(funcs_to_apply, axis=1).rename(columns={"<lambda>": "range"})
summ_n.loc[[1, 10], :].round(2)
range	max	min	std	mean
Period					
1	6.14	14.10	7.96	2.02	10.58
10	7.38	8.68	1.30	2.19	4.38
summ_p.loc[[1, 10], :].round(2)
range	max	min	std	mean
Period					
1	10.20	16.02	5.82	3.21	10.64
10	11.31	17.51	6.20	3.90	12.87
import pingouin as pg
pg.ttest(x=data_n.iloc[0, :], y=data_p.iloc[0, :])
T	dof	alternative	p-val	CI95%	cohen-d	BF10	power
T-test	-0.063782	30	two-sided	0.949567	[-2.0, 1.87]	0.02255	0.337	0.050437
pg.ttest(x=data_n.iloc[0, :], y=data_p.iloc[0, :], paired=True)
T	dof	alternative	p-val	CI95%	cohen-d	BF10	power
T-test	-0.149959	15	two-sided	0.882795	[-0.92, 0.8]	0.02255	0.258	0.05082
# 创建一个包含索引1到11的新索引
new_index = range(1, 12)
# 重新索引DataFrame，包括不存在的索引10
reindexed_summ_n = summ_n.reindex(new_index)
# 现在您可以安全地访问索引10（尽管它的值将是NaN）
print(reindexed_summ_n.loc[10, :].round(2))
range    7.38
max      8.68
min      1.30
std      2.19
mean     4.38
Name: 10, dtype: float64