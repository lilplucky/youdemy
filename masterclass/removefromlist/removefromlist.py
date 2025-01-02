"""
Remove Item 
There are several methods to remove items from list1 
1. remove() Removes specific item 
2. pop(indexNo) Removes the specified index AddtionWithInput.py
3. pop() Removes the last item if index is not specified Assignments.txt
4. del keyword with given index number deletes specific element Comments.py
5. del keyword without index no. deletes whole list Hello.py 
6. clear() empties the list, will not delete the list
"""

# Define a list 
list1= ["A", "B", "C", "D", "E"]
list2 = ["1", "2", "3", "4", "5"]

print(list1)

# using remove()
list1.remove("C")
print(list1)

#using pop() with index no
list1.pop(1)
print(list1)

print(list2)

#using del keyword with index no
del list2[3]
print(list2)

#using del keyword with no index no
#del list2 #delete whole list
print(list2)

#using clear()
list1.clear()
print(list1)
