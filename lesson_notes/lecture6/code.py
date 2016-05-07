print(sorted([1,2,-4,5,-10,3]))
print(sorted([1,2,-4,5,-10,3], reverse=True))
print(sorted([(5,3),(1,-1),(5,4),(6,3)]))
print(sorted([(5,3),(1,-1),(5,4),(1,3)], key=lambda x: x[0]**2+x[1]**2))


things = []
def rememberall(thing):
    things.append(thing)
    print(",".join(things))
j = rememberall("This")
m = rememberall("This thing")


def makerememberall(name):
    # closed in scope in rememberall
    things = []
    #function conatained in another function
    #closure, closes over the local variables defined in its scope
    def rememberall(thing):
        things.append(thing)
        print(name, ":",",".join(things))
    return rememberall
    
j = makerememberall("this")
j("glasses")