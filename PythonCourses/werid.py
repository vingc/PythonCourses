#! python

def powerSum( power, *args ):
    total = 0
    print(args) #tuple
    for i in args:
        total += pow( i, power )

    return total

print( powerSum(2,10) )

def retTuple():
    return (2,3)

a,b = retTuple()

print(a, b)

c,*d = [1,2,3,4]
print(c, d)

list1 = [1,2,3,4]
list2 = [2*i for i in list1 if i < 3 ]

print(list2)


def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)
print(twice('word'))
print(twice(5))

exec("print('hello world')")
eval('print(2+3)')

assert twice(2) < 1