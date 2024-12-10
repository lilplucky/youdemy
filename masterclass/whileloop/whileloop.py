"""
While Loop in Python 
Here while loop is very similar to C, CPP and Java 
As always while loop requires pre-defined variable(s)
With the while loop we can execute a set of statements as long as a condition is true.
"""
#define the while loop
i = 1 #Initialization
while i < 10: #Condition
    print(i) 
    i += 1 #Increament / DEcrement

#Using break
print()
i = 1
while i < 5:
    print(i)
    if i==3:
        break
    i += 1

#Using continue
print()
i = 0
while i < 5:
    i += 1
    if i==3:
        continue
    print(i)
    
#using else
print()
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("While loop executed successfully")