class badFrac:
    top = 0
    bottom = 0

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

class Fraction:
    
    # constructor
    def __init__(self,top,bottom):
        # internal data objects, not like badFrac
        self.num = top
        self.den = bottom
        
    def show(self):
        print(self.num,"/",self.den, sep="")
    
    # overriding tostring
    def __str__(self):
        return "A Fraction: "+str(self.num)+"/"+str(self.den)
     
    # overriding + operation on fraction
    def __add__(self,otherfraction):

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(self.num, self.den)
        # integer division (/ produces float)
        return Fraction(newnum//common,newden//common)
        
    # override equality
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum == secondnum

#calls __init__ 
myFrac = Fraction(2,3)
print(Fraction)
print(myFrac)
myFrac.top = 5
print(myFrac.top)

# look at all this crap, don't ever do it
bf = badFrac
print(bf.top)
bf2 = badFrac
print(bf2.bottom)
badFrac.top = 3
badFrac.left = 2
print(bf.top,",",bf.left,",",bf2.top)
bf2.right = 10001
print(badFrac.right)
print(bf.right)

myFrac.show()
frac2 = Fraction(4,6)
print(frac2+myFrac)

print(myFrac == frac2)

# inheritence
