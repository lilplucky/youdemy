"""
raise raises an exception
"""

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye','yes'):
            return True
        if ok in ('n','no','nop','nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
            print(RuntimeWarning)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?, 2')
ask_ok('OK to overwrite the file?', 2,'Come on,only yes or no')

i = 5
def f(arg=i):
    print(arg)
i = 6
f()

def f(a, L=[]):
    L.append(a)
    return L

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
