def foo():
    """Foo does something"""
    return bar()

def bar():
    return "Lol"

print(foo())

def foo():
    return "CHanged"
    
print(foo())

def foo(x,y):
    return x+y
    
f = foo

print(foo(1,2))

g = 100

def foo(x):
    g = x*2
    return g
    
print(foo(10))
print(g)

def foo(x):
    return g
    
print(foo(10))
print(g)

def foo(x):
    global g # declares g to be global
    g = x*2
    return g
    
print(foo(10))
print(g)

# defining default values in function
def foo(x=10, y=20):
    return x, y

print(foo(y=3, x=5))
print(foo())

def foo(x,y,*whatever):
    return x,y,whatever

print(foo(1,2,3,4))

def foo(x, *what, y):
    return x,y,what
    
print(foo(1,2,3,4,5,y=9))

a = b = 100
print(a,b)

def foo(x,**dictionary):
    return x,dictionary
    
print(foo(12,im="awesome",youre="not"))

def reduce(combiner, *vals, start=0):
    """Combines all items in vals with the provided
    combiner function and start value"""
    accum = start
    for item in vals:
        accum = combiner(accum, item)
    return accum

def add(m, n):
    return m+n

print(reduce(add, 1, 2, 3, 4))
print(reduce(add, 'hello', 'world', start=''))

def mult(m,n):
    return m*n

print(reduce(mult,1,2,3,4))
print(reduce(mult,1,2,3,4, start=1))