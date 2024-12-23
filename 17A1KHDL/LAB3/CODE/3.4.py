import pandas as pd
# Đọc file CSV vào DataFrame
path_1 = 'D:/17A1KHDL/LAB3/DATA/stocks1.csv' 
path_2 = 'D:/17A1KHDL/LAB3/DATA/stocks2.csv' 
# Đọc dữ liệu từ hai file CSV vào DataFram
stocks1 = pd.read_csv(path_1)
stocks2 = pd.read_csv(path_2)

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Đọc file CSV vào DataFrame companies
path_companies = 'D:/17A1KHDL/LAB3/DATA/companies.csv'  # Đường dẫn tới file companies.csv
companies = pd.read_csv(path_companies)

# Hiển thị 5 dòng đầu tiên của DataFrame companies
print("5 dòng đầu tiên của companies:")
print(companies.head())

# Kết hợp stocks (đã tạo từ bài 3) và companies dựa trên cột chung là symbol
# Giả sử stocks đã được tạo từ trước và có cột 'symbol'
merged_data = pd.merge(stocks, companies, left_on='symbol', right_on='name')

# Tính giá đóng cửa (close) trung bình cho mỗi công ty
avg_close_per_company = merged_data.groupby('name')['close'].mean()

# Hiển thị kết quả cho 5 công ty đầu tiên
print("\nGiá đóng cửa trung bình cho mỗi công ty (5 công ty đầu tiên):")
print(avg_close_per_company.head())