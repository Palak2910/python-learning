#creating variables
x=10
y="neha"
print(x)
print(y)

#assigning multiple values 
x,y,z="Hello","world",10
print(x)
print(y)
print(z)

#one value with multiple variables
x=y=z="hello world"
print(x)
print(y)
print(z)

#unpacking collections
animals = ["dog","cat","parrot"]
x,y,z=animals
print(x)
print(y)
print(z)

#variables output
#print()function
x="my name is riya"
print(x)

#separated by comma,
x="hello"
y="world"
print(x,y)

#added by +
x="hello"
y="world"
print(x+y)

#global variables
x="great and easy language"

def myfunc():
    print("python is "+x)

myfunc()    

#creating a global variable inside a function
x="great"

def myfunc():
    x="easy language"
    print("python is "+x)

myfunc()
print("python is "+x)
