#! python


def max(a,b):
    if a > b:
        print( a, "is bigger than", b )
    elif a < b:
        print( a, "is lower than" , b )
    else:
        print( a , "is equal to", b )


max(1,2)
max(3,1)
max(2,2)


x = 10
y = 20
z = 30

def tempGlobal():
    global x,y
    z = 20
    print("inner x:",x,"y:",y,"z:",z)
    x /= 2
    y /= 2
    print("inner x:",x,"y:",y,"z:",z)


print("outer x:",x,"y:",y,"z:",z)
tempGlobal();
print("outer x:",x,"y:",y,"z:",z)

a = 1

def nonLocal():
    a = 2
    print("x is", a)

    def nonLocal2():
       # nonlocal a
       global a
       a = 3

    nonLocal2()
    print("change a to", a)

nonLocal()
print("global a is", a)

def defaultParam( info, times = 1 ):
    print(info*times)

defaultParam("hello")
defaultParam("World ", 3)

#key parameters
def keyParm( a, b=5, c=10 ):
    print("a is", a, "b is", b, "c is", c )

keyParm( 1, 2 )
keyParm( 2, c=11 )
keyParm( b=4, c=12, a=1 )
#keyParm( 4, a=2 )

#varArgs
# * generate a list, ** generate a dictionary
def total( init = 4, *numbers, **params ):
    sum = init
    for i in numbers:  #number=(2,3,4)
        sum += i
    
    for key in params: #params={"kick":20, "chinken":30}
        sum += params[key]
    
    return sum

print( total( 5, 2, 3, 4, kick=20, chinken=30 ) )