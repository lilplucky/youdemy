"""
>>> 
>>> #tuples are immutable
>>> t[0] = 8888
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> #but they can contain mutable objects
>>> v = ([1,2,3], [3,2,1])
>>> v
([1, 2, 3], [3, 2, 1])
>>> emppty = ()
>>> empty = ()
>>> singleton = 'hello', #trailing comma makes it a tuple
>>> len(empty)
0
>>> len(singleton)
1
>>> singleton
('hello',)
>>> 
"""
