def sqr(n):
    return n**2
    
print(sqr(5))
print(sqr(sqr(3)))

def sqrt(n):
    root = n/2    #initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + (n / root))

    return root
    
print(sqrt(25))
print(sqrt(50))
print(sqrt(3))

globalTest = 0

def testFunc():
    # this gets the reference to the global variable
    # into the namespace of the function
    global globalTest
    globalTest += 1
    return None
    
def regFunc():
    globalTest = 1001
    return globalTest
    
print(testFunc())
print(globalTest)
print(regFunc())
print(globalTest)

