import pandas as pd

# Đọc file CSV vào DataFrame
path_1 = 'D:/17A1KHDL/LAB3/DATA/stocks1.csv'  # Đường dẫn tới file stocks1.csv
path_2 = 'D:/17A1KHDL/LAB3/DATA/stocks2.csv'  # Đường dẫn tới file stocks.csv
# Đọc dữ liệu từ hai file CSV vào DataFram
stocks1 = pd.read_csv(path_1)
stocks2 = pd.read_csv(path_2)

# 2. Gộp stocks1 và stocks2 thành DataFrame mới tên là stocks
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# 3. Tính giá trung bình (open, high, low, close) cho mỗi ngày
stocks['average_price'] = stocks[['open', 'high', 'low', 'close']].mean(axis=1)

# 4. Hiển thị 5 dòng đầu tiên của kết quả
print("5 dòng đầu tiên của DataFrame kết quả:")
print(stocks.head())
