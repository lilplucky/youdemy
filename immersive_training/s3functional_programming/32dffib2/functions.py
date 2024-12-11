"""

"""
def fib(n): #write  fibonacci series up to n
    """ Print a Fibonacci series up to n"""
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    print()
    
#Now call the function we just defined:
#fib(2000)
#print(fib) #get object location
f = fib
#f(100)
#f(0)
fib(0)


def fib2(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

f100 = fib2(100)
print(f100)



