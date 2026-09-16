#if statement 
a = 33
b = 200
if b > a:
  print("b is greater than a")

#if statement work 
number =15
if number > 0:
  print("the number is positive")

#multiple statement if block 
age = 20 
if age >= 18:
  print("you are an adult")
  print("you can vote")

#print elif statement 
a = 10
b = 5 
if a>b:
  print ("correct")
elif a==b:
  print("wrong")

#multiple elif 
score = 75
if score>90:
  print("highest marks")
elif score==90:
  print("highest marks")
elif score<90:
  print("lowest marks")

#else statement 
a = 10
b = 5
if a < b:
  print("correct")
else:
  print("wrong")

#python shorthand if
a = 10
b = 5 
if a > b: print("correct")

#logical operator
#And 
a = 10 
b = 5
if a>b and b<a:
  print("a is greater than b")

#Or
a = 10 
b = 5
if a>b or b<a:
  print("a is greater than b")

#Not 
a = 10 
b = 5
if not a>b:
  print("a is not greater than b")

#Nested 
x = 41
if x > 50:
  print("x is greater than 50")
  if x >=50:
    print("x is equal to 50")
else:
  print("wrong")

#nested 
username = "email"
password = "python"
is_active = True 
if username:
  if password:
    if is_active:
      print("login successful")
    else:
      print("Account is deactivated")
  else:
    print("Password incorrect")
else:
  print("username NOT found")

#pass statement 
a = 10 
b = 5 
if a>b:
  pass