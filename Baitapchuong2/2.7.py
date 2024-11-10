# chuyển python sang json
import json
data = '{"Name": "Dung", "age": 19, "city": "Ha Noi","company":"Lam giau"}'
python_obj = json.loads(data)

print(python_obj)