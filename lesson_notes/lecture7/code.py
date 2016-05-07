class Foo:
    # doesn't have to be self
    def bar(slf,x):
        slf.x = x
        print(x)
        
f = Foo()
f.bar(1)

# add new methods to current 
# classes

def baz(self,y):
    self.y = y
    print(y)
    
Foo.mbaz = baz
f.mbaz(3)