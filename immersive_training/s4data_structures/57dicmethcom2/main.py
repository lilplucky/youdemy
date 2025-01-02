"""
>>> 
>>> tel['jack']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'jack'
>>> tel['Jack']
4098
>>> del tel['sape']
>>> tel
{'Jack': 4098, 'guido': 4127}
>>> tel['don'] = 4127
>>> tel
{'Jack': 4098, 'guido': 4127, 'don': 4127}
>>> sorted(tel)
['Jack', 'don', 'guido']
>>> tel
{'Jack': 4098, 'guido': 4127, 'don': 4127}
>>> 
"""
