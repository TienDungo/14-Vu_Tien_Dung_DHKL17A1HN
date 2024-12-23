import pandas as pd
# Đọc file CSV vào DataFrame
path_1 = 'D:/17A1KHDL/LAB3/DATA/stocks1.csv' 
path_2 = 'D:/17A1KHDL/LAB3/DATA/stocks2.csv' 
# Đọc dữ liệu từ hai file CSV vào DataFram
stocks1 = pd.read_csv(path_1)
stocks2 = pd.read_csv(path_2)

stocks = pd.concat([stocks1, stocks2], ignore_index=True)


# 1. Tạo MultiIndex cho DataFrame stocks bằng cách sử dụng cột 'date' và 'symbol' làm chỉ mục
stocks.set_index(['date', 'symbol'], inplace=True)

# 2. Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình cho mỗi ngày, mỗi mã chứng khoán
avg_stocks = stocks.groupby(['date', 'symbol']).agg({
    'open': 'mean',
    'high': 'mean',
    'low': 'mean',
    'close': 'mean',
    'volume': 'mean'
})

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán
avg_stocks.sort_index(inplace=True)

# 4. Hiển thị kết quả cho 5 ngày đầu tiên
print(avg_stocks.head(5))