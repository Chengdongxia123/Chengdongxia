import pandas as pd

# 请确保文件路径是正确的，这里只是一个示例路径
file_path = "Chengdongxia/practice2/doing-economics-datafile-working-in-excel-project-2.xlsx"

# 尝试读取Excel文件
try:
    data_np = pd.read_excel(
        file_path,
        usecols="A:Q",
        header=1,
        index_col="Period",
        engine='openpyxl'  # 明确指定使用openpyxl引擎来读取xlsx文件
    )
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found. Please check the file path.")
    exit(1)
except pd.errors.EmptyDataError:
    print(f"Error: No data found in the file {file_path}. Please check if the file is empty or corrupted.")
    exit(1)
except pd.errors.ParserError:
    print(f"Error: There was an error parsing the file {file_path}. Please check the file format and content.")
    exit(1)
except Exception as e:
    print(f"An unexpected error occurred while reading the Excel file: {e}")
    exit(1)

# 选择数据帧的部分行
data_n = data_np.iloc[:10, :].copy()
data_p = data_np.iloc[14:24, :].copy()

# 尝试转换数据类型为float，无法转换的值设置为NaN
numeric_cols = data_n.columns.drop("Period")
data_n[numeric_cols] = pd.to_numeric(data_n[numeric_cols], errors='coerce')
data_p[numeric_cols] = pd.to_numeric(data_p[numeric_cols], errors='coerce')

# 打印数据类型和信息
print(data_n.info())
print(data_p.info())

# 示例DataFrame和修改测试
test_data = {
    "City A": [14.1, 14.1, 13.7],
    "City B": [11.0, 12.6, 12.1],
}
test_df = pd.DataFrame(test_data)

# 创建test_df的一个独立副本
test_copy = test_df.copy()

# 修改原始DataFrame
test_df.iloc[1, 1] = 99

# 打印原始和修改后的DataFrame
print("\ntest_df after modification:")
print(test_df)
print("\ntest_copy (should be unchanged):")
print(test_copy)