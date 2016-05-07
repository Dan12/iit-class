import math

counter = 0

# until statement is false
while counter <= 5:
    print("Hello, world")
    counter = counter + 1
    
for item in [1,3,6,2,5]:
    print(item)

n = 3
if n<0:
   print("Sorry, value is negative")
else:
   print(math.sqrt(n))

# else if
score = 78
if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')
   
# list comperhension
sqlist=[]
for x in range(1,11):
    sqlist.append(x*x)
    
print(sqlist)

sqlist=[x*x for x in range(1,11) if x%2 != 0]
print(sqlist)
print([ch.upper() for ch in 'comprehension' if ch not in 'aeiou'])