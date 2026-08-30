#string 
print("hello world")

#assign string to a variable
x="hello world"
print(x)

#string are array
#Python does not have a character data type, a single character is simply a string with a length of 1
x = "hello world"
print(x[0])
print(x[1])

#looping through a string 
for x in "apple":
    print(x)

#string length
x ="hii! my name is palak pandey"
print(len(x))

#check string 
x = "Python is easy to learn"
print("my" in x)
print("easy" in x)

#slicing 
a="hello world"
print(a[2:5])

#slice from the start 
a="hello world"
print(a[:5])

#slice to the end 
a="hello world"
print(a[2:])

#negative indexing 
a="hello world"
print(a[-5:-2])

#modify strings
a="hello world"
print(a.upper())

a="HELLO WORLD"
print(a.lower())

#remove whitespace
a="  hello world"
print(a.strip())

#replace string 
a="hello world"
print(a.replace("h","i"))

#split string
a="hello world"
print(a.split(","))

#string concatenation
a="hello"
b="world"
c=a+" "+b
print(c)

#string format
age = 19
txt= f"i am {age}"
print(txt)

price=100
txt=f"the price is {price:.2f}"
print(txt)