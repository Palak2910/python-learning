#Arithmetic operators
a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

#Logical operators
a =10
print(a>5 and a<15) #And operator
print(a>5 or a<15) #Or operator
print(not(a>5 and a<15)) #Not operator

#Comparison operators
a=20
b=10
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#Assignment operators
x=10
print(x)

x=10
x+=3
print(x)

x=10
x-=3
print(x)

x=10
x*=3
print(x)

x=10
x/=3
print(x)

x=10
x%=3
print(x)

x=10
x//=3
print(x)

x=10
x**=3
print(x)

x=10
x&=3
print(x)

x=10
x|=3
print(x)

x=10
x^=3
print(x)

x=10
x>>=3
print(x)

x=10
x<<=3
print(x)

#Ternary Operator
num = 7
x="WEEKEND" if num>5 else "WEEKDAY"
print(x)

#Identity operators
a=10
b=10
print(a is b)

a="apple"
b="banana"
print(a is not b)

#Membership operators
a="apple"
b="banana"
print("a" in a)
print("b" not in b)

#Bitwise operators
a=6
b=3
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<1)
print(a>>1)
