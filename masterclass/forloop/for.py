"""
FOR LOOP 
For loop is used to iterate over collections (such as list, tuple, set, dictionary) or strings. 
It is very much similar to other programming languages.
"""

#define a list
list1=["1","2","3","4"]
list2=["A","B","C","D"]

#for each or for loop
#loop through the list
for x in list1:
    print(x)

print("I am outside for loop")

#for loop for string
for x in "PYTHON":
    print(x)


#nested for loop
for x in list1:
    for y in list2: #inner loop execs first
        print(x,y)

#using break in for loop
for x in list1:
    print(x)
    if x == "3":
        break

#using continue in for loop
for x in list1:
    if x == "3":
        continue
    print(x)