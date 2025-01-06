"""
What is Tuple? 
Tuple is another type of collection such as List.
The difference is tuple is written with round brackets.
And it is ordered and unchangeble.
That means once tuple is created you cannot change the values.
This also means once tuple is created you cannot add items to it.
And you cannot remove items from tuple.
But we can delete tuple.
"""

#define a tuple
tuple1 = ("A","B","C","D","E","F","G")
print(tuple1)

#access the elements using index no
print(tuple1[3])

#check no of elements in the tuple
print(len(tuple1))

#return no. of times specific element is in the tuple
print(tuple1.count("A"))

#return index no. of a given element
print(tuple1.index("E"))

#LOOP with tuple
for x in tuple1:
    print(x)

if "B" in tuple1:
    print("Yes,B is present")

#another way to create a tuple,uing tuple() constructor
tuple2 = tuple(("A","B","C","D"))
print(tuple2)
