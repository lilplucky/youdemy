"""
step value cannot be zero
returns seq when iterated over

>> 
>>> for i in range(5):
...     print(i)
... 
0
1
2
3
4
>>> range(5,10)
range(5, 10)
>>> for i in range(5,10):
...     print(i)
... 
5
6
7
8
9
>>> for i in range(0,10,3):
...     print(i)
... 
0
3
6
9
>>> for i in range(-10,100,-30):
... 
KeyboardInterrupt
>>> for i in range(-10,-100,-30):
...     print(i)
... 
-10
-40
-70
>>> a = ['Mary','had','a','little','lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
... 
0 Mary
1 had
2 a
3 little
4 lamb
>>> print(range(10))
range(0, 10)
>>> sum(range(4))
6
>>> sum(range(12))
66
>>> list(range(4))
[0, 1, 2, 3]
>>> list(range(12))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
>>> 
"""
