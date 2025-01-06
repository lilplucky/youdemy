"""
tripple single quotes or tripple double quotes
eol can  be prev by adding backslash at end of line
>>> 
>>> print("""\)
... Usage: thingy [options]
...     -h
...     -H hostname
... """)
\)
Usage: thingy [options]
        -h
        -H hostname

>>> 3 * 'un' + 'iun'
'unununiun'
>>> 'Py' 'thon'
'Python'
>>> text = ('Put several strings within parentheses '
...         'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>> perfix = 'Py'
>>> perfix 'thon' #can't concatenate a variable and a string literal
  File "<stdin>", line 1
    perfix 'thon' #can't concatenate a variable and a string literal
           ^^^^^^
SyntaxError: invalid syntax
>>> 
"""
