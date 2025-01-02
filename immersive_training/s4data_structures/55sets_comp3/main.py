"""
>>> 
>>> a - b
{'b', 'r', 'd'}
>>> #above elements present in a but not in b
>>> a | b
{'a', 'd', 'r', 'm', 'c', 'l', 'b', 'z'}
>>> a & b
{'a', 'c'}
>>> a ^ b
{'d', 'b', 'z', 'l', 'm', 'r'}
>>> #above elements in a or b but not both
>>> a = {x for x in 'abracadabra' if x not in 'abc'}
>>> a
{'r', 'd'}
>>> 
"""
