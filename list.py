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

#Loop through a list 
x=["banana","cheery","apple","orange","kiwi","mango"]
for i in x:
    print(i)

#Loop through a list using index
x=["banana","cheery","apple","orange","kiwi","mango"]
for i in range(len(x)):
    print(x[i])

#using while loop 
x=["banana","cheery","apple","orange","kiwi","mango"]
i=0
while i<len(x):
    print(x[i])
    i+=1

#list comprehension
x=["banana","cheery","apple","orange","kiwi","mango"]
newlist=[i for i in x if "a" in i]
print(newlist)

#sort list 
x=["banana","cheery","apple","orange","kiwi","mango"]
x.sort()
print(x)

#sort list in descending order
x=["banana","cheery","apple","orange","kiwi","mango"]
x.sort(reverse=True)
print(x)

#customized sort 
x=["banana","cheery","apple","orange","kiwi","mango"]
def myfunc(n):
    return len(n)

#reverse order
x=["banana","cheery","apple","orange","kiwi","mango"]
x.reverse()
print(x)

#Copy list 
x=["banana","cheery","apple","orange","kiwi","mango"]
y=x.copy()
print(y)

#copy list using list() method
x=["banana","cheery","apple","orange","kiwi","mango"]
y=list(x)
print(y)

#slice operator
x=["banana","cheery","apple","orange","kiwi","mango"]
print(x[2:5])
print(x[:4])
print(x[2:])

#Join two list
x=["banana","cheery","apple"]
y=["orange","kiwi","mango"]
z=x+y
print(z)

#Join two list using append() method
x=["banana","cheery","apple"]
y=["orange","kiwi","mango"]
for i in y:
    x.append(i)
    print(x)

#Join two list using extend() method
x=["banana","cheery","apple"]
y=["orange","kiwi","mango"]
x.extend(y)
print(x)