# return value will be a string
aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(),
      "and has length", len(aName))
      
sradius = input("Please enter the radius of the circle ")
radius = float(sradius)
diameter = 2 * radius
print(radius)
print(diameter)

# comma seperated, default sep = " "
print("Hello","World", sep="***")
# end default = "\n"
print("Hello","World", end="***")

# string formatting
price = 24000
item = "banana"
print("The %s costs %d cents"%(item,price))
                        #field is min 5 spaces wide total
print("The %+10s costs %5.2f cents"%(item,price))
print("The %+10s costs %10.2f cents"%(item,price))
itemdict = {"item":"banana","cost":24}
print("The %(item)s costs %(cost)7.1f cents"%itemdict)
#strings also include format method (refer to python documentation)

