# book: http://interactivepython.org/runestone/static/pythonds/Introduction/GettingStartedwithData.html

# lists, zero or more objects
myList = ["Lolo",234,True, 'n']

print(myList)
print(myList[2])
print(myList+[4])
print([12,"lo;"]*4)
print('n' in myList)
print(len(myList))
print(myList[1:3])
print(myList[0:4:2])

# list references
myList = [1,2,3,4]
A = [myList]*3
print(A)
myList[2]=45
print(A)

# list opperations
myList = [1024, 3, True, 6.5]
myList.append(False)
print(myList)
myList.insert(2,4.5)
print(myList)
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)

# ranges (last value not included), mutable
print(range(10))
print(list(range(1,10)))
print(list(range(1,12,3)))
print(list(range(10,1,-1)))

# strings (immutable)
myName = "Testnasme"
print(myName[2])
print(myName*2)
print(len(myName))
print(myName.upper())
print(myName.center(20))
print(myName.find("st"), myName.find('s'))
print(myName.split('s'))
print(myName.lower().count('t'))
print(myName.rjust(20))

# tuples, sequences of objects, immutable
myTuple = (2, True, 4.96)
print(myTuple*2)
print(myTuple[0:2])
try:
    myTuple[0] = False
except:
    print("Can't change tuples")
    
# sets, unordered collection of objects, heterogeneous, immutable
# several methods to create sets from union of sets, intersections, and, or
mySet = {"lol","item",54,'l',True}
print(mySet)
# removes arbitrary element
mySet.pop()
print(mySet)
print(False in mySet)
mySet.clear()
print(mySet)
mySet = set()
print(mySet)

# dictionaries
# pairs of keys and values
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)
del capitals["Iowa"]
print(capitals)
print(capitals.get("Iowa","Nothing"))