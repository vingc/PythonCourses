#! python

items={ "left":"517",
        "right":"519",
        "forward":"520",
        "backward":"521" 
      }

print( "items number:", len(items) )

print( "all itmes:", items )

for dir, addr in items.items():
    print( "key:", dir, ", value:", addr )

print("tuple of dict:", items.items() )

#add
items["south"] = "111"
del items["backward"]

print( "cur items:", items )

name = "swaroop"
#print("first char:",name[0], "second char:", name[1],\
 #     "last cahr:",name[-1],"which char:", name[-len(name)-1] )

print( "from 1 to 3:", name[1:3] )

bri = set(["india", "chian", "hongkong"])
print("set:", bri)

print("india" in bri)
print("in" in bri )
bri.add("taiwan")
print("new set:", bri)