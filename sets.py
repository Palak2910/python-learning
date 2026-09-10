#create a set 
x={"apple","banana","cherry"}
print(x)

#length of the set
x={"apple","banana","cherry"}
print(len(x))

#type of the set 
x={"apple","banana","cherry"}
print(type(x))

#set constructor
x=set(("apple","banana","cherry"))
print(x)

#accessing items in the set
x={"apple","banana","cherry"}
for item in x:
    print(item)

#changing the value of the set or adding items in the set 
x={"apple","banana","cherry"} #once u create a set u cannot the value of the set but u can add or remove items from the set
x.add("Mango")
print(x)

#adding set 
x={"apple","banana","cherry"}
y={"kiwi","orange"}
x.update(y)
print(x)

#removing items from the set 
x={"apple","banana","cherry"}
x.remove("banana")
print(x)

#using discard, pop, del and clear to remove items from the set 
x={"apple","banana","cherry"}
x.discard("banana")
print(x)

x={"apple","banana","cherry"}
x.pop()
print(x)

x={"apple","banana","cherry"}
x.clear()
print(x)

#loop through a set 
x={"apple","banana","cherry"}
for i in x:
    print(i)

#joining two sets 
x={"apple","banana","cherry"}
y={"kiwi","orange"}
z=x.union(y)
print(z)

#joining set and tuple
x={"apple","banana","cherry"}
y=("kiwi","orange")
z=x.union(y)
print(z)

#joining set and list
x={"apple","banana","cherry"}
y=["kiwi","orange"]
z=x.union(y)
print(z)

#updating a set with another set 
x={"apple","banana","cherry"}
y={"kiwi","orange"}
x.update(y)
print(x)

#intesecting two sets
x={"apple","banana","cherry"}
y={"kiwi","banana","orange"}
z=x.intersection(y)
print(z)

#difference between two sets
x={"apple","banana","cherry"}
y={"kiwi","banana","orange"}
z=x.difference(y)
print(z)

#symmetric difference between two sets
x={"apple","banana","cherry"}
y={"kiwi","banana","orange"}
z=x.symmetric_difference(y)
print(z)

#fronzen set 
x=frozenset({"apple","banana","cherry"})
print(x)
print(type(x))
