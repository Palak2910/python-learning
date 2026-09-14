#create and print a dictionaries
x={
    "brand": "Gucci",
    "item": "handbag",
    "year": 2020
}
print(x)

#Accessing item
thisdict ={
    "brand": "gucci",
    "Item": "handbag"
}
x = thisdict["Item"]
print(x)

#get 
thisdict ={
    "brand":"Gucci",
    "item": "handbag",
    "year": 2020
}
x = thisdict.get("item")
print(x)

#Get keys
thisdict ={
    "brand":"Gucci",
    "item": "handbag",
    "year": 2020
}
x = thisdict.keys()
print(x)

#change value 
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

#update
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

#Adding item
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)