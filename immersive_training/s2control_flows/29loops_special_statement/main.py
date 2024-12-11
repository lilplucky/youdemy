"""
else part exec if cond in while loop eval to false
while can be term by vreak statement,in such cases the else part is ignored
runs if no break occurs and cond is false
>>> 
>>> i = 1
>>> while i < 8:
...     print(i)
...     i += 1
... 
1
2
3
4
5
6
7
>>> i = 1
>>> while i < 8:
...     print(i)
...     i += 1
... else:
...     print("i is no longer less than 8")
... 
1
2
3
4
5
6
7
i is no longer less than 8
>>> 

"""
