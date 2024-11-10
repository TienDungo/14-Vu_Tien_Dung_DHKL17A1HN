import json

python_dict = {
    "Name": "Dung",
    "age": 19,
    "city": "Ha Noi",
    "skills": ["M", "game", " good"],
    "experience": {
        "company": "Lam_giau",
        "years": 20
    }
}

data = json.dumps(python_dict)
data_dict = json.loads(data)
print(data)
print('My name is',data_dict['Name'],data_dict['age'],'tuổi')