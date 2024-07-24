import json 
'''x = '{"name":"Narayan", "age": 25, "city":"Butwal,Nayagaun"}'
print( json.loads(x))'''
x = {
    "name": "Narayan Pokharel",
    "age": 30,
    "city": "Nayagaun,Butwal",
    "Gender": "Male"
}
y = json.dumps(x)
print(y)

