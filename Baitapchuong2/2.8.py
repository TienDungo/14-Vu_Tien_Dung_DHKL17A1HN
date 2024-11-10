import json 
data = {"Name": "Dung",
         "age": 19, 
         "city": "Ha Noi",
         "company":"Lam_giau"}
json_data = json.dumps(data)
print(json_data)