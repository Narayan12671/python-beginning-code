thisdict = {
    "Brand": "Bajaj",
    "Model": "Pulasar 150, pulsar200, pulsar220, Pulsar250, Dominar250, Dominar400, Discover125, Platina100",
    "manufacturing_Country": "India",
    "color": "red, black_red, Blue, Grey"

}
thisdict.update({"year": 2020})
thisdict.popitem()
thisdict.pop("manufacturing_Country")
x = thisdict.keys()
y = thisdict.values()
print(x)
print(y)
#print(thisdict["Model"])