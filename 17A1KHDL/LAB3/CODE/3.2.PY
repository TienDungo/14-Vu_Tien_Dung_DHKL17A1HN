import pandas as pd

# Đọc file CSV vào DataFrame
path_1 = 'D:/17A1KHDL/LAB3/DATA/stocks1.csv'
stocks1 = pd.read_csv(path_1)

# 1. Kiểm tra xem trong stocks1 có dữ liệu Null nào không
print("Kiểm tra dữ liệu Null:")
print(stocks1.isnull().sum())  

# 2. Thay thế dữ liệu Null ở cột 'high' bằng giá trị trung bình của cột 'high'
high_mean = stocks1['high'].mean()  
stocks1['high'].fillna(high_mean, inplace=True)  

# 3. Thay thế dữ liệu Null ở cột 'low' bằng giá trị trung bình của cột 'low'
low_mean = stocks1['low'].mean()  # Tính giá trị trung bình của cột 'low'
stocks1['low'].fillna(low_mean, inplace=True)  # Thay thế giá trị Null bằng trung bình

# 4. Hiển thị thông tin tổng quan để xác nhận không còn dữ liệu Null
print("\nThông tin tổng quan sau khi thay thế dữ liệu Null:")
print(stocks1.info())  # Kiểm tra lại thông tin tổng quan của DataFrame
