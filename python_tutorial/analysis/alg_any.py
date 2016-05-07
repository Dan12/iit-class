import time

def sumOfN(n):
   theSum = 0
   for i in range(1,n+1):
       theSum = theSum + i

   return theSum

def sumOfN2(n):
   start = time.time()

   theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i

   end = time.time()

   return theSum,end-start

print(sumOfN(10))
       
for j in range(3):
    for i in range(3):
        print("Sum is %d required %10.7f seconds"%sumOfN2(1000000*(j+1)))
    
def sumOfN3(n):
    start = time.time()
    
    end = time.time()

    return (n*(n+1))/2,end-start

for j in range(3):
    for i in range(3):
        print("Sum is %d required %10.7f seconds"%sumOfN3(1000000*(j+1)))
    
    
# Big-O notation
# order of magnitude: part of T(n), number of steps, 
# that increases the fastest
# Big-O, O(f(n))
# Run time is O(n)
# T(n)=5n^2+27n+1005 -> O(n^2)
# common functions
# 1 	  Constant
# log(n)  Logarithmic
# n	      Linear
# nlog(n) Log Linear
# n^2     Quadratic
# n^3	  Cubic
# 2^n	  Exponential


# example
# 3
a=5
b=6
c=10
# 3n^2
for i in range(n):
   for j in range(n):
      x = i * i
      y = j * j
      z = i * j
# 2n   
for k in range(n):
   w = a*k + 45
   v = b*b
# 1 
d = 33
# T(n)=3+3n^2+2n+1
# O(n^2)