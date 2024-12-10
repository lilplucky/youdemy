# Decision Making Statements in Python 
# Let's understand the if-else if-else statements in Python 
# define same values 
a = 10 
b = 20 
c = 30

#if statement
if b > a:
    print("B is greater than A")
    print("I am inside if")

print("I am outside if")

#if-else statment 
if b > a:
    print("B is greater than A")
else:
    print("A is greater than B")

#if-else if-else statement
if  b > a:
    print("B is greater than A")
elif a==b:
    print("Both are same")
else:
    print("A is greater than B")

print("----------executing shorthands ---------")
#Applicable only for single statements
#shorthand if
if b>a: print("B is greater than A")

#shorthand if-else
print("B is greater than A") if b > a else print("A is greater than B")

#shorthand if-elif-else
print("B is greater than A") if  b > a else print("Both are same")  if a==b else print("A is greater than B")

#using and keyword
if b>a and c>a:
    print("Both B and C are greater than A")
    
#using or keyword
if b>a or c>a:
    print("Both B and C are greater than A")
    


