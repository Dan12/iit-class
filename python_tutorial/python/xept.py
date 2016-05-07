import math

anumber = 34

try:
   print(math.sqrt(anumber))
except:
   print("Bad Value for square root")
   print("Using absolute value instead")
   print(math.sqrt(abs(anumber)))
   
   
anumber = -34

try:
   print(math.sqrt(anumber))
except:
   print("Bad Value for square root")
   print("Using absolute value instead")
   print
   
# create custum errors
if anumber < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(anumber))
#other kinds of errors than runtimeErrors (See python documentation)