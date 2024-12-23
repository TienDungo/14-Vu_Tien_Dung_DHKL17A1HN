import pandas as pd

#1. Đọc file CSV vào DataFrame
path_1 = 'D:/17A1KHDL/LAB3/DATA/stocks1.csv'
stocks1 = pd.read_csv(path_1)

#2. Hiển thị 5 dòng đầu tiên của DataFrame
print("5 dòng đầu tiên của stocks1:")
print(stocks1.head())

#3. Hiển thị kiểu dữ liệu (dtype) của mỗi cột
print("\nKiểu dữ liệu của mỗi cột:")
print(stocks1.dtypes)

#4. Xem thông tin tổng quan của DataFrame
print("\nThông tin tổng quan của stocks1:")
print(stocks1.info())
