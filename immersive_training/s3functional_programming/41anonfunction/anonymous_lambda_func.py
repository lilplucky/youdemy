"""
defined without a name
defined using lambda keyword
small anon func can be created using lambda keyword only at first

"""
def make_incrementor(n):
    return lambda x: x + n #many arguments but only one expresion evaluated and returned

f = make_incrementor(42)
f(0)
f(1)

#works on python shell not scripted
#TESTED
