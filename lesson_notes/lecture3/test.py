print("Hello World")

newlist = """sfasf
             sadfasf
             wfasdfsf
             asdfasf
             asdfasf"""
             
rows = newlist.split()

print(rows)
print(rows[0].count("s"))

counts = []
for r in rows:
    counts.append(r.count("a"))
    
print(counts)

newcounts = [r.count("a") for r in rows]

print(newcounts)

testTuple = (1.5,-2.0)
print(testTuple)
# otherwise just parenthesized 5
oneTuple = (5,)
print(oneTuple)
# all same object
zeroTuple = ()
print(zeroTuple)

print(5 in range(0,10))
print(3 in range(0,10,2))

rangeList = list(range(20,10,-3))
print(rangeList)

# this is a range, normalizes range, 8 = 11-3
# endpoint is on continum
print(range(20,10,-3)[2:])

# default start is 0
print(range(10))