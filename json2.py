import json
x = {
    "name": "Narayan Pokharel",
    "age": 30,
    "married": False,
    "divorced": False,
    "children": None,
    "cars": [
        {"model":"BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg":24.1}
    ]


}
#y = json.dumps(x)
#parased_data = json.loads(y)
#second_car = parased_data["cars"][1]
#print(second_car)
print(json.dumps(x, indent = 4, separators=(".", "="), sort_keys=True))