#create a list
x=["orange","banana","cheery"]
print(x)

y=[1,2,3,4,5]
print(y)

#length of the list
x=["orange","banana","cheery"]
print(len(x))

#Accessing list items
x=["orange","banana","cheery"]
print(x[0])
print(x[1])
print(x[2])

#Negative indexing
x=["orange","banana","cheery"]
print(x[-1])
print(x[-2])
print(x[-3])

#checking the item in the list 
x=["banana","cheery","apple","orange","kiwi","mango"]
if "banana" in x:
    print("yes, banana is in the list")
else:
    print("no, banana is not in the list")

#changing the value of the list 
x=["banana","cheery","apple","orange","kiwi","mango"]
x[1:5]=["watermelon","grapes"]
print(x)    

#Inserting items in the list 
x=["banana","cheery","apple","orange","kiwi","mango"]
x.insert(2,"watermelon")
print(x)

#Appending items in the list 
x=["banana","cheery","apple","orange","kiwi","mango"]
x.append("watermelon")
print(x)

#Extending the list 
x=["banana","cheery","apple","orange","kiwi","mango"]
x.extend(["watermelon","grapes"])
print(x)

#Removing items from the list 
x=["banana","cheery","apple","orange","kiwi","mango"]
x.remove("apple")
print(x)

#Removing specific index from the list 
x=["banana","cheery","apple","orange","kiwi","mango"]
x.pop(3)
print(x)

#del keyword
x=["banana","cheery","apple","orange","kiwi","mango"]
del x[1]
print(x)

#clear the list 
x=["banana","cheery","apple","orange","kiwi","mango"]
x.clear()
print(x)
