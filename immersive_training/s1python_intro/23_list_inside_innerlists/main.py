"""
>> 
>>> letters = ['a','b','c''d']
>>> letters
['a', 'b', 'cd']
>>> letters = ['a','b',c''d']
  File "<stdin>", line 1
    letters = ['a','b',c''d']
                           ^
SyntaxError: unterminated string literal (detected at line 1)
>>> a = ['a','b','']
>>> a
['a', 'b', '']
>>> a = ['a','b','c']
>>> a
['a', 'b', 'c']
>>> n = [1,2,3]
>>> x = [a,n]
>>> x
[['a', 'b', 'c'], [1, 2, 3]]
>>> x[0]
['a', 'b', 'c']
>>> x[0][1]
'b'
>>> 
"""
