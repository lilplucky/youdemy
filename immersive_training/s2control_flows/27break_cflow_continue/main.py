"""
>>> for n in range(2,10):
...     for x in range(2,n):
...             if n % x == 0:
...                     print(n, 'equals', x, '*' , n//x)
...                     break
...     else:
...             print(n, 'is a prime number')
... 
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
>>> 
>>> for num in range(2,10):
...     if num % 2 == 0:
...             print("Found an even number", num)
...             continue
...     print("Found a number", num)
... 
Found an even number 2
Found a number 3
Found an even number 4
Found a number 5
Found an even number 6
Found a number 7
Found an even number 8
Found a number 9
>>> 
"""
