#Tuple
x=("banana","cheery","apple","orange","kiwi","mango")
print(x)

#tuple length
x=("banana","cheery","apple","orange","kiwi","mango")
print(len(x))

#tuple with different data types
x=(10,"apple",True,False,3.14)
print(x)

#Access tuple items
x=("banana","apple","mango")
print(x[1])

#negative indexing
x=("banana","apple","mango")
print(x[-1])

#checking the item in the tuple
x=("banana","apple","mango")
if"apple" in x:
    print("yes, apple is in the tuple")
else:
    print("no, apple is not in the tuple")

#changing the value of the tuple
x=("banana","apple","mango")
y=list(x)
y[1]="kiwi"
x=tuple(y)
print(x)

#adding items in the tuple 
x=("banana","apple","mango")
y=list(x)
y.append("kiwi")
x=tuple(y)
print(x)

#removing items from the tuple
x=("banana","apple","mango")
y=list(x)
y.remove("apple")
x=tuple(y)
print(x)

#unpacking the tuple
x=("banana","apple","mango")
(banana,apple,mango)=x
print(banana)

#using asterisk(*) to unpack the tuple
x=("banana","apple","mango","kiwi","grapes")
(banana,apple,*fruits)=x
print(banana)
print(apple)
print(fruits)

#looping through the tuple
x=("banana","apple","mango")
for i in x:
    print(i)

#looping through the tuple using index
x=("banana","apple","mango")
for i in range(len(x)):
    print(x[i])

#joining two tuples
x=("banana","apple","mango")
y=("kiwi","grapes")
z=x+y
print(z)

#using while loop 
x=("banana","apple","mango")
i=0
while i<len(x):
    print(x[i])
    i+=1

#multiplying the tuple
x=("banana","apple","mango")
y=x*2
print(y)
