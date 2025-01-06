"""
The range() function: 
1. returns a sequence of numbers, starting from @ by default 
2. increments by 1 (by default) 
3. ends at a specified number.
"""

#loop upto 5
for x in range(5):
    print(x)

#loop up to 5 starting from 1
print("---------------range from 1 to 5---------------------")
for x in range(1,5):
    print(x)

#step increase.For ex PRINT TABLE OF 2
print("------------------step increase is 2-----------------------------")
for x in range(2,21,2):
    print(x)


#using else in for loop
print()
for x in range(5):
    print(x)
else:
    print("For loop executed successfully")
    