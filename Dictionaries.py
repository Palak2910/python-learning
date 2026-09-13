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
