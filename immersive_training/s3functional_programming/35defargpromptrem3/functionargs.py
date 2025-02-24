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
ask_ok('Do you really want to quit?')
