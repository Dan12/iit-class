print("hello world")

x = True
y = False
print(x or y)
print(x and y)
print(not x)
z = 1
print(y or z)
# same thing in memory
print(x is x)
print(x is not x)

x = 2
y = 6
print(x//y)
print(x/y)
print(y**x)
print(divmod(y,x))
x = complex(2,4)
print(x)
print(x.conjugate())
y = -5
print(-y)
print(+y)
print(y.__add__(z))
print(float(y))
print(id(y))
print(id(x))
print(id(z))

x = "Hello"
y = "WOrld"
print(x+y)
print(x*3)
print(len(x))
print(x[1:3])
print(x[2:])
# immutable, throws error
# x[2:4]="le"

x = """Hello
    World
ypo"""

l = ['hello', 1, True, 3]
       
print(x)

print(l[2])
print(2 in l)
print(l.pop())
del l[0]
print(l)
l[0] = ['hello','there']
print(l)
l[-1] = 0
print(l)
l[1:-1] = [5,4,3,2,1]
print(l)
print(x.split())

for c in "HelloWorld":
    if c == 'l':
        print(c, end="")
    else:
        print(c)
        
rows = x.split()

ls = [r.count("l") for r in rows]
print(x+"\n", ls)
        