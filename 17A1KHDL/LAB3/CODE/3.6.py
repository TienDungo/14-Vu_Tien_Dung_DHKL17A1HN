import pandas as pd
# Đọc file CSV vào DataFrame
path_1 = 'D:/17A1KHDL/LAB3/DATA/stocks1.csv' 
path_2 = 'D:/17A1KHDL/LAB3/DATA/stocks2.csv' 
# Đọc dữ liệu từ hai file CSV vào DataFram
stocks1 = pd.read_csv(path_1)
stocks2 = pd.read_csv(path_2)

stocks = pd.concat([stocks1, stocks2], ignore_index=True)



# Tạo Pivot Table với date làm chỉ mục, symbol làm cột, và giá trị trung bình của 'close'
pivot_table = pd.pivot_table(stocks, values='close', index='date', columns='symbol', aggfunc='mean')
print(pivot_table)


# Tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol)
total_volume = stocks.groupby('symbol')['volume'].sum()

# Thêm cột tổng volume vào Pivot Table
pivot_table['total_volume'] = pivot_table.columns.map(total_volume)
print(pivot_table)

# Sắp xếp Pivot Table theo tổng volume giao dịch từ cao xuống thấp
pivot_table_sorted = pivot_table.sort_values(by='total_volume', axis=1, ascending=False)
print(pivot_table_sorted)

# Hiển thị 5 mã chứng khoán có tổng volume giao dịch cao nhất
top_5_symbols = pivot_table_sorted.iloc[:, :5]
print(top_5_symbols)
