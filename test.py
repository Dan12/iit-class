a = 5
b = 6

c,d=a,b

print(c)
print(d)

a = [1,2]
a[0], a[0][0] = [3,4], 5
print(a)
a = [1,2]
a[0][0], a[0] = 5, [3,4]
print(a)