"""
What is List
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.
Lists are just like dynamic sized arrays, similar to vector in C++ and ArrayList in Java. 
Lists need not be homogeneous always which makes it a most powerful tool in Python.
This means a single list may contain DataTypes like Integers, Strings, as well as Objects.
 In other words a list can contain different types of elements.
"""
#Define a list
list1 = ["A","B","C","D","E"]
# print the list
print(list1)

#Access the elements of list
print(list1[3])

#Total no. of elements in a list
print(len(list1))

#replace an element from list 
list1[3] = "F"
print(list1)

#Find the index no. of an element
x = list1.index("C")
print(x)

#Append an element in the list
list1.append("G")
print(list1)

#insert an element on a specific index no
list1.insert(2, "H")
print(list1)

#Loop with the list
for x in list1: #for(int 1 =0;i<10;i++)
    print(x)


#check if element exists or not
if "A" in list1:
    print("Yes, A is present")
    
